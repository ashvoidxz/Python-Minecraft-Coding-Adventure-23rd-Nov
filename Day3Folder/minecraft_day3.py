# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def buildwall(height):
    for j in range(4):
        for i in range(height):
            agent.place(FORWARD)
            agent.move(UP, 1)
        
        agent.move(DOWN, height)
        agent.move(RIGHT, 1)

player.on_chat("bw", buildwall)