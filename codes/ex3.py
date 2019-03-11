#ex3--数字形式转换
numbers = input()
for num in numbers:
    if num == '1':
        num = '一'
    if num == '2':
        num = '二'
    if num == '3':
        num = '三'
    if num == '4':
        num = '四'
    if num == '5':
        num = '五'
    if num == '6':
        num = '六'
    if num == '7':
        num = '七'
    if num == '8':
        num = '八'
    if num == '9':
        num = '九'
    if num == '0':
        num = '零'
    print(num,end='')
