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
    mouse_state = pygame.mouse.get_pressed()
    left_mouse_button_pressed = mouse_state[0]
    mouse_pos = pygame.mouse.get_pos()
    button.Update(mouse_pos, left_mouse_button_pressed)
    screen.fill((0, 0, 0))
    screen.blit(button.image, button.rect)
    pygame.display.flip()
