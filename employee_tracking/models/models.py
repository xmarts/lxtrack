#
from odoo import models, fields, api, _, tools
from odoo.exceptions import UserError, RedirectWarning, ValidationError
import shutil
import logging
_logger = logging.getLogger(__name__)

#class xmartsstockpicking(models.Model):
#	_inherit ='stock.picking'
#  	xmpack= fields.Boolean(string="Empaquetado",default=False)