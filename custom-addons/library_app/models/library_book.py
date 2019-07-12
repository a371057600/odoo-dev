# 模型描述业务对象，如商机、销售订单或合作伙伴（用户、供应商等）
# 模型中有一系列属性，也可定义一些特定业务逻辑

# 模型通过 Odoo 模板类派生的 Python 类来实现
# 它直接与数据库对象对应，Odoo 在安装或升级模块时会自动进行处理
# 框架中负责这部分的是对象关系映射（ORM -Object Relational Mapping）

from odoo import api, fields, models
from odoo.exceptions import Warning


class Book(models.Model):
    # _name 属性定义了 Odoo 全局对该模型引用的标识符
    _name = 'library.book'
    _description = 'Book'
    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    # active 字段用于激活记录，默认仅 active 记录会显示
    active = fields.Boolean('Active?', default=True)
    date_published = fields.Date()
    image = fields.Binary('Cover')
    # publisher_id是一个出版公司多对一关联
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    # author_ids是作者多对多关联
    author_ids = fields.Many2many('res.partner', string='Authors')
    # 都是图书与 partner 模型的关联，partner 模型内置于 Odoo 框架中，用户、公司和地址都存储在这里

    @api.multi
    def _check_isbn(self):
        self.ensure_one()
        isbn = self.isbn.replace('-', '')
        digits = [int(x) for x in isbn if x.isdigit()]
        if len(digits) == 13:
            ponderations = [1, 3] * 6
            terms = [a * b for a,b in zip(digits[:12], ponderations)]
            remain = sum(terms) % 10
            check = 10 - remain if remain !=0 else 0
            return digits[-1] == check

    @api.multi
    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise Warning('Please provide an ISBN for %s' % book.name)
            if book.isbn and not book._check_isbn():
                raise Warning('%s is an invalid ISBN' % book.isbn)
            return True
