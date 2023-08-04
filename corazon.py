import pygame
from constantes import *
from moneda import *
from plataforma import*
from enemigo import *
from auxiliar import *

class Corazon(Moneda):
    def __init__(self,x,y,ancho,alto,) -> None:
        super().__init__(x,y,ancho,alto)
        self.moneda = generar_lista_superficies(10,1,"/home/martin/Escritorio/videojuego_pygame/recursos/image__1_-removebg-preview.png")
        pass