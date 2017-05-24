import ZedLib
import pygame
import random

def GetRandomColor():
    random_red = random.randint(0, 255)
    random_green = random.randint(0, 255)
    random_blue = random.randint(0, 255)
    return (random_red, random_green, random_blue)

pygame.init()
screen_width = 400
screen_height = 400
spawn_x = screen_width / 2
spawn_y = screen_height / 2
screen = pygame.display.set_mode((screen_width, screen_height))


random.seed()
projectiles = []
image = pygame.Surface((10, 10))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        spawn_x += 5
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        spawn_x -= 5
    if pygame.key.get_pressed()[pygame.K_UP]:
        spawn_y -= 5
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        spawn_y += 5
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        random_angle = random.randint(0, 359)
        image.fill(GetRandomColor())
        new_projectile = ZedLib.AngledProjectile(image, random_angle, 4)
        new_projectile.pos.SetX(spawn_x)
        new_projectile.pos.SetY(spawn_y)
        projectiles.append(new_projectile)

    for projectile in projectiles:
        projectile.UpdateMovement()

    for projectile in projectiles:
        if (projectile.rect.x > screen_width or projectile.rect.x < 0
                or projectile.rect.y > screen_height or projectile.rect.y < 0):
            projectiles.remove(projectile)

    screen.fill((0, 0, 0))
    for projectile in projectiles:
        screen.blit(projectile.image, projectile.rect)
    pygame.display.flip()
    clock.tick(120)
