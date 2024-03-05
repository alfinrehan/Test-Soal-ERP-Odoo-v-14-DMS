# -*- coding: utf-8 -*-

from odoo import models, fields, api


class data_product(models.Model):
    _name = 'data.product'
    _description = 'Data Product'

    name = fields.Char(string="Product Name", required=True) 
    price = fields.Float(string="Price", required=True) 
    description = fields.Text(string="Description")
    qty_available = fields.Float(string="Quantity On Hand")