from odoo import api, fields, models, _

class Attendee(models.Model):
    _name = "academic.attendee"

    name                = fields.Char(string="Name", required=True,)
    session_id          = fields.Many2one("academic.session", string="Session", )
    partner_id          = fields.Many2one("res.partner", string="Partner", )
    course_id           = fields.Many2one("academic.course", string="Course", related="session_id.course_id", store=True)

    @api.onchange('partner_id')
    def onchange_partner(self):
        self.name = self.partner_id.id

    _sql_constraints = [
        ('partner_session_unique','UNIQUE(session_id,partner_id)','Multiple atendee detected')
    ]
