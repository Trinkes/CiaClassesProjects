# imports
import pygame
import sys

# Variables with simple values
size = width, height = 820, 600
speed = [2, 2]
black = 0, 0, 0


# functions
def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    ball = pygame.image.load("ball.png")
    ballrect = ball.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()


# classes
# class TestAgent(Agent):
class TestAgent:
    def executor(self):
        self.actor((1, 0))


# start
main()
