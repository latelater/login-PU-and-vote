# read.py

# file_object = open('number.txt', 'rb')
#读每行
# list_of_all_the_lines = file_object.readlines( )

#如果文件是文本文件，还可以直接遍历文件对象获取每行：

# for line in list_of_all_the_lines:
#     print(line)
#  


file_object = open('number.txt', 'rb')
try:
    while True:
        chunk = file_object.read(9)
        if not chunk:
            break
        print(chunk)
        chunk1 = str(chunk)
        print(type(chunk1))
        # do_something_with(chunk)
finally:
    file_object.close( )