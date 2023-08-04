import pygame
import sys
from constantes import *
from moneda import *
from plataforma import*
from enemigo import *
from auxiliar import *
from lluvia import *
import random 
from corazon import*
from disparo import *
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
juego_corriendo = True
clock = pygame.time.Clock()
imagen = pygame.image.load(PATH_RECUSRSOS+"recursos_de_fondo/1_game_background.png")
imagen = pygame.transform.scale(imagen,(ANCHO_VENTANA,ALTO_VENTANA))
#========================================================================================================================
lluvia = Lluvia(50,10,10,PATH_RECUSRSOS + "gota-acido-removebg-preview.png")
#========================================================================================================================

#========================================================================================================================

moneda = Moneda(850,450,ANCHO_MONEDA,ALTO_MONEDA)
moneda_dos = Moneda(950,450,ANCHO_MONEDA,ALTO_MONEDA)
moneda_tre = Moneda(1050,450,ANCHO_MONEDA,ALTO_MONEDA)
moneda_cuatro = Moneda(600,250,ANCHO_MONEDA,ALTO_MONEDA)
moneda_cinco = Moneda(700,250,ANCHO_MONEDA,ALTO_MONEDA)
moneda_seis = Moneda(800,250,ANCHO_MONEDA,ALTO_MONEDA)
lista_monedas = [moneda,moneda_dos,moneda_tre,moneda_cuatro,moneda_cinco,moneda_seis]
#========================================================================================================================
madera = Plataforma(850,400,250,50,"/home/martin/Escritorio/videojuego_pygame/recursos/recursos_de_fondo/bloque_De_madera.png")
madera_dos = Plataforma(600,300,250,50,"/home/martin/Escritorio/videojuego_pygame/recursos/recursos_de_fondo/bloque_De_madera.png")
madera_tres = Plataforma(300,250,250,50,"/home/martin/Escritorio/videojuego_pygame/recursos/recursos_de_fondo/bloque_De_madera.png")
lista_madera = [madera,madera_dos,madera_tres]
#========================================================================================================================
personaje_principal = Player(50,470,15,1,"green_hat/walk.png")
boton_derecho_apretado = False
boton_izquierdo_apretado = False
enemigo_uno = Enemigo(300,510,5,1,"zoombie_completo-removebg-preview.png")
tiempo_enemigo = 0
rect1 = personaje_principal
rect1 = madera
tiempo_captura_monedas = 0 
lluvia_tiempo = 0
lluvia_tiempo2 = 0
lista_lluvia  = []
lista_lluvia_dos = []
contador = 0
cont = 0
flag = False
#========================================================================================================================
disparo = Disparo(personaje_principal.rect_player.x,personaje_principal.rect_player.y)
corazon = Corazon(320,180,45,45)
while juego_corriendo:
    delta = clock.tick(FPS)
    tiempo_enemigo += delta
    lluvia_tiempo = delta
    lluvia_tiempo2 += delta
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                juego_corriendo = False
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
               boton_derecho_apretado = True
            if event.key == pygame.K_LEFT:
               boton_izquierdo_apretado =True
            if event.key == pygame.K_SPACE:
                 personaje_principal.saltar_player(delta )        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                boton_izquierdo_apretado = False
            if event.key == pygame.K_RIGHT:
                boton_derecho_apretado = False
            
                  
    if personaje_principal.rectangulo_de_colicion.colliderect(madera.rectangulo_de_colicion_plataforma) or personaje_principal.rectangulo_de_colicion.colliderect(madera_dos.rectangulo_de_colicion_plataforma) or personaje_principal.rectangulo_de_colicion.colliderect(madera_tres.rectangulo_de_colicion_plataforma):
           personaje_principal.gravedad_player = False
    else:
           personaje_principal.gravedad_player = True
    
    if boton_derecho_apretado == True and boton_izquierdo_apretado == True:
         personaje_principal.quieto(delta)
         boton_derecho_apretado = False
         boton_izquierdo_apretado = False
    if boton_derecho_apretado == True:
            personaje_principal.caminar_player(delta)
            pass
    if boton_izquierdo_apretado == True:
            personaje_principal.caminar_player(delta,False)
    if boton_derecho_apretado == False and boton_izquierdo_apretado == False:
         personaje_principal.quieto(delta)
    if personaje_principal.vidas_player <= 0:
         juego_corriendo = False
    screen.blit(imagen,(0,0))
    corazon.dibujar(screen)
    corazon.mostrar(delta)
    for i in range(0,3):
       lista_madera[i].dibujar(screen)
   
    for i in range(0,len(lista_monedas )):
         lista_monedas[i].dibujar(screen)
         lista_monedas[i].mostrar(delta)
         if lista_monedas[i].rectangulo_de_colicion_monedas.colliderect(personaje_principal.rect_player):
              tiempo_captura_monedas += delta
              print(i)
              if tiempo_captura_monedas >= 1000:
                    tiempo_captura_monedas = 0
                    personaje_principal.monedas_player +=1
    personaje_principal.dibujar_player(screen)
    enemigo_uno.dibujar_player(screen)
    if lluvia_tiempo2 >=2000:
          cont +=1
          contador +=1
          lluvia_tiempo2 = 0
          lista_lluvia.append(generar_lluvia(random.randint(1, ANCHO_VENTANA))[0]) 
          lista_lluvia_dos.append(generar_lluvia(random.randint(1, ANCHO_VENTANA)/2)[0]) 
    if cont >=1:
          lista_lluvia[contador-1].movimiento_lluvia()
          lista_lluvia[contador-1].dibujar_lluvia(screen) 
          lista_lluvia_dos[contador-1].movimiento_lluvia()
          lista_lluvia_dos[contador-1].dibujar_lluvia(screen) 
         
    if(tiempo_enemigo >= 150):
         enemigo_uno.frecuencia_caminar = 150
         enemigo_uno.numero_imagenes = 5
         enemigo_uno.caminar_player(tiempo_enemigo,enemigo_uno.movimiento_random(delta))
         tiempo_enemigo = 0
    personaje_principal.gravedad()
    

    pygame.display.flip()
pygame.quit()