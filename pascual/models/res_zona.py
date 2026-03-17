#
from odoo import models, fields, api, _, tools
from odoo.exceptions import UserError, RedirectWarning, ValidationError
import shutil
import logging
_logger = logging.getLogger(__name__)
class ResZona(models.Model):
    _name = "res.zona"
    name= fields.Char(string="Nombre")
    user_id =fields.Many2one('hr.employee', string="Usuario", domain=[('department_id', '=',2)])