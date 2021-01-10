#!/usr/bin/env python3
#
import base64
from urllib.parse import parse_qs
import rsa




def demo1():
    data = '''gmt_create=2018-12-23+17%3A00%3A04&charset=utf-8&seller_email=1219921315%40qq.com&subject=chekawa%7B%E0%BD%86%E0%BC%8B%E0%BD%81%E0%BC%8B%E0%BD%96%7D&sign=IIljTnH0dGFz675ZlNCpQ%2FVxiAdD8zdcttMAdEjG9z5hyX3nPf7kpXrvffLHusIx5LpPlCRrL5eDB%2B%2B5SQadEU81rLHaN%2B%2Bwamf373wwi%2F%2FVsV2SFZ0gRo2mgJ15VpzSTyq1850rsjo3SOAGpdK9LbjEeJWAac0GPi2DSfBcBaT9Y1Ao%2BIkjTtrAqI9YGIlaN5XAqZ%2FTfriO3QWeO9%2FY5S%2BT19mJqTktZBaEiQI9nBCo4SP3NNxzztOKtlRuhDUy2Q9uppBMyGgIGZqHWdZSdES%2B7QMKM%2F%2BbCH%2Bfg4iwPbApHQQff5F9PHtlNC7eqLQeWpiOAyyESNnr62sSi%2FYejg%3D%3D&body=庄村入住费&buyer_id=2088312607027006&invoice_amount=0.01&notify_id=2018122300222170005027000532482346&fund_bill_list=%5B%7B%22amount%22%3A%220.01%22%2C%22fundChannel%22%3A%22ALIPAYACCOUNT%22%7D%5D&notify_type=trade_status_sync&trade_status=TRADE_SUCCESS&receipt_amount=0.01&app_id=2018122162679203&buyer_pay_amount=0.01&sign_type=RSA2&seller_id=2088621228155884&gmt_payment=2018-12-23+17%3A00%3A05&notify_time=2018-12-23+17%3A14%3A30&version=1.0&out_trade_no=2123456&total_amount=0.01&trade_no=2018122322001427000551397000&auth_app_id=2018122162679203&buyer_logon_id=187****2078&point_amount=0.00'''
    kv_data = {k: v[0] for k, v in parse_qs(data).items()}
    kv_sorted_by_key = sorted(kv_data.items(), key=lambda kv: kv[0], reverse=False)
    kv_sorted_by_value_desc = sorted(kv_data.items(), key=lambda kv: kv[1], reverse=True)
    print('-' * 79)
    [print({k: v}) for k, v in kv_sorted_by_key]
    print('-' * 79)
    [print({k: v}) for k, v in kv_sorted_by_value_desc]
    print('-' * 79)
    # kv_message = "&".join(f"{k}={v}" for k, v in kv_sorted_by_key)
    kv_message = "&".join(u"{}={}".format(k, v) for k, v in kv_sorted_by_key)
    print(kv_message)


def demo2():
    import operator

    xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

    res = sorted(xs.items(), key=lambda x: x[1])
    print('-' * 79)
    [print({k: v}) for k, v in res]
    res = sorted(xs.items(), key=operator.itemgetter(1))
    print('-' * 79)
    [print({k: v}) for k, v in res]


def verify_with_rsa(public_key, message, sign_txt):
    sign = base64.b64decode(sign_txt)
    return rsa.verify(message, sign, rsa.PublicKey.load_pkcs1_openssl_pem(public_key))


if __name__ == '__main__':

    pub = open('chekawa_alipay.pub').read()
    message = 'app_id=2018122162679203&auth_app_id=2018122162679203&body=checkin&buyer_id=2088312607027006&buyer_logon_id=187****2078&buyer_pay_amount=0.01&charset=utf-8&fund_bill_list=[{"amount":"0.01","fundChannel":"ALIPAYACCOUNT"}]&gmt_create=2018-12-25 16:05:01&gmt_payment=2018-12-25 16:05:01&invoice_amount=0.01&notify_id=2018122500222160501027000548126009&notify_time=2018-12-25 16:19:41&notify_type=trade_status_sync&out_trade_no=201812251604460014&point_amount=0.00&receipt_amount=0.01&seller_email=1219921315@qq.com&seller_id=2088621228155884&subject=chekawa&total_amount=0.01&trade_no=2018122522001427000564405231&trade_status=TRADE_SUCCESS&version=1.0'.encode()
    sign_txt = 'UcBsQ1qcM8KZeZz5krWdwfEntWVIaTyxEgUJcgL2/INvfKNEdmJFo6uGd7CQR0wV+1bhviNAIV6yLQ+lk+xUiZhUf8U626FC16VQaZWsfXv5EB3xVuHfVFvs+dQB/xhSaUPIsltNMipeTQRI42J3w4xjy8wAlrnBobhaecusPtni4SCyO2ts+e0RnrcsMp3PjQU2wCKjLPHxij3IMCYtDcig80rqInwNqSeltG7QqHXmhd/clYl5hU3scCo15tq0n4SgR77amHh8bn2dTILtTb8X0198QYa429uf2Yg/HO0QNMUmNI8JoDqjGwvabZyPpq+oGdI8GuF+R3X6iSOCQg=='.encode()
    sign = base64.b64decode(sign_txt)

    print(verify_with_rsa(pub.encode().decode(), message, sign_txt))
