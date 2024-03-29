# -*- coding: utf-8 -*-
{
    'name': "stock_picking_quant",

    'summary': """分拣单显示批次库存信息""",

    'description': """
        分拣单显示批次库存信息
    """,

    'author': "kevinkong",
    'website': "http://mixoo.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock'],

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
    "application":True
}