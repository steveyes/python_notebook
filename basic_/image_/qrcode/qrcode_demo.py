#!/usr/bin/env python3
#

# import from sys
import qrcode
from PIL import Image
from pprint import pprint
import matplotlib.pyplot as plt
from Crypto.Cipher import AES
import binascii


# import from dist


# import from chekawa


# configs


# constants


# variables


# functions


# instances

def aes_encode(data, key):
    # aes加密函数, 如果data不是16的倍数, 加密文本data必须为16的倍数, 那就补足为16的倍数
    cipher = AES.new(key, AES.MODE_CBC, key)

    # 加密块大小
    block_size = AES.block_size

    # 块补齐填充
    if len(data) % block_size != 0:
        padding_size = block_size - (len(data) % block_size)
    else:
        padding_size = 0

    data += b'\0' * padding_size

    # 使用aes加密
    cipher_data = cipher.encrypt(data)

    # 二进制密文转十六进制密文
    return binascii.b2a_hex(cipher_data)


def gen_qrcode(url, file_name):
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
        box_size=10,
        # border=4,
        border=2,
    )

    hint = '''
ཆ་ཁ་བ་མཉེན་ཆས་ཕབ་ལེན
请使用chekawa程序扫描此二维码
'''.encode()

    # 加密数据
    cipher_description = hint + aes_encode(url, 'lpABEUwOvCZVEujV')
    pprint(hint)
    pprint(cipher_description)

    # 添加数据
    qr.add_data(cipher_description)

    # 填充数据
    qr.make(fit=True)

    # 生成图片
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.convert("RGB")  # RGBA

    # # 获取图片的宽高
    # img_w, img_h = img.size
    # factor = 6
    # size_w = int(img_w / factor)
    # size_h = int(img_h / factor)

    # # 添加logo
    # icon = Image.open("logo.png")

    # # 获取logo的宽高
    # icon_w, icon_h = icon.size
    # pprint(icon_w)
    # pprint(icon_h)
    #
    # if icon_w > size_w:
    #     icon_w = size_w
    # if icon_h > size_h:
    #     icon_h = size_h
    #
    # # 重新设置logo的尺寸
    # icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    # w = int((img_w - icon_w) / 2)
    # h = int((img_h - icon_h) / 2)
    # # 将logo嵌入到二维码图片中
    # img.paste(icon, (w, h), icon)

    # 显示图片
    plt.imshow(img)
    plt.show()

    # 保存图片
    img.save(file_name)
    return True


if __name__ == '__main__':
    temple_data = b'''{'temple_id':'1279'}'''

    gen_qrcode(temple_data, '01.png')
