import turtle as t

robot_fn = "48.gif"
rx = []
ry = []
move_cnt = 0

def move_robot(action):
    t.clear()
    if action == 0:
        for i in range(move_cnt):
            t.goto(rx[i], ry[i])
    elif action ==1:
        for i in range(move_cnt-1, -1 ,-1):
            t.goto(rx[i], ry[i])
    elif action == 2:
        t.goto(rx[move_cnt-1], ry[move_cnt-1])
    elif action == 3:
        t.goto(rx[0], ry[0])
    t. penup()

def clicked(x, y):
    global move_cnt
    move_cnt += 1
    rx.append(x)
    ry.append(y)

def list_clear():
    global move_cnt
    del rx[1:move_cnt]
    del rx[1:move_cnt]
    move_cnt = 1

def Key_SP():
    move_robot(0)
def Key_BS():
    move_robot(1)
def Key_s():
    move_robot(2)
def Key_r():
    move_robot(3)
def key_e():
    list_clear()

t.setup(600,600)
s = t.Screen()
t.hideturtle()

s.addshape(robot_fn)
t.shape(robot_fn)
t.speed(6)
t.penup()
clicked(-265,265)
t.goto(-265,265)
t.showturtle()

s.onkey(Key_SP, "space")
s.onkey(Key_BS, "BackSpace")
s.onkey(Key_s, "s")
s.onkey(Key_r, "r")
s.onkey(key_e, "e")
s.onscreenclick(clicked)
s.listen()
                          
