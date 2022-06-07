# -*- coding: utf-8 -*-
{
    'name': "campos_optica",

    'summary': """
        Este modulo se encargara de agregar campos extras en empresas que sean de optica en el from de 
        Sale, Account, Tree y Stock
        """,

    'description': """
        Este modulo se encargara de agregar campos extras en empresas que sean de optica en el from de 
        Sale, Account, Tree y Stock
        """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','stock','account'],

    # always loaded
    'data': [
        "views/sale_views.xml",
        "views/sale_views_tree.xml",
        "views/account_move_views.xml",
        "views/stock_picking_views.xml",

    ],
}
