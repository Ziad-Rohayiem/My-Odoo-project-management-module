from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class Task(models.Model):
    _name = 'project.task.management'
    _description = 'Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'priority desc, sequence, id desc'

    name = fields.Char(string='Task Name', required=True, tracking=True)
    description = fields.Html(string='Description')
    project_id = fields.Many2one('project.management', string='Project', required=True, ondelete='cascade')
    stage_id = fields.Many2one('project.task.stage', string='Stage',
                              default=lambda self: self.env['project.task.stage'].search([], limit=1),
                              group_expand='_read_group_stage_ids', tracking=True)
    user_id = fields.Many2one('res.users', string='Assigned To', default=lambda self: self.env.user, tracking=True)
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Very High'),
    ], default='1', string='Priority')
    sequence = fields.Integer(string='Sequence', default=10)
    
    # Date fields
    date_start = fields.Datetime(string='Start Date')
    date_deadline = fields.Date(string='Deadline', tracking=True)
    date_completed = fields.Datetime(string='Completion Date', readonly=True, tracking=True)
    
    # Status fields
    is_done = fields.Boolean(string='Done', compute='_compute_is_done', store=True)
    active = fields.Boolean(default=True)
    
    # Progress
    progress = fields.Float(string='Progress', compute='_compute_progress', store=True)

    @api.depends('stage_id')
    def _compute_progress(self):
        for task in self:
            stage = task.stage_id
            if stage and stage.is_done:
                task.progress = 100.0
            elif stage and stage.name == "Review":
                task.progress = 80.0
            elif stage and stage.name == "In Progress":
                task.progress = 50.0
            else:
                task.progress = 0.0

    @api.depends('stage_id', 'stage_id.is_done')
    def _compute_is_done(self):
        for task in self:
            task.is_done = task.stage_id.is_done if task.stage_id else False

    #####################################################################
    # This method overrides the default create method to add a deadline reminder activity
    @api.model
    def create(self, vals):
        task = super(Task, self).create(vals) # This is the default create method

        # Auto-schedule activity reminder if deadline and assigned user exist
        deadline = vals.get('date_deadline')
        user = vals.get('user_id')
        if deadline and user:
            task.activity_schedule(
                'mail.mail_activity_data_todo',
                user_id=int(user),  # user_id comes as string in vals
                date_deadline=deadline,
                summary='Deadline Reminder',
                note='Please complete this task before the deadline.'
            )

        return task
    ######################################################################

    @api.model
    def _read_group_stage_ids(self, stages, order):
        """Enable group_by on stage_id in kanban view"""
        return stages.search([], order=order)

    def action_mark_as_done(self):
        """Mark task as done and record completion date"""
        for task in self:
            # Find the 'Done' stage
            done_stage = self.env['project.task.stage'].search([('is_done', '=', True)], limit=1)
            
            if done_stage:
                # Update task
                task.write({
                    'stage_id': done_stage.id,
                    'date_completed': fields.Datetime.now(),
                    # 'progress': 100.0
                })
                
                # Log message in chatter (BONUS FEATURE!)
                task.message_post(
                    body=f"✅ Task marked as completed on {fields.Datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                    subject="Task Completed",
                    message_type='notification',
                )
                
                # Log to console for demo (BONUS FEATURE!)
                _logger.info(
                    "✅ Task '%s' (ID: %s) marked as DONE by user '%s' at %s",
                    task.name,
                    task.id,
                    self.env.user.name,
                    fields.Datetime.now()
                )
        
        return True
