"""
    作者：zqc
    功能：BMR计算器
    版本：2.0
    日期：11/04/2019
    备注: 新加入键盘输入函数，数据类型转换函数，加入while 循环多次使用
"""

def main():
    """
        主函数：
        功能：计算BMR，加入input函数，数据类型转换函数,加入while 循环多次使用
    """
    #定义变量，数据来自键盘录入。

    y_or_n = input('是否退出程序（Y/N）？: ')

    while y_or_n != 'Y':
        #性别
        gender = input('性别: ')
        print(type(gender))

        #体重（kg）
        weight = float(input('体重(kg): '))
        print(type(weight))

        #身高(cm)
        height = float(input('身高: '))
        print(type(height))

        #年龄
        age = int(input('年龄: '))

        if gender == '男':

            #男性
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66

        elif gender == '女':

            #女性
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print("基础代谢率（大卡）",bmr)
        else:
            print("暂不支持该性别")

        print("-----------------------------------------")
        y_or_n = input('是否退出程序（Y/N）？: ')

    print("程序已经退出，谢谢！")

if __name__ == "__main__":
    main()