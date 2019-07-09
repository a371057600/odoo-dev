from odoo import fields, models

class Book(models.Model):

    _inherit = 'library.book' # 使用_inherit类属性来声明所继承模型。
    """
        _name是模型标识符，如果修改会发生什么呢？
        其实你可以修改，这时它会创建所继承模型的拷贝，成为一个新模型。
        这叫作原型继承，本文后面会讨论。
    """
    is_available = fields.Boolean('Is Available?')