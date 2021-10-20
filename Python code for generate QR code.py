import qrcode

img = qrcode.make('tel:1608528383u38')

print(type(img))
print(img.size)
# <class 'qrcode.image.pil.PilImage'>
# (290, 290)

img.save('data/dst/qrcode_test.png')
