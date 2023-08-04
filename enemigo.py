import pygame
from constantes import * 
from player import *
#from plataforma import *
from auxiliar import *
 
class Enemigo(Player):
    def __init__(self,x,y,columna,fila,path) -> None:
        super().__init__(x,y,columna,fila,path)
        self.contador_derecha = 0
        self.contador_izquierda = 0
        self.izquierda = False
        self.derecha = True
        self.tiempo = 0
        self.tiempo_dos = 0
        #self.rectangulo_de_colicion= pygame.Rect(self.rect_player.x,self.rect_player.y + self.rect_player.h,self.rect_player.w,8)

#========================================================================================================================
    def movimiento_random(self,delta):
          
                if(self.tiempo >= 2300):
                    self.tiempo = 0
                    self.contador_derecha = 0
                    self.contador_izquierda = 0
                    self.izquierda = False
                    self.derecha = True
                if self.contador_derecha <= 320 and self.izquierda == False:
                    self.contador_derecha +=10
                    self.rect_player.x += 10
                    return True
                else:
                    self.izquierda = True
                    self.contador_derecha = 0
                    self.derecha = False
                
                if self.contador_izquierda <= 320 and self.derecha == False:
                    self.contador_izquierda +=10
                    self.rect_player.x -= 10
                    return False
                else:
                    self.izquierda = False
                    self.contador_izquierda = 0
#========================================================================================================================        