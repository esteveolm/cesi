# -*- coding: utf-8 -*-
{
    'name': "cesi",

    'summary': """
        Odoo main module for CESI capestudiantsenseinternet.org""",

    'description': """
        This module contains all customizations for the project
    """,

    'author': "Esteve Olm",
    'website': "https://capestudiantsenseinternet.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','base_geoengine','sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}