import pygame
import sys
from constantes import *
from moneda import *
from plataforma import*
from enemigo import *
from auxiliar import *
# from main import *

class Disparo():
    def __init__(self,x,y) -> None:
        self.disparo = generar_lista_superficies(8,1,"/home/martin/Escritorio/videojuego_pygame/recursos/disparo_azul-removebg-preview.png")
        #self.rect_moneda = self.moneda.get_rect()
        self.index = 0
        self.imagen_a_mostrar = self.disparo[self.index]
        self.rect_disparo = self.imagen_a_mostrar.get_rect()
        self.rect_disparo.x = x
        self.rect_disparo.y = y
        self.tiempo_comienzo = 0
        self.ancho = 25
        self.alto = 25
        self.rectangulo_de_colicion_disparo = pygame.Rect(self.rect_disparo.x,self.rect_disparo.y ,self.ancho,self.alto)
    def movimiento_disparo(self,delta):

        self.rect_disparo.x += 5
        self.imagen_a_mostrar = self.disparo[self.index]
        self.index += 1
        if(self.index >= 7):
            self.index = 1
    def dibujar_disparo(self,screen):
        # if DEBUG:
        #      pygame.draw.rect(screen,ROJO,self.rect_disparo)
        screen.blit( self.imagen_a_mostrar,self.rect_disparo)