## Reflection

### Challenges in Agile Development Management
- **Template Selection**: Choosing the right template for Agile development required careful evaluation. The goal was to ensure efficient task tracking, sprint planning, and workflow visualization.
- **Customization**: Balancing simplicity with necessary features was crucial. Essential functionalities like user roles, task dependencies, and workflow automation needed to be incorporated.
- **Integration with Issues**: Planning was necessary to ensure a seamless connection between Kanban tasks and GitHub Issues. The integration should support real-time updates, maintain data consistency, and minimize manual effort.

After selecting the Kanban template, the Automated Kanban template was not available by default due to GitHub's recent update to its Projects system. Instead, GitHub now provides a more flexible custom board setup, requiring manual setup of automated Kanban workflows.

### Steps to Automate Task Movements using GitHub Actions
#### Install GitHub Command Line
- Since the workflow uses GitHub CLI (`gh project item update`), the `gh` CLI must be installed on my machine.

#### Authenticate GitHub CLI with a Personal Access Token (PAT)
- Since GitHub Actions runs in a CI/CD environment, it needs a GitHub Token with proper permissions.

#### Generate a Personal Access Token (PAT)
- Used for Continuous Integration/Deployment and pipelines to authenticate and perform automated deployments.

### Comparison of GitHub Projects, Trello, and Jira
| Feature            | GitHub Projects | Trello | Jira |
|-------------------|---------------|--------|------|
| **Agile Support** | Yes, supports Kanban and customizable workflows | Basic Agile support via Kanban boards | Advanced support for Scrum, Kanban, and SAFe |
| **Automation** | Built-in automation via GitHub Actions and project rules | Limited (Power-Ups required for automation) | Extensive automation with customizable rules and integrations |
| **Issue Tracking** | Fully integrated with GitHub Issues | Separate (requires third-party tools for issue tracking) | Advanced issue tracking with backlog management, sprints, and reporting |
| **Customization** | Moderate (Limited board customization, but flexible labels and fields) | Highly customizable (Power-Ups, labels, workflows) | Highly customizable (Custom workflows, reports, dashboards) |
| **Collaboration** | Best for Dev Teams (Direct GitHub repo integration) | Great for General Teams (Easy to use, integrates with many apps) | Best for Large Teams (Comprehensive collaboration features) |
| **Best For** | Developers & GitHub Users managing code-related tasks | Small teams & simple task management | Large organizations with structured Agile workflows |
| **Cost** | Free for basic use (Paid plans available) | Free for individuals (Paid features via Power-Ups) | Paid (Limited free plan, full features require subscription) |
