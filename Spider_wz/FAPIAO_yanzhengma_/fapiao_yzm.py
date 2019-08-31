import tesserocr
from PIL import Image
image = Image.open('D:/YZM/1.jpg')
result = tesserocr.image_to_text(image)
print(result)
# image = Image.open('D:/YZM/1.jpg')
# image = image.convert('L')  # 将图像转化为灰度图像
# image.show()
# image = image.convert('1')  # 将图像转化为二值化图像，二值化阈值默认是127
#
# # 现将图片转化成灰度图像，再转化成二值化图像
# image = image.convert('L')
# threshold = 80  # 设定阈值
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# image = image.point(table, '1')
# image.show()  # 图像变得清晰
# result = tesserocr.image_to_text(image)
# print(result)