from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    # ===== Declare Fields =====

    gold_workmanship = fields.Float(string='Workmanship Per Unit')

    # ===== Declare Functions =====

    @api.depends('product_qty', 'price_unit', 'taxes_id')
    def _compute_amount(self):
        res = super(PurchaseOrderLine, self)._compute_amount()
        for rec in self:
            if rec.gold_workmanship:
                rec.price_subtotal += (rec.gold_workmanship * rec.product_qty)
                rec.price_total += (rec.gold_workmanship * rec.product_qty)
            else:
                rec.price_subtotal += 0
        return res

    def _prepare_account_move_line(self, move):
        res = super(PurchaseOrderLine, self)._prepare_account_move_line(move)
        res.update({
            'gold_workmanship': self.gold_workmanship,
            'new_price_unit': self.price_unit,
            'price_unit': self.price_unit + self.gold_workmanship,
        })
        return res
