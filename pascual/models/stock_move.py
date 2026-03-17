#
from odoo import models, fields, api, _, tools
from odoo.exceptions import UserError, RedirectWarning, ValidationError
import shutil
import logging
_logger = logging.getLogger(__name__)
class StockMove(models.Model):
    _inherit = "stock.move"
    # zona = fields.Many2one('res.zona', related="picking_partner_id.zona", store=True) el camppo picking_partner_id ahora es parte de stock.move.line
    zona = fields.Many2one('res.zona')