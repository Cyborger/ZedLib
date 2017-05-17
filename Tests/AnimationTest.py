import ZedLib
import pygame

screen = pygame.display.set_mode((500, 500))

spritesheet = ZedLib.Spritesheet("test_spritesheet.png", 3, 3, scale=4)
normal_animation = ZedLib.Animation(spritesheet.GetHorizontalStrip(0))
delta_animation = ZedLib.DeltaAnimation(spritesheet.GetHorizontalStrip(1),
                                        500)
nonlooping_delta_animation = ZedLib.\
            DeltaAnimation(spritesheet.GetHorizontalStrip(2), 1000,
                           looping=False)

clock = pygame.time.Clock()
running = True
while running:
    delta = clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                normal_animation.IncrementFrame()
            elif event.key == pygame.K_a:
                normal_animation.DecreaseFrame()

    delta_animation.Update(delta)
    nonlooping_delta_animation.Update(delta)

    screen.blit(normal_animation.GetFrameImage(), (64, 64))
    screen.blit(delta_animation.GetFrameImage(), (128, 128))
    screen.blit(nonlooping_delta_animation.GetFrameImage(), (196, 196))

    pygame.display.flip()
