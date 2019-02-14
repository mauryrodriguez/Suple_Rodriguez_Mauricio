import pygame


pygame.init()
pantalla=pygame.display.set_mode((480,300))   ##tamaño de la pantalla
salir=False
reloj1=pygame.time.Clock()
fuente1=pygame.font.Font(None,68)
texto1=fuente1.render("MAURICIO",0,(220,250,245))  ##fuente de la letra color

while salir!=True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir=True

    reloj1.tick(15)
    pantalla.fill((30,30,200))
    pantalla.blit(texto1,(100,100))     ##posiciones horizontal y vertical
    pygame.display.update()
    
pygame.quit()
