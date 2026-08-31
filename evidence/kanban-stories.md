# Kanban stories and screenshot plan

Create columns New Issues, Ice Box, Product Backlog, Sprint Backlog, In Progress, Review, Done. Every card should visibly show its title, estimate, sprint, and applicable `enhancement` or `technical debt` label.

## Sprint 1

| Story | Label | Points |
|---|---|---:|
| Setting up the development environment | technical debt | 3 |
| Read an account from the service | enhancement | 3 |
| List all accounts in the service | enhancement | 3 |
| Update an account in the service | enhancement | 5 |
| Delete an account from the service | enhancement | 3 |
| Create an account in the service | enhancement | 5 |

Add “Improve API error messages” (enhancement, 2) to New Issues, “Add account search” (enhancement, 5) to Ice Box, and “Document API examples” (technical debt, 2) to Product Backlog. Task 3 shows populated user stories; Task 4 the ordered Product Backlog; Task 5 visible labels; Task 6 the whole board. Task 8 shows environment setup in Done. Tasks 9–12 show their matching REST stories in Done.

## Sprint 2

- Need the ability to automate continuous integration checks — technical debt, 5.
- Need automated test coverage reporting — enhancement, 3.

Task 18 (`sprint2-plan.png`) shows both in Sprint Backlog. Task 20 shows both in Done after the real CI build.

## Sprint 3

- Need to add security headers and CORS policies — enhancement, 3.
- Containerize your microservice using Docker — technical debt, 5.
- Deploy your Docker image to Kubernetes — enhancement, 5.
- Create a CD pipeline to automate deployment to Kubernetes — technical debt, 5.

Task 25 shows the first three in Sprint Backlog. Tasks 24, 27, 28, and 33 show respectively the security, Docker, Kubernetes, and CD story in Done; capture only after each outcome is verified.
