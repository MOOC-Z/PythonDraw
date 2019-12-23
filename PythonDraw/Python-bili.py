#Python-bili.py
import turtle
'''------wai------'''
#turtle.setup(200,200)
turtle.pendown()
turtle.pencolor("pink")
turtle.pensize(10)
turtle.fd(210)
turtle.seth(-90)
turtle.fd(200)
turtle.seth(-180)
turtle.fd(210)
turtle.seth(-270)
turtle.fd(200)

'''------'''
turtle.penup()
turtle.seth(-40)
turtle.fd(34.5)
turtle.down()
'''----nei----'''
turtle.seth(0)
turtle.fd(155)
turtle.seth(-90)
turtle.fd(150)
turtle.seth(-180)
turtle.fd(155)
turtle.seth(-270)
turtle.fd(150)

'''------'''
turtle.penup()
turtle.seth(-45)
turtle.fd(75)
'''---face---'''
turtle.down()
turtle.seth(-120)
turtle.fd(30)

turtle.penup()
turtle.seth(0)
turtle.fd(75)
turtle.pendown()
turtle.seth(-240)
turtle.fd(30)

turtle.penup()
turtle.seth(-90)
turtle.fd(50)
turtle.down()
turtle.seth(-130)
turtle.circle(-15,80) #下弧 40为弧长，80为弧的角度
turtle.circle(5,90) #上弧
turtle.seth(-150)
turtle.circle(-15,80) #下弧 40为弧长，80为弧的角度
'''------'''
turtle.penup()
turtle.seth(-270)#shang
turtle.fd(140)
turtle.down()
turtle.seth(-250)
turtle.fd(50)

turtle.penup()
turtle.seth(0)
turtle.fd(100)
turtle.down()
turtle.seth(-115)
turtle.fd(50)
turtle.done()
