import pygame
pygame.init()
pygame.mixer_music.load('music.mp3')
pygame.mixer_music.play()
pygame.event.wait()