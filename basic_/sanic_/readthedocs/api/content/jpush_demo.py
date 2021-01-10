#!/usr/bin/env python3
#


import jpush
from jpush import common


class JPush(object):
    def __init__(self):
        __appkey = '59b2f897c0e8ce252bf2dbb7'
        __mastersecret = 'a073aa2872cc228553a78ee7'
        self._jpush = jpush.JPush(__appkey, __mastersecret)
        self._jpush.set_logging('DEBUG')
        self.options = {'apns_production': True}

    def get_device(self, registration_id):
        device = self._jpush.create_device()
        device.options = self.options
        try:
            response = device.get_deviceinfo(registration_id)
        except common.Unauthorized:
            raise common.Unauthorized("Unauthorized")
        except common.APIConnectionException:
            raise common.APIConnectionException("conn error")
        except common.JPushFailure:
            print("JPushFailure")
        except Exception:
            print("Exception")
        else:
            return response

    def set_device(self, registration_id, mobile, alias, tags_add: [str] = None, tags_remove: [str] = None, ):
        device = self._jpush.create_device()
        device.options = self.options
        tags = {}
        if tags_add:
            tags['add'] = tags_add

        if tags_remove:
            tags['remove'] = tags_remove

        payload = {
            "tags": tags,
            "alias": alias,
            "mobile": mobile,
        }

        try:
            response = device.set_deviceinfo(registration_id=registration_id, entity=payload)
        except common.Unauthorized:
            raise common.Unauthorized("Unauthorized")
        except common.APIConnectionException:
            raise common.APIConnectionException("conn error")
        except common.JPushFailure:
            print("JPushFailure")
        except Exception:
            print("Exception")
        else:
            return response

    def send(self, alert, alias: [str] = None, registration_id: [str] = None, platform=None, ):

        push = self._jpush.create_push()

        # audience
        if alias:
            push.audience = {"alias": alias}
        elif registration_id:
            push.audience = {"registration_id": [registration_id, ]}
        else:
            raise Exception("jpush audience not found!")

        # platform && notification
        if platform == 'android':
            android_msg = jpush.android(alert=alert, )
            push.notification = jpush.notification(android=android_msg)
            push.platform = platform
        elif platform == 'ios':
            ios_msg = jpush.ios(alert=alert, badge="+1")
            push.notification = jpush.notification(ios=ios_msg)
            push.platform = platform
        else:
            push.notification = jpush.notification(alert=alert)
            push.platform = jpush.all_

        # options
        push.options = self.options

        try:
            response = push.send()
        except common.Unauthorized:
            raise common.Unauthorized("Unauthorized")
        except common.APIConnectionException:
            raise common.APIConnectionException("conn error")
        except common.JPushFailure:
            print("JPushFailure")
        except:
            print("Exception")
        else:
            return response


def get_device_demo():
    jpush = JPush()
    registration_id = '1a1018970afb9a7a1e0'
    # registration_id = '161a3797c842d71b6a8'

    response = jpush.get_device(registration_id)
    print(response)


def set_device_demo():
    jpush = JPush()
    registration_id = '1a1018970afb9a7a1e0'
    mobile = '18918029173'
    alias = f"000"
    tags_remove = None
    response = jpush.set_device(registration_id, mobile, alias, tags_remove=tags_remove, )
    print(response)


def send_demo():
    jpush = JPush()
    alert = '您有一条信息的请求待处理.'
    alias = ['1430', ]
    jpush.send(alert=alert, alias=alias, platform='ios')


if __name__ == '__main__':
    get_device_demo()
    # set_device_demo()
    # send_demo()
