#
from odoo import models, fields, api, _, tools
from odoo.exceptions import UserError, RedirectWarning, ValidationError
import shutil
import logging
_logger = logging.getLogger(__name__)
class ReasonRejection(models.Model):
    _name="reason.rejection"
    name =fields.Char(string="Nombre")