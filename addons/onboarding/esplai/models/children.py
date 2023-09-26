from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class EsplaiChild(models.Model):
    _name = "esplai.child"
    _description = "Database of all the children"

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    birthdate = fields.Date(string="Birthdate", required=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ], string="Gender")
    attention= fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string="Need of special attention")
    schoolcourse = fields.Char(string='Course', compute='_compute_course', store=True)
    on_waiting_list = fields.Boolean(string='On Waiting List', compute='_compute_waiting_list')

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                current_year = fields.Date.today().year
                birth_year = record.birthdate.year
                record.age = current_year - birth_year

    @api.depends('age')
    def _compute_course(self):
        for record in self:
            if record.age==6 or record.age==7:
                current_curse = 'Little'
                record.schoolcourse = current_curse
            if record.age==8 or record.age==9:
                current_curse = 'Lil-Medium'
                record.schoolcourse = current_curse
            if record.age==10 or record.age==11:
                current_curse = 'Medium'
                record.schoolcourse = current_curse
            if record.age==12 or record.age==14:
                current_curse = 'Big'
                record.schoolcourse = current_curse
            if record.age==15 or record.age==18:
                current_curse = 'Young'
                record.schoolcourse = current_curse

    # Create a method to update the waiting list status
    @api.depends('schoolcourse')
    def _compute_waiting_list(self):
        threshold = 21

        for record in self:
            if record.schoolcourse:
                course_count = self.search_count([('schoolcourse', '=', record.schoolcourse)])
                record.on_waiting_list = course_count > threshold

    @api.constrains('age')
    def _check_child_age(self):
        for rec in self:
            if rec.age > 18:
                raise ValidationError(_("Child must be between 6 and 18 years old"))

