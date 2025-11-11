{
    'name': 'Project Management',
    'version': '1.0',
    'category': 'Project',
    'summary': 'Custom Project and Task Management System',
    'description': """
        A simple project management module with:
        - Projects
        - Tasks with stages
        - Mark tasks as done
        - Completion date tracking
        - Automatic notifications
    """,
    'author': 'Ziad Rohayiem',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/stage_data.xml',
        'views/project_views.xml',
        'views/task_views.xml',
        'views/stage_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
