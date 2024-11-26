from odoo import api, fields, models, _

class Course(models.Model):
    _name = "academic.course"
    
    name                = fields.Char(string="name",)
    description         = fields.Text(string="Description", required=True,)
    responsible_id      = fields.Many2one("res.users", string="Responsible",)
    session_ids         = fields.One2many("academic.session", string="Sessions", inverse_name="course_id", ondelete="cascade")
    
    _sql_constraints = [
        ('check_name_unique','UNIQUE(name)','Field name harus unik'),
        ('check_name_desc','CHECK(name <> description)','name dan description tidak boleh sama')
    ]
    
