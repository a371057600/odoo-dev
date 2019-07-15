from odoo import http
from odoo.http import request

class Buy(http.Controller):
    @http.route('/activity/<page>', auth = "public", website = True)
    def buy(self, page, **kwargs):
        Num = request.env['activity'].sudo()
        num = Num.search([('name', '=', page)])
        Inden = request.env['indent'].sudo()
        inden = Inden.search([])
        if num:
            return http.request.render('juan_tong.activity_web', {'orders': inden, 'docs': num})
        else:
            return '<h1>活动已结束或不存在<h1>'


class MyCard(http.Controller):
    @http.route('/card/<page>', auth="public", website=True)
    def card(self, page, **kwargs):
        Inden = request.env['indent'].sudo()
        inden = Inden.search([])

        return http.request.render('juan_tong.card_web', {'orders': inden})
