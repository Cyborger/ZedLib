import pygame
import zedlib


class RenderWindow:
    def __init__(self):
        self.current_width = 500
        self.current_height = 500


pygame.init()
screen = pygame.display.set_mode((500, 500))
player_rect = pygame.Rect(0, 0, 25, 25)
player_image = pygame.Surface((25, 25))
player_image.fill((255, 255, 255))
test_rect = pygame.Rect(600, 200, 25, 25)
test_image = pygame.Surface((25, 25))
test_image.fill((255, 255, 255))
clock = pygame.time.Clock()
render_window = RenderWindow()
camera = zedlib.Camera(render_window, 700, 700)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_d]:
        player_rect.x += 2
    elif keys_pressed[pygame.K_a]:
        player_rect.x -= 2
    if keys_pressed[pygame.K_w]:
        player_rect.y -= 2
    elif keys_pressed[pygame.K_s]:
        player_rect.y += 2

    camera.update_target(player_rect)
    screen.fill((0, 0, 0))
    screen.blit(player_image, camera.apply_to_rect(player_rect))
    screen.blit(test_image, camera.apply_to_rect(test_rect))
    pygame.display.flip()
    clock.tick(60)
