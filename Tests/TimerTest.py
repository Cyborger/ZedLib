import ZedLib
import pygame

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

normal_timer = ZedLib.Timer(2000)
lapping_timer = ZedLib.LappingTimer(2000)

clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 15)
running = True
while running:
    delta = clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    normal_timer.Update(delta)
    lapping_timer.Update(delta)
    normal_timer_label = font.render(str(normal_timer.time_passed), 1, (255, 255, 255))
    normal_timer_max = font.render("/ " + str(normal_timer.delay), 1, (255, 255, 255))
    normal_timer_complete = font.render(str(normal_timer.complete), 1, (255, 255, 255))
    lapping_timer_label = font.render(str(lapping_timer.time_passed), 1, (255, 255, 255))
    lapping_timer_max = font.render("/ " + str(lapping_timer.lap_time), 1, (255, 255, 255))
    lapping_timer_laps = font.render(str(lapping_timer.laps_complete), 1, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(normal_timer_label, (0, 0))
    screen.blit(normal_timer_max, (50, 0))
    screen.blit(normal_timer_complete, (100, 0))
    screen.blit(lapping_timer_label, (0, 50))
    screen.blit(lapping_timer_max, (50, 50))
    screen.blit(lapping_timer_laps, (100, 50))
    pygame.display.flip()
