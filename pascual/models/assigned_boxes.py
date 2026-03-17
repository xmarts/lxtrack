
from odoo import api, fields, models
from odoo.tools.sql import drop_view_if_exists


class AssignedBox(models.Model):
    _name = "assigned.boxes"
    _description = "Cajas Asignadas"
    _auto = False

    # id = fields.Integer('Id', readonly=True) Field assigned.boxes.id is not an instance of fields.Id
    pedido = fields.Char('No. Pedido', readonly=True)
    producto = fields.Char('Producto', readonly=True)
    qty = fields.Integer('Cantidad', readonly=True)
    unidad =  fields.Char('Unidad', readonly=True)
    vendedor = fields.Char('Vendedor', readonly=True)
    repartidor = fields.Char('Repartidor', readonly=True)

    @api.model
    def init(self):
        drop_view_if_exists(self.env.cr, 'assigned_boxes')
        self.env.cr.execute("""
            create or replace view assigned_boxes as (
                  select sl.id, s.name as pedido, pt.name as producto,sl.product_uom_qty as qty,  resp.name as vendedor,  usm.login as repartidor
                    from sale_order_line  sl
                    left join sale_order s on s.id= sl.order_id
                    left join stock_picking sp on sp.origin =s.name
                    left join product_product p on p.id =sl.product_uom_id
                    left join product_template pt on p.product_tmpl_id=pt.id
                    left join product_uom pu on pu.id=sl.product_uom_id
                    left join res_users us on us.id = s.user_id
                    left join res_partner resp on resp.id= us.partner_id
                    left join res_users usm on usm.id = sp.deliveryman_id
                    group by resp.name,sl.id, s.name, pt.name,sl.product_uom_qty,usm.login

            )""")