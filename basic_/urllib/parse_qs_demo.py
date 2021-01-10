#!/usr/bin/env python3
#
from urllib.parse import parse_qs
from urllib.parse import unquote
import json

'''
encode: application/x-www-form-urlencoded
'''


def parse_data(data):
    res = parse_qs(data)

    for k, v in res.items():
        print(f'{k}:{v[0]}')


def parse_unquote(data):
    res = unquote(data)

    return res


if __name__ == '__main__':
    data1 = '''
data%5Bname1%5D=test&
data%5Bname2%5D=test&
data%5Bname3%5D=test&
data%5Bname4%5D=test'''
    data2 = '''gmt_create=2018-12-23+17%3A00%3A04&charset=utf-8&seller_email=1219921315%40qq.com&subject=chekawa%7B%E0%BD%86%E0%BC%8B%E0%BD%81%E0%BC%8B%E0%BD%96%7D&sign=IIljTnH0dGFz675ZlNCpQ%2FVxiAdD8zdcttMAdEjG9z5hyX3nPf7kpXrvffLHusIx5LpPlCRrL5eDB%2B%2B5SQadEU81rLHaN%2B%2Bwamf373wwi%2F%2FVsV2SFZ0gRo2mgJ15VpzSTyq1850rsjo3SOAGpdK9LbjEeJWAac0GPi2DSfBcBaT9Y1Ao%2BIkjTtrAqI9YGIlaN5XAqZ%2FTfriO3QWeO9%2FY5S%2BT19mJqTktZBaEiQI9nBCo4SP3NNxzztOKtlRuhDUy2Q9uppBMyGgIGZqHWdZSdES%2B7QMKM%2F%2BbCH%2Bfg4iwPbApHQQff5F9PHtlNC7eqLQeWpiOAyyESNnr62sSi%2FYejg%3D%3D&body=check_in&buyer_id=2088312607027006&invoice_amount=0.01&notify_id=2018122300222170005027000532482346&fund_bill_list=%5B%7B%22amount%22%3A%220.01%22%2C%22fundChannel%22%3A%22ALIPAYACCOUNT%22%7D%5D&notify_type=trade_status_sync&trade_status=TRADE_SUCCESS&receipt_amount=0.01&app_id=2018122162679203&buyer_pay_amount=0.01&sign_type=RSA2&seller_id=2088621228155884&gmt_payment=2018-12-23+17%3A00%3A05&notify_time=2018-12-23+17%3A14%3A30&version=1.0&out_trade_no=2123456&total_amount=0.01&trade_no=2018122322001427000551397000&auth_app_id=2018122162679203&buyer_logon_id=187****2078&point_amount=0.00'''
    # print(parse_data(data1))
    res = parse_qs(data2)
    [print({k: v[0]}) for k, v in res.items() if k in 'body']
    print('-----' * 10)
    [print({k: v[0]}) for k, v in res.items()]
