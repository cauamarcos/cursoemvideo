#codigo para tocar uma música baixada
import pygame

pygame.mixer.init ()
pygame.mixer.music.load () #aqui entra o nome do arquivo da música
pygame.mixer.music.play ()
pygame.event.wait ()
