#TempConvert.py
'''TempStr = input("请输入带有符号的温度值")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.3f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.4f}F".format(F))
else:
    print("输入格式错误")'''
#hello world
s=eval(input())
if s==0:
    print("Helloworld")
elif s>0:
    print("He\nll\no\nWo\nrl\nd")
else:
    for i in "Hello World":
        print(i)
