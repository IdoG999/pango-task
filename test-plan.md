# Part 1 - Exploration & Test Plan

## What did I choose to test, and why?

I focused mainly on the Dashboard, and I also covered History and Users.

The Dashboard is the most important tab because it supports the core parking flow. This is where users perform the main business actions, like starting parking, ending parking, assigning slots, and uploading vehicle images. If the Dashboard is unstable, the core product value is affected immediately.

## How did I structure my testing approach?

I used a simple flow that follows business importance:

1. Dashboard first - validate core parking actions, validations, and error handling.
2. History second - verify that Dashboard actions are recorded correctly and safely.
3. Users third - validate account creation rules and admin behavior.

This approach helped me find high-impact issues early, then confirm traceability and user-management quality.

## What did I consider important? (risk, edge cases, user flows)

- Business risk: core parking actions must work correctly at all times.
- Data integrity: slot, plate, and image data must be valid and reliable.
- User trust: success and error messages must be accurate and real-time.
- Privacy and access: users should only see data they are allowed to see.
- Operational usability: History should support practical search and filtering.

Significant bugs identified (top 8)

BUG-01 - Missing vehicle type options
- Tab: Dashboard
- Severity: Major
- Business impact: Parking pricing and rules may be incorrect because only one generic vehicle type is available.
- Observed behavior: The system provides only a single vehicle type option (standard).
- Expected behavior: The system should support multiple relevant vehicle types (for example private car, motorcycle, bus, truck/heavy vehicle), according to business rules.

BUG-02 - Invalid slot input is accepted
- Tab: Dashboard
- Severity: Critical
- Business impact: Invalid slot data can break parking management accuracy and operational trust.
- Observed behavior: Slot accepts letters, symbols, and very long non-realistic values.
- Expected behavior: Slot should accept only valid format and range based on defined parking slot rules.

BUG-03 - Two vehicles can be assigned to the same slot
- Tab: Dashboard
- Severity: Critical
- Business impact: Allows conflicting active parking assignments and causes billing/operational errors.
- Observed behavior: A second vehicle can be parked in a slot that was already used, without proper occupancy validation.
- Expected behavior: The system should block new assignment when the slot is occupied and allow assignment only after it is available.

BUG-04 - End parking shows error even when operation succeeds
- Tab: Dashboard
- Severity: Major
- Business impact: Misleading feedback reduces user confidence and may cause repeated actions.
- Observed behavior: User receives an error message when ending parking, but the session is actually closed and visible in History.
- Expected behavior: System should display a success message when parking ends successfully.

BUG-05 - Non-image files accepted as vehicle image
- Tab: Dashboard
- Severity: Major
- Business impact: Poor data quality and potential misuse of upload field.
- Observed behavior: Upload accepts files that are not image types (for example PDF).
- Expected behavior: Upload should enforce valid image MIME types and reject unsupported files.

BUG-06 - History exposes questionable and invalid records
- Tab: History
- Severity: Major
- Business impact: Data integrity and privacy concerns; users may see records with invalid plate formats and poor media quality.
- Observed behavior: History includes records with invalid plate lengths/formats and entries with missing or irrelevant images.
- Expected behavior: History should display only valid, relevant records that meet data validation standards.

BUG-07 - Missing History search and filtering capabilities
- Tab: History
- Severity: Major
- Business impact: Hard to audit and investigate parking activity efficiently.
- Observed behavior: No search/filter options by date, time, user, slot, or plate.
- Expected behavior: History should provide practical filtering/search to support operational and support workflows.

BUG-08 - User creation lacks credential policy enforcement
- Tab: Users
- Severity: Major
- Business impact: Weak account security and inconsistent user data quality.
- Observed behavior: Usernames and passwords can be created without policy constraints.
- Expected behavior: System should enforce clear username/password policy (length, character requirements, and invalid pattern blocking).

## Representative test cases (well-structured, not exhaustive)

This is a representative set of test cases and not a full exhaustive suite.

Test data for login scenarios

Valid credentials:
- Username: admin
- Password: password

Invalid credentials:
- Username: admin
- Password: wrong

TC-01 - Login with valid credentials
Tab: Authentication
Priority: High
Severity: Critical

STEP 1: Navigate to application
ACTION: Open browser -> http://localhost:5000
EXPECTED: Login page loads with "Sign In" button

STEP 2: Enter credentials
ACTION: Username field -> type "admin"
ACTION: Password field -> type "password"
EXPECTED: No validation errors, fields accept input

STEP 3: Submit login
ACTION: Click "Sign In" button
EXPECTED: Loading spinner appears and disappears in less than 3 seconds

STEP 4: Verify dashboard
ACTION: Wait for redirect
EXPECTED: Dashboard loads and navigation menu is visible

TC-02 - Login with invalid credentials
Tab: Authentication
Priority: High
Severity: Major

STEP 1: Open login page
ACTION: Open browser -> http://localhost:5000
EXPECTED: Login page is displayed

STEP 2: Enter invalid credentials
ACTION: Username field -> type "admin"
ACTION: Password field -> type "wrong"
EXPECTED: Fields accept input

STEP 3: Submit login
ACTION: Click "Sign In"
EXPECTED: Clear error message is displayed and user stays on login page

TC-03 - Login with missing username
Tab: Authentication
Priority: Medium
Severity: Major

STEP 1: Open login page
ACTION: Open browser -> http://localhost:5000
EXPECTED: Login page is displayed

