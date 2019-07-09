from odoo import api, fields, models
from odoo.exceptions import Warning


class Book(models.Model):
    """
    第一行是 Python 代码导入语句，让 Odoo 内核的models和fields对象在这里可用。
    紧接着声明了新的模型，它是models.Model派生出的一个类。
    然后_name 属性定义了 Odoo 全局对该模型引用的标识符。
    注意Python 类名 Book 与框架无关，_name 的值才是模型的标识符。
    """
    _name = 'library.book'
    _description = 'Book'
    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    active = fields.Boolean('Active?', default=True)
    date_published = fields.Date()
    image = fields.Binary('Cover')
    publisher_id = fields.Many2one('res.partner', string='Publisher') 
    author_ids = fields.Many2many('res.partner', string='Authors')

    # 对于记录的逻辑，我们使用@api.multi装饰器。此处 self 表示一个记录集，然后我们遍历每一条记录。
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
        # 代码遍历所有已选图书，对于每本书，如果 ISBN 有值，则检查有效性，若无值，则向用户抛出一条警告消息。
        for book in self:
            if not book.isbn:
                raise Warning('Please provide an ISBN for %s' % book.name)
            if book.isbn and not book._check_isbn():
                raise Warning('%s is an invalid ISBN' % book.isbn)
            return True
