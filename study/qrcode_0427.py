# -*- coding: utf-8 -*-
import qrcode
#from PIL import Image #qrcodeを起動

img = qrcode.make('') #''内の文字をQRコードに変換
img.save('qr_img_cupnoodle.png') #QRコードに名前をつけて保存

img.show() #生成したQRコードを表示