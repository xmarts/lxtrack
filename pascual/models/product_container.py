#
from odoo import models, fields, api, _, tools
from odoo.exceptions import UserError, RedirectWarning, ValidationError
import shutil
import logging
_logger = logging.getLogger(__name__)
class ProductContainer(models.Model):
    _name="product.container"
    _description="Tipo de Envase del Producto"
    name = fields.Char(string="Envase")