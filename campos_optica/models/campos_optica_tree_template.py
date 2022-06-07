# -*- coding: utf-8 -*-
import logging

from odoo import models, fields


class CamposOpticaTreeTemplate(models.Model):
    _inherit = 'sale.order'

    Campo_Laboratorio_Tree = fields.Many2one(comodel_name='res.partner',string="Laboratorio",required=True, ondelete='cascade', compute="Buscador")
    Campo_Paciente_Tree = fields.Many2one(comodel_name='res.partner',string="Paciente",required=True, ondelete='cascade')
    Campo_Albaran_Tree = fields.Char(string="Albaran")

    def Buscador(self):
        #sale_order = self.env['sale.order'].search[('id', '=', self.analytic_account_id)]
        #self.Campo_Laboratorio_Tree = sale_order.Campo_Laboratorio_Sale
        self.Campo_Laboratorio_Tree = self.env['sale.order'].browse(26).Campo_Laboratorio_Sale
