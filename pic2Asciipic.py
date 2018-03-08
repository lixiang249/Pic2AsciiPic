# -*- coding: utf-8 -*-

from PIL import Image
import sys


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")


def get_char(r, g, b, alpha=256):
    """
    用于返回rgb三原色所对应的灰度值，返回对应灰度值的字符
    :param r:
    :param g:
    :param b:
    :param alpha:
    :return:
    """
    if alpha == 0:
        return " "
    length = len(ascii_char)
    gray = (2126 * r + 7152 * g + 722 * b) / 10000

    # gray / (256+1) = index / length
    index = int((gray / (256 + 1.0)) * length)
    return ascii_char[index]


def write2file(file_name, content):
    """
    将字符图片写入到文件中进行保存
    :param file_name:
    :param content:
    :return:
    """
    with open(file_name, "w") as f:
        f.write(content)


def main(file_name="../wm.png", width=80, height=50, output_file="../output.txt"):
    text = ""
    im = Image.open(file_name).resize((width, height), Image.NEAREST)  # Image.NEAREST指示图片质量
    for i in range(height):
        for j in range(width):
            content = im.getpixel((j, i))  # 返回指定位置的像素，如果所打开的图像是多层次的图片，那这个方法就返回一个元组。
            text += get_char(*content)  # *表示解包的意思，分别将元组分解为单个变量
        text += "\n"
    write2file(output_file, text)


if __name__ == "__main__":
    main()
