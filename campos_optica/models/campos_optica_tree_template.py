# -*- coding: utf-8 -*-
import logging

from odoo import models, fields


class CamposOpticaTreeTemplate(models.Model):
    _inherit = 'sale.order', 'account.move'

    Campo_Laboratorio_Tree = fields.Many2one(comodel_name='res.partner',string="Laboratorio",required=False, ondelete='cascade')
    Campo_Paciente_Tree = fields.Many2one(comodel_name='res.partner',string="Paciente",required=False, ondelete='cascade')
    Campo_Albaran_Tree = fields.Char(string="Albaran")