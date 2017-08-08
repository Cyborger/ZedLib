import ZedLib
import pygame

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

normal_timer = ZedLib.Timer(5000)
lapping_timer = ZedLib.LappingTimer(5000)

clock = pygame.time.Clock()

white = (255, 255, 255)
font = pygame.font.SysFont("arial", 15)
running = True
while running:
    delta = clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                normal_timer.Reset()
                lapping_timer.Reset()
            if event.key == pygame.K_DOWN:
                lapping_timer.DecreaseLaps()
    normal_timer.Update(delta)
    lapping_timer.Update(delta)
    normal_timer_label = font.render(str(normal_timer.time_passed), 1, white)
    normal_timer_max = font.render("/ " + str(normal_timer.delay), 1, white)
    normal_timer_complete = font.render(str(normal_timer.complete), 1, white)
    lapping_timer_label = font.render(str(lapping_timer.time_passed), 1, white)
    lapping_timer_max = font.render("/ " + str(lapping_timer.lap_time), 1,
                                    white)
    lapping_timer_laps = font.render(str(lapping_timer.laps_complete), 1,
                                     white)
    screen.fill((0, 0, 0))
    screen.blit(normal_timer_label, (0, 0))
    screen.blit(normal_timer_max, (50, 0))
    screen.blit(normal_timer_complete, (100, 0))
    screen.blit(lapping_timer_label, (0, 50))
    screen.blit(lapping_timer_max, (50, 50))
    screen.blit(lapping_timer_laps, (100, 50))
    pygame.display.flip()
