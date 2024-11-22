from odoo import models, fields, api, _

class CreateAttendeeWizard(models.TransientModel):
    _name = 'academic.create.attendee.wizard'

    session_id = fields.Many2one('academic.session', string='Session',)
    session_ids = fields.Many2many('academic.session', string='Session',)
    partner_ids = fields.Many2many('res.partner', string='Partners to add to session', required=True)

    def action_add_attendee(self):
        self.ensure_one()
        for ses in self.session_ids:
            ses.attendee_ids = [(0,0,{'partner_id': p.id}) for p in self.partner_ids]
        #one2many
        #self.session_id.attendee_ids = [(0,0,{'partner_id': p.id}) for p in self.partner_ids]
        return {'type':'ir.actions.act_window_close'}

