import pygame
from constantes import * 
from player import *
from auxiliar import *

#===============================================================================================================================
class Player:
    def __init__(self,x,y,columnas,filas,path,) -> None:
        self.movimiento_derecha_player= generar_lista_superficies(columnas,filas,PATH_RECUSRSOS+path)
        self.movimiento_izquierda_player = generar_lista_superficies(columnas,filas,PATH_RECUSRSOS+path,True)
        self.movimiento_saltar_player = generar_lista_superficies(33,1,"/home/martin/Escritorio/videojuego_pygame/recursos/green_hat/jump.png")
        self.movimiento_saltar_player_izquierda = generar_lista_superficies(33,1,"/home/martin/Escritorio/videojuego_pygame/recursos/green_hat/jump.png",True)
        self.quieto_player = generar_lista_superficies(16,1,"/home/martin/Escritorio/videojuego_pygame/recursos/green_hat/idle.png")
        self.index_player_derecha = 0
        self.index_player_izquierda = 0
        self.index_quieto = 0
        self.index_salta_derecha = 0
        self.index_salta_izquierda = 0 
        self.imagen_player_a_mostrar = self.movimiento_derecha_player[self.index_player_derecha]
        self.rect_player = self.imagen_player_a_mostrar.get_rect()
        self.rect_player.x = x
        self.rect_player.y = y
        self.vidas_player = 5
        self.monedas_player = 0
        self.tiempo = 0
        self.segundo_salto = True
        self.direccion_player = True
        self.tiempo_quieto = 0
        self.tiempo_espera_quieto = 0
        self.acumulador_saltador = 0
        self.tiempo_salto = 0
        self.saltando = False
        self.saltando = False
        self.gravedad_player= True
        self.rectangulo_de_colicion = pygame.Rect(self.rect_player.x + 25 ,self.rect_player.y +self.rect_player.h -8,self.rect_player.w / 2,8)
        self.frecuencia_caminar = 60
        self.columnas = columnas
        self.filas = filas
        self.numero_imagenes = 11
        #==============DISPARO===========================================
        # self.disparo = generar_lista_superficies(8,1,"/home/martin/Escritorio/videojuego_pygame/recursos/disparo_azul-removebg-preview.png")
        # #self.rect_moneda = self.moneda.get_rect()
        # self.index = 0
        # self.imagen_a_mostrar_disparo = self.disparo[self.index]
        # self.rect_disparo = self.imagen_a_mostrar.get_rect()
        # self.rect_disparo.x = x
        # self.rect_disparo.y = y
        # self.tiempo_comienzo = 0
        # self.ancho = 25
        # self.alto = 25
        # self.rectangulo_de_colicion_disparo = pygame.Rect(self.rect_disparo.x,self.rect_disparo.y ,self.ancho,self.alto)
        
#===============================================================================================================================
    def caminar_player(self,delta,direccion:bool=True):
        self.tiempo += delta
        self.tiempo_espera_quieto = 0
        self.index_quieto = 0
        self.rectangulo_de_colicion.x = self.rect_player.x + 25
        self.rectangulo_de_colicion.y = self.rect_player.y +self.rect_player.h -8
        if direccion == True:
            self.direccion_player = True
            self.index_player_izquierda = 0
            if self.tiempo >= self.frecuencia_caminar:
                self.tiempo = 0 
                self.imagen_player_a_mostrar = self.movimiento_derecha_player[self.index_player_derecha]
                self.index_player_derecha += 1
                self.rect_player.x += 5
            if self.index_player_derecha >= self.numero_imagenes:   
                self.index_player_derecha = 0
        else:
             self.direccion_player = False
             self.index_player_derecha = 0
             if self.tiempo >= self.frecuencia_caminar:
                self.tiempo = 0 
                self.imagen_player_a_mostrar = self.movimiento_izquierda_player[self.index_player_izquierda]
                self.index_player_izquierda += 1
                self.rect_player.x -= 5
             if self.index_player_izquierda >=self.numero_imagenes :
                 self.index_player_izquierda  = 0
#===============================================================================================================================
    def saltar_player(self,delta):
                
                    if self.segundo_salto == True: 
                        self.rect_player.y -= int(self.rect_player.h * 1.8)
                        if self.direccion_player == True:
                            self.imagen_player_a_mostrar = self.movimiento_saltar_player[self.index_salta_derecha]
                            self.index_salta_derecha += 1
                            if self.index_salta_derecha >= 32:
                                self.index_salta_derecha == 0
                            self.rect_player.x += 30
                        else:
                            self.imagen_player_a_mostrar = self.movimiento_saltar_player_izquierda[self.index_salta_izquierda]
                            self.index_salta_izquierda += 1
                            if self.index_salta_derecha >= 32:
                                self.index_salta_izquierda == 0
                                self.rect_player.x -= 30
                        self.rectangulo_de_colicion.x = self.rect_player.x + 25
                        self.rectangulo_de_colicion.y = self.rect_player.y +self.rect_player.h -8
#===============================================================================================================================
    def gravedad(self):
        self.rectangulo_de_colicion.x = self.rect_player.x + 25
        self.rectangulo_de_colicion.y = self.rect_player.y +  self.rect_player.h -8
        if self.rect_player.y < 470 and self.gravedad_player == True:
             self.segundo_salto = False
             self.rect_player.y += 8
             if self.direccion_player == True :
                  self.rect_player.x += 2
             if self.direccion_player == False :
                    self.rect_player.x -= 2
        else:
            self.segundo_salto = True
#===============================================================================================================================
    def quieto(self,delta):
        self.tiempo_espera_quieto += delta
        self.imagen_player_a_mostrar = self.quieto_player[self.index_quieto]
        if self.tiempo_espera_quieto >=3000:
            self.tiempo_quieto += delta
            if self.tiempo_quieto >= 80:
                self.tiempo_quieto = 0
                self.imagen_player_a_mostrar = self.quieto_player[self.index_quieto]
                self.index_quieto += 1
            if self.index_quieto >= 15:
                self.index_quieto = 0
        self.rectangulo_de_colicion.x = self.rect_player.x + 25
        self.rectangulo_de_colicion.y = self.rect_player.y +self.rect_player.h -8
#===============================================================================================================================
    # def disparar(self,delta):
    #     self.rect_disparo.x += 5
    #     self.imagen_a_mostrar_disparo = self.disparo[self.index]
    #     self.index += 1
    #     if(self.index >= 7):
    #         self.index = 1
         
    #     pass
#===============================================================================================================================
    def dibujar_player(self,screen):
        if DEBUG:
             pygame.draw.rect(screen,ROJO,self.rect_player)
             pygame.draw.rect(screen,VERDE,self.rectangulo_de_colicion)
        screen.blit(self.imagen_player_a_mostrar,self.rect_player)
       
        