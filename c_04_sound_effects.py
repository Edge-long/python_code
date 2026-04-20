import pygame

# 初始化模块mixer
pygame.mixer.init()

# 定义两个声音，并将声音文件的路径作为唯一的参数
bullet_sound = pygame.mixer.Sound('sounds/laser1.wav')
alien_sound = pygame.mixer.Sound('sounds/Explosion2.wav')