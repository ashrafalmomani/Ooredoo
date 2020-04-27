# -*- coding: utf-8 -*-

from odoo import api, models, modules, fields, _
from datetime import date

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    purchaser_id = fields.Many2one('res.partner', string='Purchaser', required=True, default=lambda self: self.env.user.partner_id, change_default=True, track_visibility='always')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def partner_domain(self):
        partner_ids = []
        partner = self.env.user.partner_id
        if partner.partner_type == 'distributor':
            distributor_type = partner.distributor_type
            if distributor_type in ('preferred', 'sub'):
                partner_ids = self.env['res.partner'].search([('distributor_id', '=', partner.id)]).ids
            else:
                partner_ids = self.env['res.partner'].search([('main_partner_id', '=', partner.id)]).ids

        elif partner.partner_type == 'salesperson':
            salesperson_type = partner.salesperson_type
            if salesperson_type == 'dsr':
                partner_ids = self.env['res.partner'].search([('distributor_id', '=', partner.id)]).ids
            else:
                partner_ids = self.env['res.partner'].search([('main_partner_id', '=', partner.id)]).ids

        return [('id', 'in', partner_ids)]

    ooredoo_salesman_id = fields.Many2one('res.partner', string='Sales Person', change_default=True, track_visibility='always', default=lambda self: self.env.user.partner_id)
    partner_id = fields.Many2one('res.partner', string='Customer', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, domain=partner_domain, required=True, change_default=True, index=True, track_visibility='always', track_sequence=1)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.multi
    def product_domain(self):
        products_ids = []
        region_id = self.env.user.partner_id.region_id
        if region_id:
            products_ids = self.env['ooredoo.price.list'].search([('region_id', '=', region_id.id)]).ids
        return [('id', 'in', products_ids)]

    product_id = fields.Many2one('product.product', string='Product', domain=product_domain, change_default=True, ondelete='restrict')

    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()

        salesman = self.env.user.partner_id
        order_partner_id = self.order_partner_id
        if salesman.partner_type == 'distributor' and order_partner_id.partner_type == 'distributor':
            popl_id = self.env['ooredoo.price.list'].search([('product_id', '=', self.product_id.id),
                                                             ('region_id', '', order_partner_id.region_id.id),
                                                             ('start_date', '<=', date.today()),
                                                             ('end_date', '>=', date.today()),
                                                             ('price_type', '>=', 'pdp')], limit=1)
            if popl_id:
                self.price_unit = popl_id.price
            else:
                opl_id = self.env['ooredoo.price.list'].search([('product_id', '=', self.product_id.id),
                                                                ('region_id', '', order_partner_id.region_id.id),
                                                                ('price_type', '>=', 'pd')], limit=1)
                self.price_unit = opl_id.price

        elif salesman.partner_type == 'distributor' and order_partner_id.partner_type == 'dealer':
            popld_id = self.env['ooredoo.price.list'].search([('product_id', '=', self.product_id.id),
                                                             ('region_id', '', order_partner_id.region_id.id),
                                                             ('start_date', '<=', date.today()),
                                                             ('end_date', '>=', date.today()),
                                                             ('price_type', '>=', 'dealerp')], limit=1)
            if popld_id:
                self.price_unit = popld_id.price
            else:
                opld_id = self.env['ooredoo.price.list'].search([('product_id', '=', self.product_id.id),
                                                                 ('region_id', '', order_partner_id.region_id.id),
                                                                 ('price_type', '>=', 'dealer')], limit=1)
                self.price_unit = opld_id.price
