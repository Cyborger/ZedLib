import ZedLib
import pygame

screen = pygame.display.set_mode((500, 500))

spritesheet = ZedLib.Spritesheet("test_spritesheet.png", 3, 3, 4)
vertical_frames = spritesheet.GetVerticalStrip(0)
horizontal_frames = spritesheet.GetHorizontalStrip(1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for frame in vertical_frames:
        screen.blit(frame, (64, vertical_frames.index(frame) * 64))

    for frame in horizontal_frames:
        screen.blit(frame, (192 + horizontal_frames.index(frame) * 64, 64))

    pygame.display.flip()
