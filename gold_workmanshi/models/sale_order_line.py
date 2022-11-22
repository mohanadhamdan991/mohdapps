from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    # ===== Declare Fields =====

    gold_workmanship = fields.Float(string='Workmanship Per Unit')

    # ===== Declare Functions =====

    @api.onchange('gold_workmanship')
    def _compute_amount(self):
        res = super(SaleOrderLine, self)._compute_amount()
        for rec in self:
            if rec.gold_workmanship:
                rec.price_subtotal += (rec.gold_workmanship * rec.product_uom_qty)
                rec.price_total += (rec.gold_workmanship * rec.product_uom_qty)
            else:
                rec.price_subtotal += 0
                rec.price_total += 0
        return res

    def _prepare_invoice_line(self):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res['gold_workmanship'] = self.gold_workmanship
        res['new_price_unit'] = res['price_unit']
        res['price_unit'] += self.gold_workmanship
        print('res', res)
        return res
