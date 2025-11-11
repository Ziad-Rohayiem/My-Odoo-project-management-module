from odoo import models, fields

class Stage(models.Model):
    _name = 'project.task.stage'
    _description = 'Task Stage'
    _order = 'sequence, name'

    name = fields.Char(string='Stage Name', required=True) #, translate=True
    description = fields.Text(string='Description')
    sequence = fields.Integer(string='Sequence', default=10)
    fold = fields.Boolean(string='Folded in Kanban',
                         help='This stage is folded in the kanban view when there are no records in that stage to display.')
    is_done = fields.Boolean(string='Is Done Stage',
                            help='Tasks in this stage are considered completed')
