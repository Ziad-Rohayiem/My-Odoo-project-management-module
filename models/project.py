from odoo import models, fields, api

class Project(models.Model):
    _name = 'project.management'
    _description = 'Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Project Name', required=True, tracking=True)
    description = fields.Text(string='Description')
    start_date = fields.Date(string='Start Date', default=fields.Date.today)
    end_date = fields.Date(string='End Date')
    user_id = fields.Many2one('res.users', string='Project Manager', default=lambda self: self.env.user)
    task_ids = fields.One2many('project.task.management', 'project_id', string='Tasks')
    task_count = fields.Integer(string='Task Count', compute='_compute_task_count')
    active = fields.Boolean(default=True)

    @api.depends('task_ids')
    def _compute_task_count(self):
        for project in self:
            project.task_count = len(project.task_ids)
