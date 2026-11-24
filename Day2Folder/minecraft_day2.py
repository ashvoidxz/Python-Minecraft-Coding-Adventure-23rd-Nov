# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
# def on_on_chat():
#     pass
# player.on_chat("run", on_on_chat)

def Teleport():
    agent.teleport_to_player()

player.on_chat("come", Teleport)


def Move_Forward(steps):
    agent.move(FORWARD, steps)
player.on_chat("fw", Move_Forward)

def Move_Backward(steps):
    agent.move(BACK,steps)
player.on_chat("bk", Move_Backward)

def Move_Up(steps):
    agent.move(UP,steps)
player.on_chat("up", Move_Up)

def Move_Down(steps):
    agent.move(DOWN, steps)
player.on_chat("down", Move_Down)

def Turn_Right():
    agent.turn(RIGHT)
player.on_chat("tr", Turn_Right)

def Turn_Left():
    agent.turn(LEFT)
player.on_chat("tl", Turn_Left)

def Move_Left(steps):
    agent.move(LEFT, steps)
player.on_chat("left", Move_Left)

def Move_Right(steps):
    agent.move(RIGHT, steps)
player.on_chat("right", Move_Right)


def Obby1():
    agent.move(FORWARD, 4)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)

player.on_chat("obby1", Obby1)


def steps():
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,1)
    agent.move(UP,1)
    agent.move(FORWARD,3)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
    agent.move(FORWARD,1)
    agent.move(DOWN,1)
player.on_chat("step", steps)


def chopTrees(height):
    for i in range(height):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    
    agent.move(DOWN,height)
    agent.collect_all()
    agent.move(RIGHT,1)

player.on_chat("chop", chopTrees)

def mine(steps):
    for i in range(steps):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.move(FORWARD, 1)
        agent.collect_all()

player.on_chat("mine", mine)
