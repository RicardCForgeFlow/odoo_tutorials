from odoo import api, fields, models, _

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = 'mail.thread'
    _description = "Doctor Records"
    _rec_name = 'ref'

    name = fields.Char(string='Name', required = True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('others', 'Others')], string="Gender", tracking = True)
    ref = fields.Char(string="Reference", required=True)
    active = fields.Boolean(default=True)
    #nameref = fields.Char(string='Referencia amb nom', compute='_compute_nameref', store=True)

    def name_get(self):
        res = []
        for rec in self:
            name = f'{rec.ref} - {rec.name}'
            res.append((rec.id,name))
        return res

#    @api.depends('name')
#    def _compute_nameref(self):
#        for rec in self:
#            rec.nameref= rec.name + "-" + rec.ref
