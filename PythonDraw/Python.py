#python.py
import turtle
turtle.setup(750,350,200,200)  # 绘图窗体长，宽，初始位置：x，y
turtle.penup()  # 抬起画笔
turtle.fd(-250)  # forward(d)/fd(d):直行d个像素
turtle.pendown()  # 落下画笔
turtle.pensize(10)  # 画笔宽度
turtle.pencolor("green")  # 画笔颜色
turtle.seth(-40)  # 改变前进方向，()内为倾斜角度 turtle.setheading(angle)
'''----------body----------------'''
for  i in range(2):  # snake的弯曲节数
    turtle.pencolor("green")
    turtle.circle(10,80)  # 下弧 40为弧长，80为弧的角度
    turtle.circle(-50,80)  # 上弧
#for  i in range(2):  # snake的弯曲节数
    turtle.pencolor("blue")
    turtle.circle(10,80)  # 下弧 40为弧长，80为弧的角度
    turtle.circle(-50,80)  # 上弧
#for  i in range(2):  # snake的弯曲节数
    '''turtle.pencolor("red")
    turtle.circle(10,80) #下弧 40为弧长，80为弧的角度
    turtle.circle(-50,80) #上弧'''
'''----------head----------------'''
turtle.pencolor("purple")
turtle.circle(40,80)  # neck部分下弧参数
turtle.pencolor("orange")
turtle.fd(40)         # 继续直行d个像素
turtle.pencolor("black")
turtle.circle(16,180)  # 360°为一圈，弧长16
turtle.pencolor("green")
turtle.fd(40*3/4)    # head部分长度
turtle.done()         # 停止画笔绘制，但绘图窗体不关闭
