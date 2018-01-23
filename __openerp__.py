# -*- coding: utf-8 -*-
{
    'name': "Removes tax info from pos receipts",
    'author': "QArea, Yury Stasovsky",
    'license': 'LGPL-3',
    'website' : "https://qarea.us",
    'category': 'Custom integration',
    'version': '1.0.0',

    'depends': ['base', 'point_of_sale'],

    'qweb': ['static/src/xml/custom_rcpt.xml'],
    'installable': True,
}
