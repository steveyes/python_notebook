#!/usr/bin/env python3
#

import jpush
from jpush import common

app_key = '59b2f897c0e8ce252bf2dbb7'
master_secret = 'a073aa2872cc228553a78ee7'


def get_device_temple(alias=None, reg_id=None):
    app_key = '59b2f897c0e8ce252bf2dbb7'
    master_secret = 'a073aa2872cc228553a78ee7'
    _jpush = jpush.JPush(app_key, master_secret)
    device = _jpush.create_device()

    try:
        if alias:
            response = device.get_aliasuser(alias=alias, )
        elif reg_id:
            response = device.get_deviceinfo(registration_id=reg_id)
        else:
            raise Exception("error alias or reg_id not found")
        print(response)
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


def send_temple(reg_id=None,):
    app_key = '59b2f897c0e8ce252bf2dbb7'
    master_secret = 'a073aa2872cc228553a78ee7'
    _jpush = jpush.JPush(app_key, master_secret)
    push = _jpush.create_push()
    # if you set the logging level to "DEBUG",it will show the debug logging.
    _jpush.set_logging("DEBUG")
    push.audience = jpush.all_
    push.notification = jpush.notification(alert="hello python jpush api")
    push.platform = jpush.all_
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


def get_device_cuser(alias=None, reg_id=None):
    app_key = '568a31c38959e0741704d915'
    master_secret = '66f517e9008515dac6f4bfd5'
    _jpush = jpush.JPush(app_key, master_secret)
    device = _jpush.create_device()

    try:
        if alias:
            response = device.get_aliasuser(alias=alias, )
        elif reg_id:
            response = device.get_deviceinfo(registration_id=reg_id)
        else:
            raise Exception("error alias or reg_id not found")
        print(response)
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


if __name__ == '__main__':
    alias = 'temple_1127'
    # alias = 'temple_1337'
    reg_id = '191e35f7e018ff742a0'
    get_device_temple(reg_id=reg_id)

    # alias = 'cuser_117'
    # get_device_cuser(alias=alias)

    # reg_id = '1114a89792ed1ba6404'
    # get_device_cuser(reg_id=reg_id)
