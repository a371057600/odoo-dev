odoo.define('juan_tong.button_buy', function(require){
'use strict';
var core = require('web.core');
var session = require('web.Session');
var Widget = require('web.Widget');
var User = require('juantong.share').Ticket;
var rpc = require('web.rpc');
var ajax = require('web.ajax');
var qweb = core.qweb;
var _t = core._t;

require('web.dom_ready');

var BuyButton = Widget.extend({
    template: 'buy.template',
    events: {
        'click .o_buynow': '_onClick',
    },
    xmlDependencies: ['/juan_tong/static/src/xml/widget_template.xml'],

    init: function () {
    },
    _onClick: function () {
     
        this.user = new User();
        //this.user.test();
       // var c = this.user.test();

        if (typeof WeixinJSBridge == "undefined") {
          alert('p3'); 
	   if (document.addEventListener) {
		alert('p4');
                document.addEventListener('WeixinJSBridgeReady', this.user.onBridgeReady(), false);
            } else if (document.attachEvent) {
                document.attachEvent('WeixinJSBridgeReady', this.user.onBridgeReady());
                document.attachEvent('onWeixinJSBridgeReady', this.user.onBridgeReady());
            }
        } else {
	    alert('p5');
            this.user.onBridgeReady();
        }
	 },
	/*onBridgeReady: function(){


    	WeixinJSBridge.invoke(
         'getBrandWCPayRequest', {
         "appId":"wx2421b1c4370ec43b",     //公众号名称，由商户传入
         "timeStamp":"1395712654",         //时间戳，自1970年以来的秒数
         "nonceStr":"e61463f8efa94090b1f366cccfbbb444", //随机串
         "package":"prepay_id=u802345jgfjsdfgsdg888",
         "signType":"MD5",         //微信签名方式：
         "paySign":"70EA570631E4BB79628FBCA90534C63FF7FADD89" //微信签名
      },
      function(res){
      if(res.err_msg == "get_brand_wcpay_request:ok" ){
      // 使用以上方式判断前端返回,微信团队郑重提示：
            //res.err_msg将在用户支付成功后返回ok，但并不保证它绝对可靠。
      }
   });
},*/
});
var app = new BuyButton(null);

app.appendTo($(".o_buy")).then(function () {

    });
return BuyButton;
});


