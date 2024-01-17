import pygame
from pygame.locals import *
from sys import exit
import os

directory_main = os.path.dirname(__file__)
directory_images = os.path.join(directory_main, 'spriteshes')

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

BG = (50, 50, 50)
BLACK = (0, 0, 0)

sprite_sheet_img = pygame.image.load('mario sprite . 3 (2) (1).png').convert_alpha()


class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_mario = []
        for i in range(5):  # Changed to 5 frames for the jump animation
            img = sprite_sheet_img.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 5, 32 * 5))
            self.img_mario.append(img)

        self.index_list = 0
        self.image = self.img_mario[self.index_list]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)

        self.is_running = False
        self.is_jumping = False
        self.jump_count = 10  # Adjust this value to control the jump height

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[K_RIGHT]:
            self.is_running = True
            self.rect.x + 1
        else:
            self.is_running = False

        if keys[K_SPACE] and not self.is_jumping:
            self.is_jumping = True

        if self.is_running:
            if self.index_list > 3:
                self.index_list = 0
            self.index_list += 0.25
            self.image = self.img_mario[int(self.index_list)]
        elif self.is_jumping:
            self.image = self.img_mario[4]  # Display the jump frame
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10
        else:
            # Display the first frame when not running or jumping
            self.index_list = 0
            self.image = self.img_mario[self.index_list]


sprites_all = pygame.sprite.Group()
mario = Mario()
sprites_all.add(mario)

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    sprites_all.draw(screen)
    sprites_all.update()

    pygame.display.flip()