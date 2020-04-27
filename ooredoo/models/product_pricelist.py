# -*- coding: utf-8 -*-

from odoo import api, models, modules, fields


class Pricelist(models.Model):
    _inherit = "product.pricelist"

    region_id = fields.Many2one('res.region', 'Region')
    price_type = fields.Selection([('pd', 'PD Price'), ('dealer', 'Price to Dealer'), ('retail', 'Retail Price'),
                                   ('pdp', 'PD Promotional Price'), ('dealerp', 'Retail Promotional Price')],
                                  default='pd', string='Price Type')

    @api.multi
    def create_ooredoo_price_list(self, region_id, price_type, item_ids):
        ooredoo_pricelist_obj = self.env['ooredoo.price.list']
        for item in item_ids:
            if item[2]['applied_on'] == '0_product_variant' and item[2]['compute_price'] == 'fixed':
                ooredoo_pricelist_obj.create({
                    'product_id': item[2]['product_id'],
                    'region_id': region_id,
                    'price_type': price_type,
                    'start_date': item[2]['date_start'],
                    'end_date': item[2]['date_end'],
                    'price': item[2]['fixed_price'],
                })

    @api.model
    def create(self, vals):
        if ('region_id' in vals and vals['region_id']) and ('price_type' in vals and vals['price_type']) and \
                ('item_ids' in vals and vals['item_ids']):
            self.create_ooredoo_price_list(vals['region_id'], vals['price_type'], vals['item_ids'])
        return super(Pricelist, self).create(vals)
