import pygame
from constantes import *
from moneda import *
from plataforma import*
from enemigo import *
from auxiliar import *
from random import * 

class Lluvia:
    def __init__(self,x,ancho,alto,path) -> None:
        self.lluvia = generar_lista_superficies(1,1,path)
        self.lluvia_imagen = self.lluvia[0]
        self.lluvia_imagen= pygame.transform.scale(self.lluvia_imagen,(25,25))
        self.rect_lluvia = self.lluvia_imagen.get_rect()
        self.rect_lluvia.x = x
        self.rect_lluvia.y = 0
    def movimiento_lluvia(self):
        self.rect_lluvia.y += 5

    def dibujar_lluvia(self,screen):
        if DEBUG:
             pygame.draw.rect(screen,ROJO,self.rect_lluvia)
        screen.blit(self.lluvia_imagen,self.rect_lluvia)
       
        
def generar_lluvia(posicio_x):
    lista_lluvia = []
    lista_lluvia.append(Lluvia(posicio_x,10,10,PATH_RECUSRSOS + "gota-acido-removebg-preview.png"))
    return lista_lluvia
    pass