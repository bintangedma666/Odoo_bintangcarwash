# -*- coding: utf-8 -*-
 
from odoo import models, fields, api
 
class OrderCuci(models.Model):
    # ini akan berbentuk tabel nanti
    _name = 'bintangcarwash.ordercucian'
    _description = 'Daftar Order Cucian'
   
    tanggal_pesan = fields.Datetime(string='Tanggal Pesanan', default=fields.Datetime.now)
    detailcucian_ids = fields.One2many('bintangcarwash.detailpesanan', 'order_id', string='Detail Order')
    jumlah_pesanan = fields.Integer(compute='_compute_jumlah_pesanan', string='Jumlah Pesanan')
    total_harga = fields.Char(compute='_compute_total_harga', string='Total Tagihan')

    @api.model
    def _compute_total_harga(self):
        # mapped = untuk mengambil satu atribut saja
        # self.env---.mapped = mengembalikan suatu list
        for record in self:
            total = sum(self.env['bintangcarwash.detailpesanan'].search([('order_id','=',record.id)]).mapped('jumlah_harga'))
            record.total_harga = total
   
    @api.depends('detailcucian_ids')
    def _compute_jumlah_pesanan(self):
        for record in self:
            record.jumlah_pesanan = len(record.detailcucian_ids)
 
class detailPesanan(models.Model):
    _name = 'bintangcarwash.detailpesanan'
    _description = 'Detail Pesanan Cuci'
 
    name = fields.Char(string='Kode Order')
    order_id = fields.Many2one('bintangcarwash.ordercucian', string='Order Cuci')
    models_id = fields.Many2one('bintangcarwash.jeniscucian', string='Bahan Cucian')
    harga = fields.Integer(compute='_compute_harga', string='Harga (per mobil)')
    jumlah = fields.Integer(string='Jumlah mobil')
    jumlah_harga = fields.Integer(compute='_compute_jumlah_harga', string='Jumlah Harga')
   
    @api.depends('jumlah')
    def _compute_jumlah_harga(self):
        for record in self:
            record.jumlah_harga = record.harga * record.jumlah
   
    @api.depends('models_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.models_id.harga
