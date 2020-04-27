# -*- coding: utf-8 -*-

from odoo import api, models, modules, fields


class CompanyType(models.Model):
    _name = 'company.type'
    _description = 'Company Type'
    _rec_name = 'name'

    name = fields.Char('Name')


class ShippingMethod(models.Model):
    _name = 'shipping.method'
    _description = 'Shipping Method'
    _rec_name = 'name'

    name = fields.Char('Name')


class FreightTerms(models.Model):
    _name = 'freight.terms'
    _description = 'Freight Terms'
    _rec_name = 'name'

    name = fields.Char('Name')


class ChannelType(models.Model):
    _name = 'channel.type'
    _description = 'Channel Type'
    _rec_name = 'name'

    name = fields.Char('Name')
    partner_type = fields.Selection([('distributor', 'Distributor'), ('dealer', 'Dealer'),],
                                    default='distributor', string='Type')


class DistributorType(models.Model):
    _name = 'distributor.type'
    _description = 'Distributor Type'
    _rec_name = 'name'

    name = fields.Char('Name')


class DistributorClass(models.Model):
    _name = 'distributor.class'
    _description = 'Distributor Class'
    _rec_name = 'name'

    name = fields.Char('Name')


class ApplicableTaxesType(models.Model):
    _name = 'applicable.taxes.type'
    _description = 'Applicable Taxes Type'
    _rec_name = 'name'

    name = fields.Char('Name')


class DealerBusinessType(models.Model):
    _name = 'dealer.business.type'
    _description = 'Dealer business type'
    _rec_name = 'name'

    name = fields.Char('Name')


class DealerAccountType(models.Model):
    _name = 'dealer.account.type'
    _description = 'Dealer Account Type'
    _rec_name = 'name'

    name = fields.Char('Name')


class DealerSegment(models.Model):
    _name = 'dealer.segment'
    _description = 'Dealer Segment'
    _rec_name = 'name'

    name = fields.Char('Name')


class Region(models.Model):
    _name = 'res.region'
    _description = 'Region'
    _rec_name = 'name'

    name = fields.Char('Name')
    reg_id = fields.Integer('ID')
    country_id = fields.Many2one('res.country', string='Country')


class Wilaya(models.Model):
    _name = 'res.wilaya'
    _description = 'Wilaya'
    _rec_name = 'name'

    name = fields.Char('Name')
    wil_id = fields.Integer('ID')
    region_id = fields.Many2one('res.region', 'Region')


class AssignedTerritory(models.Model):
    _name = 'assigned.territory'
    _description = 'Assigned territory'
    _rec_name = 'name'

    ter_id = fields.Integer('ID')
    name = fields.Char('Name')
    wilaya_id = fields.Many2one('res.wilaya', string='Wilaya')
    territory_type_id = fields.Many2one('territory.type', string='Territory Type')


class TerritoryType(models.Model):
    _name = 'territory.type'
    _description = 'Territory Type'
    _rec_name = 'name'

    name = fields.Char('Name')


class Area(models.Model):
    _name = 'res.area'
    _description = 'Area'
    _rec_name = 'name'

    are_id = fields.Integer('ID')
    name = fields.Char('Name')
    area_type_id = fields.Many2one('area.type', 'Type')
    area_manager_id = fields.Many2one('area.manager', string='Area Manager')


class AreaType(models.Model):
    _name = 'area.type'
    _description = 'Area Type'
    _rec_name = 'name'

    name = fields.Char('Name')


class AreaManager(models.Model):
    _name = 'area.manager'
    _description = 'Area Manager'
    _rec_name = 'name'

    name = fields.Char('Name')


class SalespersonPosition(models.Model):
    _name = 'salesperson.position'
    _description = 'Salesperson Position'
    _rec_name = 'name'

    name = fields.Char('Name')


class SalespersonClass(models.Model):
    _name = 'salesperson.class'
    _description = 'Salesperson Class'
    _rec_name = 'name'

    name = fields.Char('Name')


class SalespersonSupervisor(models.Model):
    _name = 'salesperson.supervisor'
    _description = 'Salesperson Supervisor'
    _rec_name = 'name'

    name = fields.Char('Name')


class PartnerAddress(models.Model):
    _name = 'partner.address'
    _description = 'Partner Address'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string='Partner')
    address_type = fields.Selection([('billing', 'Billing Address'), ('shipping', 'Shipping Address 1'),
                                     ('shipping2', 'Shipping Address 2')], default='billing', string='Addresses')
    street = fields.Char('Street')
    zip = fields.Char('Postal')
    wilaya_id = fields.Many2one('res.wilaya', 'Wilaya', ondelete='restrict')
    region_id = fields.Many2one('res.region', string='Region', ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')


class PartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    state = fields.Char('Status')


class LegalInformation(models.Model):
    _name = 'legal.information'
    _description = 'Legal Information'
    _rec_name = 'vat'

    type = fields.Selection([('dealer', 'Dealer'), ('distributor', 'Distributor')], default='dealer', string='Type')
    street = fields.Char('Street')
    zip = fields.Char('Postal')
    wilaya_id = fields.Many2one('res.wilaya', 'Wilaya', ondelete='restrict')
    region_id = fields.Many2one('res.region', string='Region', ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    registration_number = fields.Char('Registration Number')
    company_type_id = fields.Many2one('company.type', 'Company Type')
    vat = fields.Char('Tax ID')
    municipality_expiry_date = fields.Date('Municipality Expiry')
    tra_license_status = fields.Selection([('available', 'Available'), ('not', 'Not-available')],
                                          default='available', string='TRA License Status')


class PartnerContract(models.Model):
    _name = 'partner.contract'
    _description = 'Partner Contract'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string='Partner')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    renewal_date = fields.Date('Renewal Date')
