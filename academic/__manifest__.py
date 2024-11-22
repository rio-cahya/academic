# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2017 vitraining.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


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
        "security/group.xml",        
        "security/ir.model.access.csv",
        "wizard/create_attendee.xml",
        ],
    "installable": True,
    "application": True,
    "auto_install": False,
}