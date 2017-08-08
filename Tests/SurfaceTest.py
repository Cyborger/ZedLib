import ZedLib
import pygame

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

test_surface1 = ZedLib.Surface(ZedLib.LoadImage("test_image.png", scale=1), 0, 0)
test_surface2 = ZedLib.Surface(ZedLib.LoadImage("test_image.png", scale=2), 100, 100)
test_surface3 = ZedLib.Surface(ZedLib.LoadImage("test_image.png", scale=3), 200, 200)
test_surface4 = ZedLib.Surface(ZedLib.LoadImage("test_image.png", scale=4), 300, 300)
test_surface_list = [test_surface1, test_surface2, test_surface3,
                     test_surface4]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for surface in test_surface_list:
        screen.blit(surface.image, surface.rect)
    pygame.display.flip()
