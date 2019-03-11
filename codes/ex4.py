#ex4--汇率转换
cash = input()
if cash[0] == 'R':
    print("USD{:.2f}".format(eval(cash[3:])/6.78))
else:
    print("RMB{:.2f}".format(eval(cash[3:])*6.78))
