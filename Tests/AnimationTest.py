import ZedLib
import pygame

class AnimatedSprite1:
    def __init__(self):
        self.spritesheet = ZedLib.Spritesheet("test_spritesheet.png",
                                              3, 3, scale=4)
        strip = self.spritesheet.GetHorizontalStrip(0)
        self.animation = ZedLib.Animation(self, strip, looping=False)
        self.image = self.animation.frames[0]

class AnimatedSprite2:
    def __init__(self):
        self.spritesheet = ZedLib.Spritesheet("test_spritesheet.png",
                                              3, 3, scale=4)
        strip = self.spritesheet.GetHorizontalStrip(1)
        self.animation = ZedLib.DeltaAnimation(self, strip, 500, looping=True)
        self.image = self.animation.frames[0]

class AnimatedSprite3:
    def __init__(self):
        self.spritesheet = ZedLib.Spritesheet("test_spritesheet.png",
                                              3, 3, scale=4)
        strip = self.spritesheet.GetHorizontalStrip(2)
        self.animation = ZedLib.DeltaAnimation(self, strip, 2000, looping=False)
        self.image = self.animation.frames[0]

screen = pygame.display.set_mode((500, 500))

normal_animation = AnimatedSprite1()
delta_animation = AnimatedSprite2()
nonlooping_delta_animation = AnimatedSprite3()

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

    screen.blit(normal_animation.image, (64, 64))
    screen.blit(delta_animation.image, (128, 128))
    screen.blit(nonlooping_delta_animation.image, (196, 196))

    pygame.display.flip()
