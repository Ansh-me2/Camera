import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((600,480))
screen.fill((255,255,255))

camlist = pygame.camera.list_cameras()
if camlist:
    cam = pygame.camera.Camera(camlist[0],(640,480))

cam.start()
image = cam.get_image()

screen.blit(image , (0,0))
pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.flip()

