# -*- coding: utf-8 -*-
from sys import argv
#将argv参数分包
script,filename = argv**
#打开指定文件，将内容返回给txt
txt = open(filename)
#打印文件名
print "Here's your file %r:" % filename
#txt的read方法，打印txt的文件内容
print txt.read()

print "Type the filename again:"
#显示提示符，输入文件名赋值给file_again
file_again
#打开指定文件，将内容返回给txt_again
txt_again = open(file_again)
#txt_again的read方法，打印txt_again的文件内容
print txt_again.read()
