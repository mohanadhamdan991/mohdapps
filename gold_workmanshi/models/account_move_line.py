from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    # ===== Declare Fields =====

    new_price_unit = fields.Float(string='Price Unit', store=True)
    gold_workmanship = fields.Float(string='Workmanship Per Unit')

    # ===== Declare Functions =====

    @api.onchange('new_price_unit', 'gold_workmanship')
    def onchange_gold_workmanship(self):
        if self.exclude_from_invoice_tab == False:
            self.price_unit = self.new_price_unit + self.gold_workmanship
            print('self.new_price_unit', self.new_price_unit)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        res = super(AccountMoveLine, self)._onchange_product_id()
        for line in self:
            line.new_price_unit = line.price_unit
        return res
