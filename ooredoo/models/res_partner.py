# -*- coding: utf-8 -*-

from odoo import api, models, modules, fields, _


class Partner(models.Model):
    _inherit = 'res.partner'

    distributor_code = fields.Char('Distributor Code', track_visibility='always')
    shipping_method_id = fields.Many2one('shipping.method', 'Shipping Method', track_visibility='always')
    freight_terms_id = fields.Many2one('freight.terms', 'Freight Terms', track_visibility='always')
    fax = fields.Char('Fax', track_visibility='always')
    latitude = fields.Float('Latitude', track_visibility='always')
    longitude = fields.Float('Longitude', track_visibility='always')
    channel_type = fields.Many2one('channel.type', 'Channel Type', track_visibility='always')
    distributor_type_id = fields.Many2one('distributor.type', 'Distributor Type', track_visibility='always')
    distributor_class_id = fields.Many2one('distributor.class', 'Distributor Class', track_visibility='always')
    region_id = fields.Many2one('res.region', 'Region', track_visibility='always')
    wilaya_id = fields.Many2one('res.wilaya', 'Wilaya', track_visibility='always')
    assigned_territory_id = fields.Many2one('assigned.territory', 'Assigned territory', track_visibility='always')
    legal_id = fields.Many2one('legal.information', 'Legal Information', track_visibility='always')
    territory_ids = fields.Many2many('assigned.territory', 'territory_partner_rel', 'partner_id', 'territory_id',
                                     'Territory', track_visibility='always')
    applicable_taxes_type_id = fields.Many2one('applicable.taxes.type', 'Applicable Taxes Type', track_visibility='always')
    dealer_business_type_id = fields.Many2one('dealer.business.type', 'Business Type', track_visibility='always')
    dealer_account_type_id = fields.Many2one('dealer.account.type', 'Account Type', track_visibility='always')
    dealer_segment_id = fields.Many2one('dealer.segment', 'Segment', track_visibility='always')
    area_id = fields.Many2one('res.area', 'Area', track_visibility='always')
    area_type_id = fields.Many2one('area.type', 'Area Type', related='area_id.area_type_id', track_visibility='always')
    area_code = fields.Char('Area Code', track_visibility='always')
    area_manager_id = fields.Many2one('area.manager', 'Area Manager', related='area_id.area_manager_id', track_visibility='always')
    salesperson_supervisor_id = fields.Many2one('salesperson.supervisor', 'Supervisor', track_visibility='always')
    salesperson_id = fields.Many2one('res.partner', 'Salesperson', track_visibility='always')
    credit_limit = fields.Float('Credit Limit', track_visibility='always')
    dealer_ordering_code = fields.Char('Dealer Ordering Code', track_visibility='always')
    dealer_payment_code = fields.Char('Dealer Payment Code', track_visibility='always')
    bank_guarantee = fields.Float('Bank guarantee', track_visibility='always')
    appointment_date = fields.Date('Appointment Date', track_visibility='always')
    dealer_code = fields.Char('Dealer Code', track_visibility='always')
    partner_address_ids = fields.One2many('partner.address', 'partner_id', 'Partner Address', track_visibility='always')
    title = fields.Many2one('res.partner.title', 'Title', track_visibility='always')
    salesperson_position_id = fields.Many2one('salesperson.position', 'Position', track_visibility='always')
    salesperson_class_id = fields.Many2one('salesperson.class', 'Salesperson Class', track_visibility='always')
    employee_id = fields.Char('Employee ID', track_visibility='always')
    salesperson_code = fields.Char('Salesperson code', track_visibility='always')
    counter_salesman_id = fields.Char('Salesperson code', track_visibility='always')
    start_date = fields.Date('Start Date', track_visibility='always')
    end_date = fields.Date('End Date', track_visibility='always')
    prospect = fields.Boolean('Prospect', track_visibility='always')
    salesperson_type = fields.Selection([('dsm', 'DSM'), ('dsr', 'DSR')], string='Salesperson Type', track_visibility='always')
    main_partner_id = fields.Many2one('res.partner', 'Parent',track_visibility='always')
    distributor_id = fields.Many2one('res.partner', 'Distributor', track_visibility='always')
    distributor_child_ids = fields.One2many('res.partner', 'main_partner_id', string='Contacts', track_visibility='always',
                                            domain=[('partner_type', '=', 'salesperson'),
                                                    ('distributor_id', '=', False)])
    dealer_child_ids = fields.One2many('res.partner', 'dealer_id', string='Contacts', track_visibility='always',
                                       domain=[('partner_type', '=', 'dealer')])
    pp_sd_child_ids = fields.One2many('res.partner', 'distributor_id', string='Contacts', track_visibility='always',
                                      domain=[('partner_type', '=', 'salesperson')])
    territory_type_id = fields.Many2one('territory.type', 'Territory Type', track_visibility='always',
                                        related='assigned_territory_id.territory_type_id')
    contact_type = fields.Selection([('authorized', 'Authorized Contact'), ('alt', 'Alt Contact Person'),
                                     ('counter', '(DSM/DSR) Distributor Salesman')], string='Contact Type', track_visibility='always')
    dealer_contact_type = fields.Selection([('authorized', 'Authorized Contact'), ('alt', 'Alt Contact Person'),
                                            ('counter', 'Counter Salesman')], string='Contact Type', track_visibility='always')
    dealer_state = fields.Selection([('active', 'Active'), ('suspended', 'Suspended'), ('terminated', 'Terminated'),
                                     ('resigned', 'Resigned')], default='active', string='Status', track_visibility='always')
    state = fields.Selection([('active', 'Active'), ('inactive', 'Inactive'), ('available', 'Available'),
                              ('unavailable', 'Unavailable')], default='active', string='Status', track_visibility='always')
    partner_type = fields.Selection([('distributor', 'Distributor'), ('dealer', 'Dealer'),
                                     ('salesperson', 'Salesperson')], string='Partner Type', track_visibility='always')
    distributor_type = fields.Selection([('premium', 'PD Premium Distributor'), ('preferred', 'PP Preferred Partner'),
                                         ('sub', 'SD Sub-Distributor')], string='Distributor Type', track_visibility='always')
    allowed_products = fields.Selection([('all', 'All Products'), ('category', 'Category')],
                                        default='all', string='Allowed products', track_visibility='always')
    category_ids = fields.Many2many('product.category', 'partner_category_rel',
                                    'partner_id', 'categ_id', string="Categories", track_visibility='always')
    dsm_id = fields.Many2one('res.partner', 'DSM', domain="[('partner_type', '=', 'salesperson'), "
                                                          "('contact_type', '=', 'counter'), "
                                                          "('salesperson_type', '=', 'dsm'),"
                                                          "('distributor_type', '=', 'premium')]", track_visibility='always')
    dsr_id = fields.Many2one('res.partner', 'DSR', domain="[('partner_type', '=', 'salesperson'), "
                                                          "('contact_type', '=', 'counter'), "
                                                          "('salesperson_type', '=', 'dsr'),"
                                                          "('distributor_type', 'in', ('preferred', 'sub'))]", track_visibility='always')
    dealer_id = fields.Many2one('res.partner', 'Dealer', domain="[('partner_type', '=', 'dealer')]", track_visibility='always')

    @api.onchange('region_id')
    def onchange_region_id(self):
        if self.region_id:
            return {'domain': {'wilaya_id': [('region_id', '=', self.region_id.id)]}}
        else:
            return {'domain': {'wilaya_id': [('id', '=', [])]}}

    @api.onchange('wilaya_id')
    def onchange_wilaya_id(self):
        if self.wilaya_id:
            return {'domain': {'territory_ids': [('wilaya_id', '=', self.wilaya_id.id)]}}
        else:
            return {'domain': {'territory_ids': [('id', '=', [])]}}

    @api.onchange('main_partner_id')
    def onchange_main_partner_id(self):
        if self.partner_type == 'dealer':
            self.region_id = self.main_partner_id.region_id.id
            self.wilaya_id = self.main_partner_id.wilaya_id.id
            self.distributor_type = self.main_partner_id.distributor_type
            return {'domain': {'assigned_territory_id': [('id', 'in', self.main_partner_id.territory_ids.ids)]}}
        elif self.main_partner_id.distributor_type == 'premium':
            self.region_id = self.main_partner_id.region_id.id
            self.wilaya_id = self.main_partner_id.wilaya_id.id
            return {'domain': {'assigned_territory_id': [('id', 'in', self.main_partner_id.territory_ids.ids)]}}

    @api.onchange('distributor_id')
    def onchange_distributor_id(self):
        if self.partner_type == 'dealer':
            self.region_id = self.distributor_id.region_id.id
            self.wilaya_id = self.distributor_id.wilaya_id.id
            return {'domain': {'assigned_territory_id': [('id', 'in', self.distributor_id.territory_ids.ids)]}}

    @api.multi
    def change_data_fields(self, main_partner_id, partner_type, dealer_contact_type, dealer_id, distributor_id,
                           distributor_type):
        res = {}
        main_partner_id = self.env['res.partner'].browse(main_partner_id)
        dealer_id = self.env['res.partner'].browse(dealer_id)
        distributor_id = self.env['res.partner'].browse(distributor_id)
        if partner_type == 'salesperson':
            if main_partner_id.distributor_type in ('preferred', 'sub'):
                res = {'distributor_id': main_partner_id.id,
                       'main_partner_id': main_partner_id.main_partner_id.id,
                       'distributor_type': main_partner_id.distributor_type,
                       'salesperson_type': 'dsr'}
            else:
                res = {'distributor_id': False,
                       'main_partner_id': main_partner_id.id,
                       'distributor_type': main_partner_id.distributor_type,
                       'salesperson_type': 'dsm'}

        if partner_type == 'dealer' and dealer_contact_type is False:
            if distributor_type in ('preferred', 'sub'):
                res = {'distributor_id': distributor_id.id,
                       'distributor_type': distributor_type,
                       'main_partner_id': distributor_id.main_partner_id.id}
            else:
                res = {'distributor_id': False,
                       'distributor_type': main_partner_id.distributor_type,
                       'main_partner_id': main_partner_id.id}

        if dealer_contact_type == 'counter':
            if dealer_id.distributor_type in ('preferred', 'sub'):
                res = {'distributor_id': dealer_id.distributor_id.id,
                       'dsr_id': dealer_id.dsr_id.id,
                       'distributor_type': dealer_id.distributor_id.distributor_type,
                       'main_partner_id': dealer_id.distributor_id.main_partner_id.id}
            else:
                res = {'distributor_id': False,
                       'dsm_id': dealer_id.dsm_id.id,
                       'distributor_type': dealer_id.main_partner_id.distributor_type,
                       'main_partner_id': dealer_id.main_partner_id.id}
        return res

    @api.model
    def create(self, vals):
        main_partner_id = vals['main_partner_id'] or False if 'main_partner_id' in vals else False
        partner_type = vals['partner_type'] or False if 'partner_type' in vals else False
        dealer_contact_type = vals['dealer_contact_type'] if 'dealer_contact_type' in vals else False
        dealer_id = vals['dealer_id'] or False if 'dealer_id' in vals else False
        distributor_id = vals['distributor_id'] or False if 'distributor_id' in vals else False
        distributor_type = vals['distributor_type'] or False if 'distributor_type' in vals else False
        res = self.change_data_fields(main_partner_id, partner_type, dealer_contact_type, dealer_id, distributor_id,
                                      distributor_type)
        vals.update(res)
        return super(Partner, self).create(vals)

    @api.multi
    def product_by_category(self):
        form_view_ref = self.env.ref('ooredoo.res_product_template_oodoo_form', False)
        tree_view_ref = self.env.ref('ooredoo.res_product_template_oodoo_tree', False)
        return {
            'name': _('Products'),
            'view_mode': 'tree, form',
            'view_id': False,
            'view_type': 'form',
            'res_model': 'product.template',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': "[('categ_id', 'in', %s)]" % self.category_ids.ids,
            'views': [(tree_view_ref and tree_view_ref.id or False, 'tree'),
                      (form_view_ref and form_view_ref.id or False, 'form')],
            'context': {'default_type': 'product'}
        }
