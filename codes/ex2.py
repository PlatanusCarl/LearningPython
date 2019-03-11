#ex2--依然是温度转换
temp = input()
if temp[-1] in ['c','C']:
    print("{:.2f}F".format(eval(temp[0:-1])*1.8 +32))
elif temp[-1] in ['F','f']:
    print("{:.2f}C".format((eval(temp[0:-1]) - 32)/1.8))
else:
    print("输入格式错误")
