try:
    file=open("../Common/a.txt","r")
    # 如果要是用read
    # 需要做以下注意：
    print(file.read(1024))
    file.close()
except:
    print("读取文件失败！")
finally:
    file.close()

with open("../Common/a.txt","r",encoding="utf-8") as file:
    print(file.read(1024))