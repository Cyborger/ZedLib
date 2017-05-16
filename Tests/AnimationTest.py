import ZedLib
import pygame

screen = pygame.display.set_mode((500, 500))

spritesheet = ZedLib.Spritesheet("test_spritesheet.png", 3, 3, scale=4)
normal_animation = ZedLib.Animation(spritesheet.GetHorizontalStrip(0))
delta_animation = ZedLib.Animation(spritesheet.G)
clock = pygame.time.Clock()
running = True
while running:
    delta = clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                normal_animation.animation.IncrementFrame()
            elif event.key == pygame.K_a:
                normal_animation.animation.DecreaseFrame()

    delta_animation.animation.Update(delta)
    nonlooping_delta_animation.animation.Update(delta)

    screen.blit(normal_animation_image, (64, 64))
    screen.blit(delta_animation.image, (128, 128))
    screen.blit(nonlooping_delta_animation.image, (196, 196))

    pygame.display.flip()
