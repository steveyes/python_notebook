#!/usr/bin/env python3
#

from urllib import parse


def decode_alipay():
    str_alipay = 'gmt_create=2019-03-08+16%3A02%3A22&charset=utf-8&seller_email=1219921315%40qq.com&subject=chekawa%7B%E0%BD%86%E0%BC%8B%E0%BD%81%E0%BC%8B%E0%BD%96%7D&sign=MjkiYb5TvR1f02NdlJhPgOrlcX9SHjqe0PrxpoT8ZVvlGigsEWYrz0%2FdSQZGaBvoLRF5GAaKlls9r%2FyUZmWaXrX4Gzj6v58LXuBHZJ66NeTiFOFBFCqzwO%2BzumjycF7sA4bi3TuluZ8JnGvjKJ8VY%2FRig7hhhWS52AstDt%2FR60o1xZmFlTOAQl2y2ntmfa2sodm8qHMve36twbzalZOw23vJmpn1OzFurNGaiKtJZBWCjhkxNouJGeRqfQv668vR2O9dxsAWcaFaRvL50e47Dv93BIb5WMHDpHPXvCqS8vr1T1yO%2B8Jh29IhbggceZiENYl0%2Fj%2Fo0DgwFcMcnJdJDA%3D%3D&body=%E6%99%AE%E9%80%9A%E7%94%A8%E6%88%B7%E6%B3%A8%E5%86%8C%E8%B4%B9&buyer_id=2088312607027006&invoice_amount=0.01&notify_id=2019030800222160222027001003402253&fund_bill_list=%5B%7B%22amount%22%3A%220.01%22%2C%22fundChannel%22%3A%22ALIPAYACCOUNT%22%7D%5D&notify_type=trade_status_sync&trade_status=TRADE_SUCCESS&receipt_amount=0.01&app_id=2019020163223005&buyer_pay_amount=0.01&sign_type=RSA2&seller_id=2088621228155884&gmt_payment=2019-03-08+16%3A02%3A22&notify_time=2019-03-08+16%3A16%3A10&passback_params=notify_url_suffix%3Dcuser%26body%3Dcuser&version=1.0&out_trade_no=2019030816021700000111&total_amount=0.01&trade_no=2019030822001427001031728288&auth_app_id=2019020163223005&buyer_logon_id=187****2078&point_amount=0.00'
    str_decoded = {k: v[0] for k, v in parse.parse_qs(str_alipay).items()}
    [print(f"{k:20}{v}") for k, v in str_decoded.items()]


if __name__ == '__main__':
    decode_alipay()
