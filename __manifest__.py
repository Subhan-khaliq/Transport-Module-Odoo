{
    'name': 'Transport',
    'version': '15.0.1.0.0',
    'author': 'Subhan Khaliq, Bilal Khan and Asad Zaman',
    'website': 'http://www.edu.pk',
    'category': 'Campus Management System',
    'license': "AGPL-3",
    'Summary': 'A Module For Campus Management System',
    'images': ['static/description/icon.png'],
    'depends': ['base'],
    'data': ['security/campus_security.xml',
             'security/ir.model.access.csv',
             'wizard/wizard_report_4_view.xml',
             'wizard/wizard_report_3_view.xml',
             'wizard/wizard_report_2_view.xml',
             'wizard/wizard_report_1_view.xml',
             'report/report_1_view.xml',
             'report/report_2_view.xml',
             'report/report_3_view.xml',
             'report/report_4_view.xml',
             'report/report.xml',
             'views/cms_student_view.xml'],
    
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    #'post_init_hook': '_method_run_before_installation',
}
