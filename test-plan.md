# Part 1 - Exploration and Test Plan

## 1) Scope and Testing Focus

I focused mainly on the **Dashboard** and also tested **History** and **Users**.

The Dashboard is the most important area because it supports the core parking flow. Most critical business actions happen there, such as starting and ending parking sessions and assigning parking slots. If this tab fails, the main product value is affected immediately.

## 2) How I Structured the Testing Approach

I followed this flow:

1. **Dashboard first** - test the main parking functionality and data validation behavior.
2. **History second** - verify that actions performed on Dashboard are recorded correctly.
3. **Users last** - test user management behavior, permissions, and validations.

This order helped me validate the most important user journey first, then confirm traceability and administration behavior.

## 3) What I Considered Important

- **Business risk:** parking flow is the core function, so Dashboard got highest priority.
- **Data quality:** invalid plate numbers, invalid slot values, and bad media data can damage system reliability.
- **Access and privacy:** user data visibility in History and user management permissions in Users.
- **User experience:** error messages should appear in real time and in the correct action context.
- **Consistency:** Dashboard actions should match History records.

## 4) Representative Test Cases (No Detailed Steps)

The following test cases are intentionally representative and not exhaustive.

| TC ID | Tab | Test Case | Priority | Severity |
| --- | --- | --- | --- | --- |
| TC-01 | Dashboard | Start a parking session with valid license plate, slot, and image data | High | Critical |
| TC-02 | Dashboard | End an active parking session and verify successful completion feedback | High | Critical |
| TC-03 | Dashboard | Prevent assigning a second active vehicle to an already occupied slot | High | Critical |
| TC-04 | Dashboard | Reject invalid slot input (letters, symbols, and unrealistic long values) | High | Major |
| TC-05 | Dashboard | Validate vehicle type options include required real-world categories | Medium | Major |
| TC-06 | History | Show only valid and relevant parking history records per expected visibility rules | Medium | Major |
| TC-07 | History | Support practical search and filtering (date, time, user, slot, plate) | Medium | Major |
| TC-08 | Users | Enforce username and password policy when creating users | Medium | Major |

## 5) Significant Bugs Identified (Top 8)

### BUG-01 - Missing vehicle type options
- **Tab:** Dashboard
- **Severity:** Major
- **Business impact:** Parking pricing and rules may be incorrect because only one generic vehicle type is available.
- **Observed behavior:** The system provides only a single vehicle type option (standard).
- **Expected behavior:** The system should support multiple relevant vehicle types (for example private car, motorcycle, bus, truck/heavy vehicle), according to business rules.

### BUG-02 - Invalid slot input is accepted
- **Tab:** Dashboard
- **Severity:** Critical
- **Business impact:** Invalid slot data can break parking management accuracy and operational trust.
- **Observed behavior:** Slot accepts letters, symbols, and very long non-realistic values.
- **Expected behavior:** Slot should accept only valid format and range based on defined parking slot rules.

### BUG-03 - Two vehicles can be assigned to the same slot
- **Tab:** Dashboard
- **Severity:** Critical
- **Business impact:** Allows conflicting active parking assignments and causes billing/operational errors.
- **Observed behavior:** A second vehicle can be parked in a slot that was already used, without proper occupancy validation.
- **Expected behavior:** The system should block new assignment when the slot is occupied and allow assignment only after it is available.

### BUG-04 - End parking shows error even when operation succeeds
- **Tab:** Dashboard
- **Severity:** Major
- **Business impact:** Misleading feedback reduces user confidence and may cause repeated actions.
- **Observed behavior:** User receives an error message when ending parking, but the session is actually closed and visible in History.
- **Expected behavior:** System should display a success message when parking ends successfully.

### BUG-05 - Non-image files accepted as vehicle image
- **Tab:** Dashboard
- **Severity:** Major
- **Business impact:** Poor data quality and potential misuse of upload field.
- **Observed behavior:** Upload accepts files that are not image types (for example PDF).
- **Expected behavior:** Upload should enforce valid image MIME types and reject unsupported files.

### BUG-06 - History exposes questionable and invalid records
- **Tab:** History
- **Severity:** Major
- **Business impact:** Data integrity and privacy concerns; users may see records with invalid plate formats and poor media quality.
- **Observed behavior:** History includes records with invalid plate lengths/formats and entries with missing or irrelevant images.
- **Expected behavior:** History should display only valid, relevant records that meet data validation standards.

### BUG-07 - Missing History search and filtering capabilities
- **Tab:** History
- **Severity:** Major
- **Business impact:** Hard to audit and investigate parking activity efficiently.
- **Observed behavior:** No search/filter options by date, time, user, slot, or plate.
- **Expected behavior:** History should provide practical filtering/search to support operational and support workflows.

### BUG-08 - User creation lacks credential policy enforcement
- **Tab:** Users
- **Severity:** Major
- **Business impact:** Weak account security and inconsistent user data quality.
- **Observed behavior:** Usernames and passwords can be created without policy constraints.
- **Expected behavior:** System should enforce clear username/password policy (length, character requirements, and invalid pattern blocking).

## 6) Summary

My testing focused on the highest-value business flow first (Dashboard), then checked data traceability (History), and then user management controls (Users). This approach exposed critical functional and data-quality risks that should be prioritized before expanding test coverage.
