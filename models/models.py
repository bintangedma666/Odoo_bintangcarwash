# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ModelDasar(models.Model):
    _name = 'bintangcarwash.base'
    _description = 'model dasar Bintang carwash'
 
    ukuran = fields.Char(string="ukuran mobil", required=True)
    tipe = fields.Selection(string="tipe/jenis mobil", selection=[('convertible', 'Convertible'),
    ('coupe','Coupe'), ('hatchback','Hatchback'),('minivan','Minivan'),('suv','SUV'),('sedan','Sedan'),('wagon','Wagon')])


class bintangcarwash(models.Model):
    _name = 'bintangcarwash.jeniscucian'
    _description = 'Daftar jenis jenis pencucian'
    _inherit = "bintangcarwash.base"

    name = fields.Char(string='jenis Pencucian', required=True)
    harga = fields.Integer(string='Harga pencucian', required=True)
    active = fields.Boolean(default=True)
    teknik_id = fields.Many2one(comodel_name="bintangcarwash.caracuci", string='teknik pencucian',required=True, delegate=True )

    @api.constrains('name')
    def _constrains_name(self):
        for rec in self:
            duplicate = self.env['bintangcarwash.jeniscucian'].search([('name','=',rec.name)])
            if len(duplicate)>1:
                raise ValidationError("Bahan Cucian %s Sudah Ada di Daftar!! %s" % (str(rec.name).upper(),str(len(duplicate))))
 
    @api.onchange('tipe')
    def _onchange_tipe(self):
        # jika atribut 'tipe' berubah maka akan muncul suatu warning
        if self.tipe == 'katun':
            return {
                'warning': {
                    'title' : 'Teknik Cuci',
                    'message' : 'Teknik Cuci harus golongan B'
                }
            }
        elif self.tipe == 'polyester':
            return {
                'warning': {
                    'title' : 'Teknik Cuci',
                    'message' : 'Teknik Cuci harus golongan A'
                }
            }
