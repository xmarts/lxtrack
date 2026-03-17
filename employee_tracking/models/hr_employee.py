#
from odoo import models, fields, api, _, tools
from odoo.exceptions import UserError, RedirectWarning, ValidationError
import shutil
import logging
from hashlib import sha1
_logger = logging.getLogger(__name__)
class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    password = fields.Char('Contraseña')

    @api.model
    def create(self, vals):
        if vals['password'] is not False or vals['password'] is not  None:
            val=str(vals['password']).encode('utf-8')
            pasw= sha1(val).hexdigest()
            vals['password']=pasw
        return super(HrEmployee, self).create(vals)

    def write(self, vals):
        if vals.get('password'):
            val=str(vals['password']).encode('utf-8')
            pasw= sha1(val).hexdigest()
            vals['password']=pasw
        return super(HrEmployee, self).write(vals)