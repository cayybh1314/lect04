"""
作者：zqc
乘法计算器
"""

def jsq(b,c):
    a = b * c
    return a

def main():
    print("请输入第一个数据！")
    b = int(input())
    print("请输入第二个数据！")
    c = int(input())

    result = jsq(b,c)
    print("结果是:",result)
if __name__ == '__main__':
    main()
