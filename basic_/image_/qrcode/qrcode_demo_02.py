#!/usr/bin/env python3
#

# import from sys
from Crypto.Cipher import AES
import binascii
from os import path
import matplotlib.pyplot as plt
import json

# import from dist
import qrcode


# import from chekawa


# configs


# constants


# variables


# functions


# instances


class Qrcode(object):
    def __init__(self):
        self.__key = '1234567890123456'
        self.__hint = '''
ཆ་ཁ་བ་མཉེན་ཆས་ཕབ་ལེན
请使用chekawa程序扫描此二维码
'''

    def _aes_encode(self, data_str: str):

        # 编码
        data = data_str.encode()

        # aes加密函数, 如果data不是16的倍数, 加密文本data必须为16的倍数, 那就补足为16的倍数
        cipher = AES.new(self.__key, AES.MODE_CBC, self.__key)

        # 加密块大小, 默认16
        block_size = AES.block_size

        # 块补齐填充
        if len(data) % block_size != 0:
            padding_size = block_size - (len(data) % block_size)
        else:
            padding_size = 0

        data += b'\0' * padding_size

        # 使用aes加密
        cipher_data = cipher.encrypt(data)
        print(type(cipher_data))
        print(cipher_data)

        # 二进制密文转十六进制密文
        cipher_data_hex = binascii.b2a_hex(cipher_data)
        print(type(cipher_data_hex))
        print(cipher_data_hex)

        return cipher_data_hex

    def _gen_qrcode(self, data: str, ):
        '''
        version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。

        error_correction：控制二维码的错误纠正功能。可取值下列3个常量。
        ERROR_CORRECT_L：至多7%的错误能被纠正。
        ERROR_CORRECT_M（默认）：至多15%的错误能被纠正。
        ROR_CORRECT_H：至多30%的错误能被纠正。

        box_size：控制二维码中每个小格子包含的像素数。

        border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）
        '''
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.ERROR_CORRECT_H,
            # error_correction=qrcode.ERROR_CORRECT_L,
            box_size=10,
            border=2,
        )

        # 加密数据部分
        cipher_data = self._aes_encode(data)

        # 拼接提示
        cipher = self.__hint.encode() + cipher_data

        # 添加数据
        qr.add_data(cipher)

        # 填充数据
        qr.make(fit=True)

        # 生成图片
        img = qr.make_image(fill_color="black", back_color="white")
        img = img.convert("RGB")

        # 显示图片
        plt.imshow(img)
        plt.show()

        # # 保存图片
        # img.save(file_path)
        # return True

    def gen_qrcode_temple(self, temple_id: int):
        qr_kv = {'temple_id': str(temple_id)}
        qr_json = json.dumps(qr_kv)

        self._gen_qrcode(qr_json)

        # 目录路径
        # _dir_path = path.join(_WORK_DIR, _CONF_MEDIA.get('image'), str(temple_id))


if __name__ == '__main__':
    qr = Qrcode()
    qr.gen_qrcode_temple(96385274123696841231231236314236541265346512436541256436514236511322132312)
