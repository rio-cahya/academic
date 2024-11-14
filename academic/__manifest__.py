# -*- coding: utf-8 -*-

{
    "name": "Academic Information System v1.0",
    "version": "1.0",
    "author": "Rio",
    "category": "Education",
    "website": "www.riocahya.com",
    "description": """
    Modul Pengelolaan Academik
   
""",
    "depends": ["base"],
    "data":[
        "views/menu.xml",
        "views/course.xml",
        "views/session.xml",
        "views/attendee.xml",
        "views/partner.xml",
        "security/ir.model.access.csv",
        ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
