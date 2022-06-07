# -*- coding: utf-8 -*-

from odoo import models, fields


class CamposOpticaTemplate(models.Model):
    _inherit = 'sale.order'
    Campo_Laboratorio_Sale = fields.Many2one( comodel_name='res.partner', string="Laboratorio", required=True, ondelete='cascade',                                store=True)
    Campo_Paciente_Sale = fields.Many2one(comodel_name='res.partner', string="Paciente", required=True, ondelete='cascade')
    Campo_Albaran_Sale = fields.Char(string="Albaran")



