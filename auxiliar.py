import pygame
def generar_lista_superficies(columnas,filas,path,direccion_caminar = False):
    lista = []
    superficie = pygame.image.load(path)
    fotograma_ancho = int(superficie.get_width()/columnas)
    fotograma_alto = int(superficie.get_height() /filas)
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            superficie_fotograma = superficie.subsurface(x,y,fotograma_ancho,fotograma_alto)
            if (direccion_caminar == True):
                superficie_fotograma = pygame.transform.flip(superficie_fotograma,True,False)
            # superficie_fotograma = pygame.transform.scale(superficie_fotograma,(100,100))
            lista.append(superficie_fotograma)
    return lista
def getSurfaceFromSeparateFiles(path_format,from_index,quantity,flip=False,step = 1,scale=1,w=0,h=0,repeat_frame=1):
        lista = []
        for i in range(from_index,quantity+from_index):
            path = path_format.format(i)
            surface_fotograma = pygame.image.load(path)
            fotograma_ancho_scaled = int(surface_fotograma.get_rect().w * scale)
            fotograma_alto_scaled = int(surface_fotograma.get_rect().h * scale)
            if(scale == 1 and w != 0 and h != 0):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(w, h)).convert_alpha()
            if(scale != 1):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(fotograma_ancho_scaled, fotograma_alto_scaled)).convert_alpha() 
            if(flip):
                surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
            
            for i in range(repeat_frame):
                lista.append(surface_fotograma)
        return lista