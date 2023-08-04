import pygame
from constantes import * 
from player import *
from auxiliar import *
class Moneda:

    def __init__(self,x,y,ancho,alto) -> None:
        self.moneda = generar_lista_superficies(10,1,"/home/martin/Escritorio/videojuego_pygame/recursos/image-removebg-preview.png")
        #self.rect_moneda = self.moneda.get_rect()
        self.index = 0
        self.imagen_a_mostrar = self.moneda[self.index]
        self.rect_moneda = self.imagen_a_mostrar.get_rect()
        self.rect_moneda.x = x
        self.rect_moneda.y = y
        self.tiempo_comienzo = 0
        self.ancho = ancho
        self.alto = alto
        self.rectangulo_de_colicion_monedas = pygame.Rect(self.rect_moneda.x,self.rect_moneda.y ,ancho,alto)
#========================================================================================================================
    def mostrar(self,delta):
        self.tiempo_comienzo = self.tiempo_comienzo + delta
        if(self.tiempo_comienzo >= 120):
            self.tiempo_comienzo = 0
            self.imagen_a_mostrar = self.moneda[self.index]
            self.index +=1    
            if(self.index >= 9):
                self.index =0
#========================================================================================================================
    def dibujar(self,screen):
        if DEBUG:
             pygame.draw.rect(screen,VERDE,self.rectangulo_de_colicion_monedas)
        screen.blit(pygame.transform.scale(self.imagen_a_mostrar,(self.ancho,self.alto)),self.rect_moneda)
        

        pass