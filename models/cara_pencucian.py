# -*- coding: utf-8 -*-
 
from odoo import models, fields, api
 
class bintangcarwash(models.Model):
    # ini akan berbentuk tabel nanti
    _name = 'bintangcarwash.caracuci'
    _description = 'Daftar Teknik Pencucian'
    
    # ini merupakan field yang dibutuhkan untuk suatu record
    name = fields.Selection(string='Nama Teknik', selection=[('sprinkle','Sprinkle'),('normal','Normal'),('water jet','Water Jet'),('super wash','Super Wash')])
    air = fields.Selection(string='Jenis Air',
                            selection=[('hot water', 'Hot Water'), ('cold water', 'Cold Water'), ('normal water', 'Normal Water'), ('special water', 'Special Water')],
                            required=True
    )
    
    kotoran =  fields.Selection(string='Tipe Kotoran',
                            selection=[('ringan', 'Ringan'), ('sedang', 'Sedang'), ('berat', 'Berat')],
                            required=True
    )
    
    tersedia = fields.Boolean(string='tersedia',
                             default=True
    )
    
    deskripsi = fields.Char(string='deskripsi',
                            help='isi dengan alat yang digunakan untuk mencuci')
    models_id = fields.One2many(string="jenis_bahan_cucian", inverse_name='teknik_id',comodel_name='bintangcarwash.jeniscucian')