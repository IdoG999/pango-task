# Part 3 - Reflection

## Overall approach and key decisions

I started by installing Docker and running the application locally. I explored the system manually and documented bugs during exploration. I then organized the assignment in a dedicated local project folder and created a public GitHub repository for submission.

From a QA perspective, I made an early priority decision to focus on the Dashboard because it contains the core parking flow and has the highest business impact. After that, I expanded coverage to History and Users.

Once the exploratory findings were clear, I converted them into structured deliverables:
- a prioritized manual test plan
- representative test cases
- automation scenarios tied to the most critical risks

## Trade-offs I made and why

I chose depth over breadth. Instead of trying to automate many scenarios, I focused on high-value flows that directly affect data integrity and user trust. This gave better value for the assignment timeline and produced clearer, more maintainable tests.

I also accepted that not every issue could be automated in this phase. Some findings were better documented first in the manual test plan and left for future automation iterations.

## AI tools and technologies I used

I used Cursor as my primary AI development assistant and worked with Python, Pytest, and Playwright for automation.

I selected this stack because:
- I am experienced with Cursor and use it regularly
- Python + Pytest is fast to develop and easy to maintain
- Playwright is reliable for browser automation
- the Page Object structure keeps selectors and test logic clean

## Reasoning behind tool choices, benefits, and limitations

Cursor helped me move faster in several areas:
- repository scaffolding and file organization
- improving writing quality in markdown deliverables
- refactoring tests into a cleaner structure (pages, fixtures, test data)
- tightening assertions and improving readability

At the same time, I did not rely on AI output blindly. I validated behavior by running tests locally and manually reviewing flows in the browser. This was important because generated selectors and assumptions can be inaccurate without runtime verification.

The main limitation was that AI suggestions sometimes required adjustment to match the real UI behavior. Human QA judgment was still necessary for prioritization, expected outcomes, and final quality decisions.
