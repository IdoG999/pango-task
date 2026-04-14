# Part 3 - Reflection

## Overall approach and key decisions

I started by installing Docker and running the application locally. I explored the system manually and documented bugs during exploration. I then organized the assignment in a dedicated local project folder and created a public GitHub repository for submission.

My working approach was to lead with my own QA knowledge and decision-making, and use AI as a force multiplier. I used my experience to define priorities, expected behavior, and risk areas, while AI helped me execute faster and keep the output structured.

From a QA perspective, I made an early priority decision to focus on the Dashboard because it contains the core parking flow and has the highest business impact. After that, I expanded coverage to History and Users.

Once the exploratory findings were clear, I converted them into structured deliverables:
- a prioritized manual test plan
- representative test cases
- automation scenarios tied to the most critical risks

## How I thought through the task

My main thinking process was risk-first and impact-first. I asked myself: "If this breaks in production, what hurts the user and the business the most?" That is why I started from Dashboard flows and not from less critical areas.

I balanced product behavior and test reliability. I did not just collect bugs; I grouped them by impact and by how realistic they are in daily usage. In parallel, I made sure the automated scenarios were meaningful, repeatable, and connected directly to the manual findings.

Another decision was to keep the scope focused. Instead of trying to automate everything, I chose a smaller set of high-value scenarios and implemented them cleanly, with clear structure and reusable components. For me, this is a stronger QA approach than writing many weak tests.

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

The key point is that AI improved speed and consistency, but my own knowledge drove the actual QA decisions. I chose what to test, how to prioritize, how to structure the automation, and how to validate outcomes.

At the same time, I never rely on AI output blindly. I always validate behavior by running tests locally and manually reviewing flows in the browser. This is important because generated selectors and assumptions can be inaccurate without runtime verification.

The main limitation is that AI suggestions sometimes need adjustments to match real UI behavior. Human QA judgment remains critical for prioritization, expected outcomes, and final quality decisions.
