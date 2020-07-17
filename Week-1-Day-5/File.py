# 读文件
def read():
    with open('test.txt', encoding='UTF-8') as f:
        print(f.read())

# 写文件
def write():
    with open('test.txt', mode='w', encoding="UTF-8") as f:
        f.write('hahaha\n')

# 追加
def append():
    with open('test.txt', mode='a', encoding="UTF-8") as f:
        f.write('Hello, World!\n')
        f.write('Hello, World!')

# 读写图片
def read_image():
    f1 = open('one.png', mode='rb')
    f2 = open('two.png', mode='wb')
    content = f1.read()
    f2.write(content)
    f1.close()
    f2.close()

if __name__ == "__main__":
    read_image()
