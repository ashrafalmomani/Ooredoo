# -*- coding: utf-8 -*-

from odoo import api, models, modules, fields, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    state = fields.Selection([('active', 'Active'), ('inactive', 'Inactive'), ('expired', 'Expired')],
                             default='active', string='Status')
    eligible_for_commission = fields.Boolean('Eligible for Commission')
    availability_date = fields.Date('Availability Date')
    expiration_date = fields.Date('Expiration Date')
    product_department_id = fields.Many2one('product.department', 'Department')


class Warehouse(models.Model):
    _inherit = "stock.warehouse"

    @api.multi
    def act_warehouse_location(self):
        view_location_id = self.view_location_id.id
        location_ids = self.env['stock.location'].search([('location_id', '=', view_location_id)]).ids
        form_view_ref = self.env.ref('stock.view_location_form', False)
        tree_view_ref = self.env.ref('stock.view_location_tree2', False)
        return {
            'name': _('Locations'),
            'view_mode': 'tree, form',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'stock.location',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': "[('id', 'in', %s)]" % location_ids,
            'views': [(tree_view_ref and tree_view_ref.id or False, 'tree'),
                      (form_view_ref and form_view_ref.id or False, 'form')],
            'context': {}
        }


class ProductDepartment(models.Model):
    _name = 'product.department'
    _description = 'Product.department'
    _rec_name = 'name'

    name = fields.Char('Name')
