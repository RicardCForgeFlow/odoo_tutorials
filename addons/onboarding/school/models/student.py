from odoo import api, fields, models, _

class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "Database of all students"

    name = fields.Char(string='Name', required=True)
    surname = fields.Char(string='Surname', required=True)
    birthdate = fields.Date(string="Birthdate", required=True)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ], string="Gender")
    classroom = fields.Selection([
        ('classa', 'Class A'),
        ('classb', 'Class B'),
    ], string="Classroom", widget='selection')
    schoolcourse = fields.Char(string='Course', compute='_compute_course', store=True)


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
            if record.age <= 10:
                current_curse = 'Little'
                record.schoolcourse = current_curse
            if record.age > 10 and record.age < 30:
                current_curse = 'Medium'
                record.schoolcourse = current_curse
            if record.age >= 30:
                current_curse = 'Old'
                record.schoolcourse = current_curse

