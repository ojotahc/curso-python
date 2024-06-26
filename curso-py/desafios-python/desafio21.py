# a principal funcionalidade do pygame é jogo, mas dá pra fazer outras coisa...
import pygame
pygame.init()
pygame.mixer.music.load('angra.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
