import ZedLib
import pygame

screen = pygame.display.set_mode((500, 500))
spritesheet = ZedLib.Spritesheet("test_spritesheet.png", 3, 3, 2)
button = ZedLib.Button(spritesheet.GetVerticalStrip(0))
button.SetPosition(100, 100)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("mouse clicked")
            button.CheckPress()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            button.CheckRelease()
    mouse_pos = pygame.mouse.get_pos()
    button.Update(mouse_pos)
    screen.fill((0, 0, 0))
    screen.blit(button.image, button.rect)
    pygame.display.flip()
