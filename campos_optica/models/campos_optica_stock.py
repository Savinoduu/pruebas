# -*- coding: utf-8 -*-
import logging

from odoo import models, fields,api



class CamposOpticaStock(models.Model):
    _inherit = 'stock.picking'
    _name = "stock.picking"
    Campo_Laboratorio_Stock = fields.Many2one( comodel_name='res.partner',string="laboratorio",compute="Buscador")
    Campo_Paciente_Stock = fields.Many2one(comodel_name='res.partner', string="Paciente", required=False, ondelete='cascade',compute="Buscador")
    Campo_Albaran_Stock = fields.Char(string="Albaran", compute="Buscador")

    def Buscador(self):
        if not self.sale_id: return
        self.Campo_Laboratorio_Stock = self.sale_id.Campo_Laboratorio_Sale
        self.Campo_Paciente_Stock = self.sale_id.Campo_Paciente_Sale
        self.Campo_Albaran_Stock = self.sale_id.Campo_Albaran_Sale


