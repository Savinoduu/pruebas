# -*- coding: utf-8 -*-

from odoo import models, fields


class CamposOpticaAccount(models.Model):
    _inherit = 'account.move'
    _name = 'account.move'
    Campo_Laboratorio_Account = fields.Many2one(comodel_name='res.partner',string="Laboratorio",required=False, ondelete='cascade',compute="Buscador")
    Campo_Paciente_Account = fields.Many2one(comodel_name='res.partner',string="Paciente",required=False, ondelete='cascade',compute="Buscador")
    Campo_Albaran_Account = fields.Char(string="Albaran",compute="Buscador")

    def Buscador(self):
        self.Campo_Laboratorio_Account = False
        self.Campo_Paciente_Account = False
        self.Campo_Albaran_Account = False
        sale_order =self.env['sale.order'].search([('name', '=', self.invoice_origin)])
        if not sale_order: return
        self.Campo_Laboratorio_Account = sale_order.Campo_Laboratorio_Sale
        self.Campo_Paciente_Account = sale_order.Campo_Paciente_Sale
        self.Campo_Albaran_Account = sale_order.Campo_Albaran_Sale




