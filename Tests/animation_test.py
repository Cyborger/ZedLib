import pygame
import zedlib

pygame.init()
screen = pygame.display.set_mode((500, 500))
spritesheet = zedlib.Spritesheet("test_spritesheet.png", 3, 1)
animation = zedlib.Animation(spritesheet.get_horizontal_strip(0), looping=False)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                animation.update()
            elif event.key == pygame.K_BACKSPACE:
                animation.restart()

    if animation.on_first_frame():
        print("on first frame")
    if animation.on_last_frame():
        print("on last frame")
    print("Number of frames from end: %s" % animation.frames_from_end())
    screen.fill((0, 0, 0))
    screen.blit(animation.get_current_frame(), (0, 0))
    pygame.display.flip()
