# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Training(models.Model):
    _name = 'training'

    name = fields.Char()
    description = fields.Text()
    partner_id = fields.Many2one('res.partner', string='Partner')
    user_ids = fields.Many2many('res.users', string='Users')

    @api.multi
    def set_description(self):
        for train in self:
            description = str(self.name)
            for user in self.user_ids:
                description += " " + str(user.name)
            train.description = description

