from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import time

class Session(models.Model):
    _name = "academic.session"
    
    name                = fields.Char(string="Name", required=True,)
    course_id           = fields.Many2one("academic.course", string="Course", required=True,)
    instructor_id       = fields.Many2one("res.partner", string="Instructor", required=True,)
    start_date          = fields.Date(string="Start Date", default=lambda self: time.strftime("%Y-%m-%d"))
    duration            = fields.Integer(string="Duration",)
    seats               = fields.Integer(string="Seats",)
    active              = fields.Boolean(string="Active", default=True,)
    attendee_ids        = fields.One2many("academic.attendee", string="Attendee", inverse_name="session_id", )
    taken_seats         = fields.Float(string="Taken Seats", compute="_calc_taken_seats")
    image_small         = fields.Binary("Image Small")
    state               = fields.Selection(string="State",
                                        selection=[
                                        ('draft','Draft'),
                                        ('open','Open'),
                                        ('done','Done'),
                                        ],
                                        required=True,
                                        readonly=True,
                                        default='draft')

    def action_draft(self):
        self.state = 'draft'

    def action_open(self):
        self.state = 'open'

    def action_done(self):
        self.state = 'done'

    def _calc_taken_seats(self):
        for rec in self:
            if rec.seats > 0:
                rec.taken_seats = 100.0 * len(rec.attendee_ids) / rec.seats
            else:
                rec.taken_seats = 0.0

    @api.onchange('seats','attendee_ids')
    def onchange_seats(self):
        for rec in self:
            if rec.seats > 0:
                rec.taken_seats = 100.0 * len(rec.attendee_ids) / rec.seats
            else:
                rec.taken_seats = 0.0

    @api.constrains('instructor_id','attendee_ids')
    def _cek_instructor(self):
        for session in self:
            partner_ids = [ att.partner_id.id for att in session.attendee_ids]
            
            if session.instructor_id.id in partner_ids:
                raise ValidationError('Instructor tidak boleh sekalian menjadi peserta!')
            
    def copy(self, default=None):
        self.ensure_one()
        d = dict(default or {}, 
                 name=f"Copy of {self.name}"
                 )
        return super(session, self).copy(default=d)
