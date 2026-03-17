#
from odoo import models, fields, api, _, tools
from odoo.exceptions import UserError, RedirectWarning, ValidationError
import shutil
import logging
_logger = logging.getLogger(__name__)
class Motivo(models.Model):
    _name="res.motivo"
    name = fields.Char(string="Motivo")
