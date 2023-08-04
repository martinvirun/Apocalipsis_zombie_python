import pygame
from constantes import *
from player import *
from auxiliar import *


class Plataforma:
    def __init__(self,x,y,ancho,alto,path) -> None:
        self.plataforma = generar_lista_superficies(1,1,path)
        self.plataforma = pygame.transform.scale(self.plataforma[0],(ancho,alto))
        self.rect_plataforma = self.plataforma.get_rect()
        self.rect_plataforma.x = x
        self.rect_plataforma.y = y
        self.rectangulo_de_colicion_plataforma = pygame.Rect(self.rect_plataforma.x,self.rect_plataforma.y + 7,self.rect_plataforma.w,8)
        pass
    def dibujar(self,screen):
        if DEBUG:
             pygame.draw.rect(screen,VERDE,self.rectangulo_de_colicion_plataforma)
        screen.blit(self.plataforma,self.rect_plataforma)
        
    