import pygame
from pygame.locals import *
import sys

class Player:
    def __init__(self,image):
        self.image = image
        

class Game:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 600
        self.SCREEN_HEIGHT = 600
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        pygame.display.set_caption('KnightGame')
        self.CLOCK = pygame.time.Clock()
        

    def get_image(self,sheet,width,height,frame,scale,color):
        sheet = pygame.image.load(sheet).convert_alpha()
        self.image = pygame.Surface((width,height),pygame.SRCALPHA)
        self.image.blit(sheet,(0,0),((frame*width),0,width,height))
        return pygame.transform.scale(self.image, (width*scale, height*scale))

    def update(self):
        self.CLOCK.tick(60)
        pygame.display.flip()
        
        #I will probably need to call the player controls function here.

    def draw(self):
        self.SCREEN.fill('black')
        self.player = Player(self.get_image('knight.png',24,24,0,3,None))
        self.SCREEN.blit(self.player.image,(30,30))

    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.quit()

    def run(self):
        while True:
            self.update()
            self.draw()
            self.check()



if __name__ == '__main__':
    game = Game()
    game.run()
