from odoo import api, fields, models, _

class kota(models.Model):
    _name = "vit.kota"
    
    name = fields.Char(string="Name",)
    state_id = fields.Many2one("res.country.state", string="State")

