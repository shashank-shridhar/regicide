import pygame
from pygame.locals import *
import sys

class Player:
    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect(topleft = (30,350))
        self.gravity = 2
        self.jump_height = 20
        self.velocity = self.jump_height
        self.pos_x = self.rect.x
        self.pos_y = self.rect.y
        self.jumping = False

    def control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.move_ip(4.75,0)
        if keys[pygame.K_a]:
            if(self.rect.x > 0 or self.rect.x <=500):
                self.rect.move_ip(-4.75,0)
        if keys[pygame.K_w]:
            self.jumping = True
        if self.jumping:
            self.rect.y -= self.velocity
            self.velocity -= self.gravity
            if self.velocity == -self.jump_height:
                self.jumping = False
                self.velocity = self.jump_height
        
class GoatDemon:
    def __init__(self,image):
        self.image = image
        self.rect = self.image.get_rect(topleft = (300,300))

class Game:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 500
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        pygame.display.set_caption('KnightGame')
        self.CLOCK = pygame.time.Clock()
        self.demon = GoatDemon(self.get_image('cultist.png',24,24,1,5,None))
        self.player = Player(self.get_image('knight.png',24,24,0,3,None))
        

    def get_image(self,sheet,width,height,frame,scale,color):
        sheet = pygame.image.load(sheet).convert_alpha()
        self.image = pygame.Surface((width,height),pygame.SRCALPHA)
        self.image.blit(sheet,(0,0),((frame*width),0,width,height))
        return pygame.transform.scale(self.image, (width*scale, height*scale))

    def update(self):
        self.CLOCK.tick(60)
        pygame.display.flip()
        self.player.control()
        
        #I will probably need to call the player controls function here.

    def draw(self):
        self.screen.fill('black')
        self.screen.blit(self.player.image,self.player.rect)
        self.screen.blit(self.demon.image,self.demon.rect)

    def check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run(self):
        while True:
            self.update()
            self.draw()
            self.check()

if __name__ == '__main__':
    game = Game()
    game.run()
