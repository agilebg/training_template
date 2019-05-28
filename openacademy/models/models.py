# -*- coding: utf-8 -*-

from odoo import models, fields, api


class openacademy(models.Model):
    _name = 'openacademy.openacademy'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null',
                                     string="Responsible", index=True)

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100


class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('product.template',
                                ondelete='cascade',
                                string="Course", required=True)


class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()
    biography = fields.Html()
    course_ids = fields.One2many('product.template',
                                 'teacher_id',
                                 string="Courses")


class Courses(models.Model):
    _inherit = 'product.template'

    teacher_id = fields.Many2one('academy.teachers', string="Teacher")


class Invoice(models.Model):
    _inherit = 'account.invoice.line'

    name2 = fields.Char(string='Campo di prova')
