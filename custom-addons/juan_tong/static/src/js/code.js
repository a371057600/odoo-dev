function myFunction()
{
    alert('succeed');
    window.location.href="https://www.baidu.com/";
}

function buyNow(temp)
{
    alert(temp);
   // a=document.getElementById("link");
    //a.innerHTML="<a href=https://www.baidu.com/ target+_blank></a>";
}
window.onload = function() {
	var sp = document.getElementsByTagName("li");
	var cons = document.querySelector(".bd").getElementsByTagName("div");
	for(var i = 0; i < sp.length; i++) {
		sp[i].index = i;
		sp[i].onclick = function() {
		    for(var j = 0; j < sp.length; j++) {
                sp[j].className = "";
                cons[j].className = "";
            }
		this.className = "current";
		cons[this.index].className = "show";
	    }
	}
}

    //????JS api ??
/*function onBridgeReady() {
        WeixinJSBridge.invoke(
            'getBrandWCPayRequest',
            {
                appId: "wx7376a2b8c3146546",        //?????,?????
                timeStamp: "1559613679", //???,?1970??????
                nonceStr: "vuNhv52X",  //???
                package: "prepay_id=wx041001197600906d01c802ac1173800100",  //???id
                signType: "MD5",  //??????
                paySign: "885CE44A4EB46C5E2401BB5ADC8A6D5F"     //????
            },
            function (res) {
                //??????? get_brand_wcpay_request:ok
                if (res.err_msg == "get_brand_wcpay_request:ok") {
                    // ??????????
                    window.location.href = '#';
                    {alert('????');}
                } else if (res.err_msg == "get_brand_wcpay_request:cancel") {
                    alert("??????!");
                    
                   }
                } else if (res.err_msg == "get_brand_wcpay_request:fail") {
                    $.each(res, function(key,value){
                        alert(value);
                        });
                    alert("????!");
                }
            
        );
    }
function test(){
    
    if (typeof WeixinJSBridge == "undefined") {
            if (document.addEventListener) {
                document.addEventListener('WeixinJSBridgeReady', onBridgeReady, false);
            } else if (document.attachEvent) {
                document.attachEvent('WeixinJSBridgeReady', onBridgeReady);
                document.attachEvent('onWeixinJSBridgeReady', onBridgeReady);
            }
        } else {
            onBridgeReady();
        }
}*/
