{
    'name': "Employee Tracking",

    'summary': """
    Modulo dependiente de login webservice de tracking para xltrack""",

    'description': """
   Modulo dependiente de  login webservice de tracking para xltrack
    """,

    'author': "Nayeli Valencia Díaz",
    'website': "http://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': "19.0.1.0.0",

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
         'views/hr_employee.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}