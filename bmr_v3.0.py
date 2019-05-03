"""
    作者：zqc
    功能：BMR计算器
    版本：2.0
    日期：11/04/2019
    备注: 新加入键盘输入函数，数据类型转换函数，加入while 循环多次使用,提前使用python list功能
    3.0增加功能:
            1.用户可以在一行输入所有信息。list功能
            2.带单位的信息输出。 使用{}占位
"""

def main():
    """
        主函数：
        功能：计算BMR，加入input函数，数据类型转换函数,加入while 循环多次使用
    """
    #定义变量，数据来自键盘录入。

    y_or_n = input('是否打开程序（Y/N）？: ')

    while y_or_n != 'Y':
        # #性别
        # gender = input('性别: ')
        # print(type(gender))
        #
        # #体重（kg）
        # weight = float(input('体重(kg): '))
        # print(type(weight))
        #
        # #身高(cm)
        # height = float(input('身高: '))
        # print(type(height))
        #
        # #年龄
        # age = int(input('年龄: '))
        print("请输入一下信息，用空格隔开！")
        input_str = input("性别 体重(kg) 身高(cm) 年龄:")
        str_list = input_str.split(' ')
        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = int(str_list[3])

        if gender == '男':

            #男性
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66

        elif gender == '女':

            #女性
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print("您的性别:{},体重:{}公斤,身高:{}厘米,年龄:{}岁".format(gender,weight,height,age))
            print("您的基础代谢率:{}大卡".format(bmr))
        else:
            print("暂不支持该性别")

        print("-----------------------------------------")
        y_or_n = input('是否重新调用程序（Y/N）？: ')

    print("程序已经退出，谢谢！")

if __name__ == "__main__":
    main()