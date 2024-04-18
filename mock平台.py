"""
123123123
Administrator
2024/4/17
"""

"""
123123123
Administrator
2024/4/13
"""
import random

import time

from flask import Flask,request,json
#实例化一个web服务对象
app=Flask(__name__)
#创建一个方法来处理请求
#定义一个路由--访问服务的根目录就可以得到结果
#构造一个接受post请求的响应
@app.route('/post',methods=['POST'])
def test_post():
    a =  {
    "alipay_trade_pay_response": {
        "code": "10000",
        "msg": "Success",
        "trade_no": "2013112011001004330000121536",
        "out_trade_no": "6823789339978248",
        "buyer_logon_id": "159****5620",
        "settle_amount": "88.88",
        "pay_currency": "CNY",
        "pay_amount": "580.04",
        "settle_trans_rate": "1",
        "trans_pay_rate": "6.5261",
        "total_amount": 120.88,
        "trans_currency": "USD",
        "settle_currency": "USD",
        "receipt_amount": "88.88",
        "buyer_pay_amount": 8.88,
        "point_amount": 8.12,
        "invoice_amount": 12.5,
        "gmt_payment": "2014-11-27 15:45:57",
        "fund_bill_list": [
            {
                "fund_channel": "ALIPAYACCOUNT",
                "bank_code": "CEB",
                "amount": 10,
                "real_amount": 11.21
            }
        ],
        "card_balance": 98.23,
        "store_name": "证大五道口店",
        "buyer_user_id": "2088101117955611",
        "discount_goods_detail": "[{\"goods_id\":\"STANDARD1026181538\",\"goods_name\":\"雪碧\",\"discount_amount\":\"100.00\",\"voucher_id\":\"2015102600073002039000002D5O\"}]",
        "voucher_detail_list": [
            {
                "id": "2015102600073002039000002D5O",
                "name": "XX超市5折优惠",
                "type": "ALIPAY_FIX_VOUCHER",
                "amount": 10,
                "merchant_contribute": 9,
                "other_contribute": 1,
                "memo": "学生专用优惠",
                "template_id": "20171030000730015359000EMZP0",
                "purchase_buyer_contribute": 2.01,
                "purchase_merchant_contribute": 1.03,
                "purchase_ant_contribute": 0.82
            }
        ],
        "advance_amount": "88.8",
        "auth_trade_pay_mode": "CREDIT_PREAUTH_PAY",
        "charge_amount": "8.88",
        "charge_flags": "bluesea_1",
        "settlement_id": "2018101610032004620239146945",
        "business_params": "{\"data\":\"123\"}",
        "buyer_user_type": "PRIVATE",
        "mdiscount_amount": "88.88",
        "discount_amount": "88.88",
        "buyer_user_name": "菜鸟网络有限公司"
    },
    "sign": "ERITJKEIJKJHKKKKKKKHJEREEEEEEEEEEE"
    }
    return a
@app.route('/')
def hello():
    b = test_post()
    return "<h1>这是一个mock平台 url:http://127.0.0.1:9090/post 方法：POST</h1>"
if __name__ == "__main__":
    app.run("127.0.0.1","9090")
