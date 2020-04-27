# -*- coding: utf-8 -*-

from odoo import api, models, modules, fields


class OoredooPriceList(models.Model):
    _name = 'ooredoo.price.list'
    _description = 'Ooredoo Price List'
    _rec_name = 'product_id'

    product_id = fields.Many2one('product.product', 'Product')
    region_id = fields.Many2one('res.region', 'Region')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    price = fields.Float('Price')
    price_type = fields.Selection([('pd', 'PD Price'), ('dealer', 'Price to Dealer'), ('retail', 'Retail Price'),
                                   ('pdp', 'PD Promotional Price'), ('dealerp', 'Retail Promotional Price')],
                                  default='pd', string='Price Type')
