import random
import pygame
pygame.init()
screen=pygame.display.set_mode((800,547))
bg=pygame.image.load("images/bg.jpg")
while True:
    screen.blit(bg,(0,0))
    pygame.display.update()
