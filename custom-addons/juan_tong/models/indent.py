from odoo import api, fields, models

class Indent(models.Model):
	_name = "indent"
	_description = "订单"
	
	
	id_activity = fields.Many2one("activity", '活动', domain="[('name_id','=', id_name_id)]", ondelete='restrict')
	id_name_id = fields.Many2one('shangjia', '商家', ondelete='restrict')
#	activity_name_id=fields.Char(string='活动名称', compute='_compute_activity', store=True, inverse='_write_stage_fold')
	number = fields.Integer("数量")
	unit_price = fields.Float("单价", required=True)
	username = fields.Char("用户名", required=True)
	username_addr = fields.Char('用户名缩写', compute='_compute_username')
	indent_time = fields.Datetime("订单时间", default=lambda self: fields.Datetime.now())
	indent_number = fields.Char("订单编号")
	status = fields.Selection([('unavailable','未领取'),('available','已领取')],'状态')

	def _compute_username(self):
		for name in self:
			if len(name.username) > 2:
				name.username_addr = name.username[0] + '***' + name.username[-1]
			else:
				name.username_addr = name.username[0] + '***'

	@api.model
	def create(self,vals):
		if not vals.get('indent_number'):
			vals['indent_number'] = self.env['ir.sequence'].next_by_code('indent') or '/'
			#print vals['name']
		return super(Indent,self).create(vals)
	
	
	'''@api.depends('id')
	def _inverse_indent_number(self):
		for cord in self:
			cord.indent_number = cord.id
'''
#	@api.onchange('activity_id')
#	def _compute_activity(self):
#		for indent in self:
#			if indent.activity_id:
#				indent.activity_name_id = indent.activity_id.NameCN
#
#	def _write_stage_fold(self):
#		for indent in self:
#			if indent.activity_id:
#				indent.activity_id.NameCN = indent.activity_name_id

