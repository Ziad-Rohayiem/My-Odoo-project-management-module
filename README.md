# Odoo Project Management Module

This is a custom-built project management module for the Odoo ERP platform. It provides a straightforward system for managing projects, tasks, and stages from within Odoo.

## Features

- **Project Management:** Create and manage projects, assigning project managers and tracking start and end dates.
- **Task Management:** Organize tasks within projects, assign them to users, and set priorities and deadlines.
- **Customizable Stages:** Define unique stages for task workflows (e.g., To Do, In Progress, Review, Done).
- **Kanban View:** Visualize task progress in a Kanban-style board, with tasks grouped by stage.
- **Progress Tracking:** Task progress is automatically updated based on its stage.
- **Deadline Reminders:** Automatically schedules a "Deadline Reminder" activity for tasks with a set deadline.
- **Chatter Integration:** Tracks changes and facilitates communication on projects and tasks through Odoo's chatter feature.
- **Access Control:** Permissions are configured to control which users can create, view, edit, or delete projects and tasks.

## Models

The module is built around three core models:

- **Project (`project.management`):** The main container for tasks. Each project has a name, description, project manager, and related tasks.
- **Stage (`project.task.stage`):** Represents a single stage in the task workflow. Stages are sortable and can be designated as a "folded" or "done" state in the Kanban view.
- **Task (`project.task.management`):** The individual work items that belong to a project. Each task has a description, assigned user, priority, and is associated with a specific stage.

## Installation

1.  Ensure you have a running Odoo instance.
2.  Clone or download this module.
3.  Place the `project_management` directory into your Odoo `addons` path.
4.  Restart the Odoo server.
5.  Navigate to **Apps** in your Odoo instance.
6.  Click on **Update Apps List**.
7.  Search for "Project Management" and click **Install**.

## Usage

After installation, the "Project Management" menu will be available in your Odoo dashboard.

- **Create a Project:** Navigate to `Project Management > Projects` and click "Create". Fill in the project details and assign a Project Manager.
- **Define Stages:** Go to `Project Management > Configuration > Stages` to create or modify the stages for your task workflows.
- **Create Tasks:** Open a project and go to the "Tasks" tab to create new tasks. Assign them to users, set deadlines, and place them in the appropriate stage.
- **Update Task Status:** Drag and drop tasks between stages in the Kanban view to update their status.

---

*Author: Ziad Rohayiem*