STEP 2: Leave username empty
ACTION: Username field -> keep empty
ACTION: Password field -> type "password"
EXPECTED: Form allows only valid required inputs

STEP 3: Submit
ACTION: Click "Sign In"
EXPECTED: Validation message for missing username and no login

TC-04 - Login with missing password
Tab: Authentication
Priority: Medium
Severity: Major

STEP 1: Open login page
ACTION: Open browser -> http://localhost:5000
EXPECTED: Login page is displayed

STEP 2: Leave password empty
ACTION: Username field -> type "admin"
ACTION: Password field -> keep empty
EXPECTED: Form allows only valid required inputs

STEP 3: Submit
ACTION: Click "Sign In"
EXPECTED: Validation message for missing password and no login

TC-05 - Login with both fields empty
Tab: Authentication
Priority: Medium
Severity: Major

STEP 1: Open login page
ACTION: Open browser -> http://localhost:5000
EXPECTED: Login page is displayed

STEP 2: Keep fields empty
ACTION: Username field -> keep empty
ACTION: Password field -> keep empty
EXPECTED: Fields remain empty

STEP 3: Submit
ACTION: Click "Sign In"
EXPECTED: Required field validation appears for both fields

TC-06 - Prevent duplicate active slot assignment
Tab: Dashboard
Priority: High
Severity: Critical
Related bug: BUG-03

STEP 1: Create first parking session
ACTION: Login and start parking in slot 101 with valid data
EXPECTED: Session starts successfully in slot 101

STEP 2: Try second session on same slot
ACTION: Attempt to start another parking session in slot 101 for a different vehicle
EXPECTED: Operation is blocked with clear occupancy message

TC-07 - Validate slot input format
Tab: Dashboard
Priority: High
Severity: Critical
Related bug: BUG-02

STEP 1: Open start parking form
ACTION: Navigate to Dashboard parking form
EXPECTED: Form is visible

STEP 2: Enter invalid slot values
ACTION: Try slot values with letters, symbols, and very long text
EXPECTED: Invalid values are rejected by validation

STEP 3: Enter valid slot value
ACTION: Enter a valid numeric slot value
EXPECTED: Form accepts value

TC-08 - Verify end parking feedback accuracy
Tab: Dashboard
Priority: High
Severity: Major
Related bug: BUG-04

STEP 1: Start active parking
ACTION: Start a parking session with valid data
EXPECTED: Active session is created

STEP 2: End parking
ACTION: Click end parking for that active session
EXPECTED: Success message is shown (not error)

STEP 3: Confirm record
ACTION: Open History
EXPECTED: Session appears as ended and data is consistent

TC-09 - Validate vehicle type options coverage
Tab: Dashboard
Priority: Medium
Severity: Major
Related bug: BUG-01

STEP 1: Open vehicle type selector
ACTION: Click vehicle type dropdown on Dashboard
EXPECTED: Dropdown opens

STEP 2: Review available options
ACTION: Compare listed options to expected categories
EXPECTED: Supported categories are present (not only standard)

TC-10 - Restrict upload to image files only
Tab: Dashboard
Priority: Medium
Severity: Major
Related bug: BUG-05

STEP 1: Upload invalid file
ACTION: Try uploading a PDF file as vehicle image
EXPECTED: Upload is blocked with validation message

STEP 2: Upload valid image
ACTION: Upload JPG or PNG file
EXPECTED: Upload is accepted

TC-11 - Validate history record quality and visibility
Tab: History
Priority: Medium
Severity: Major
Related bugs: BUG-06, BUG-07

STEP 1: Generate data from Dashboard
ACTION: Create and end parking sessions with valid data
EXPECTED: Sessions are recorded

STEP 2: Open History
ACTION: Navigate to History tab
EXPECTED: Records contain valid plate formats and relevant images

STEP 3: Check filters
ACTION: Try filtering by date, time, user, slot, and plate
EXPECTED: Filtering is available and results are accurate

TC-12 - Enforce username and password policy
Tab: Users
Priority: Medium
Severity: Major
Related bug: BUG-08

STEP 1: Open user creation
ACTION: Navigate to Users tab and open create user form
EXPECTED: Form is displayed

STEP 2: Submit weak credentials
ACTION: Enter invalid username/password combinations
EXPECTED: Validation blocks invalid values with clear messages

STEP 3: Submit valid credentials
ACTION: Enter valid username/password based on policy
EXPECTED: User is created successfully

TC-13 - Non-admin user cannot delete other users
Tab: Users
Priority: High
Severity: Major

STEP 1: Login as non-admin user
ACTION: Sign in with a user that does not have admin permissions
EXPECTED: Login succeeds and Users tab is accessible according to role permissions

STEP 2: Open users list
ACTION: Navigate to Users tab and review other user rows
EXPECTED: No delete option is shown for other users

STEP 3: Validate UI restrictions
ACTION: Check row actions and page controls
EXPECTED: Delete action is hidden or disabled for non-admin user

TC-14 - Deleting user with parking sessions shows immediate warning
Tab: Users
Priority: High
Severity: Major

STEP 1: Prepare target user with parking history
ACTION: Use a user that already has parking sessions in the system
EXPECTED: User appears in Users list with existing history

STEP 2: Try deleting target user
ACTION: As admin, click delete on that user
EXPECTED: Warning message appears immediately saying deletion is blocked due to existing parking sessions

STEP 3: Verify no delayed error behavior
ACTION: Stay on same screen, then logout and login again with any user
EXPECTED: No delayed delete error appears after re-login; warning must appear only at delete attempt time
