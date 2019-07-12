{
    # 声明文件
    # 仅 name属性为必填，但推荐同时添加 description 和 author 属性
    'name': 'Library Management',
    'description': 'Manage library book catalogue and lending.',
    'author': 'Alan Hou',
    
    # depends 属性可以是一个包含所用到的模块列表。
    # Odoo 会在模块安装时自动安装这些模块，这不是强制属性，但建议使用。
    # 如果没有特别的依赖，可以添加内核 base 模块。
    # 应注意将所有依赖都在此处列明，否则，模块会因缺少依赖而报错或出现加载错误
    'depends': ['base'],
    'application': True,

    # 注意library_security.xml 加在library_menu.xml文件之前，
    # 数据文件的加载顺序非常重要，因为我们只能引用已经定义过的标识符。
    # 菜单项经常引用到安全组，所以建议将安全组定义文件放到菜单和视图文件之前
    'data': [
        'security/library_security.xml',
        # 权限通过该文件添加、该文件最后一行不能留空格、否则会报错
        # 文件名必须与要载入的模型对应，第一行为列名，CSV 文件中有如下列：

        # id是记录的外部标识符（也称为XML ID），需在模块中唯一
        # name是描述性标题，仅在保证唯一时提供有用信息
        # model_id是赋权模型的外部标识符，模型有ORM自动生成的XML ID，对于library.book，标识符为model_library_book
        # group_id指明授权的安全组，我们给前文创建的安全组授权：library_group_user和library_group_manager
        # perm_…字段标记read读, write写, create创建, 或unlink删除权限，我们授予普通用户读权限、管理员所有权限
        'security/ir.model.access.csv',
        'views/library_menu.xml',  
        'views/book_view.xml',
        'views/book_list_template.xml',
    ],
}

# 其他说明
# 更新模板命令：~/odoo-dev/odoo/odoo-bin -d dev12 -u library_app
# -u：更新、-i：新增
# -u(或全称–update)要求使用-d 参数并接收一个逗号分隔的待升级模块集。
# 例如可以使用-u library_app,mail

# 添加模型字段时需进行升级。修改 Python 代码（含 manifest 文件）时需要重启服务。
# 修改XML或CSV文件时，需进行升级。在不确定时，同时重启服务并升级模块。

# 我们创建的是一个图书应用，所以应包含这些元素，它们是：
# - 图标：用于在应用列表中展示
# - 顶级菜单项：其下放置所有的应用菜单项
# - 应用安全组：通过权限访问仅对指定用户（User）开放

# 添加图标(icon)，仅需在模块目录下static/description/子文件夹中放置icon.png文件
# 菜单项是使用 XML 文件中添加的视图组件，通过创建views/library_menu.xml来定义菜单项


