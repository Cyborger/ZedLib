import pygame


class Camera:
    """ A camera that follows a given rect """
    def __init__(self, screen_size, location_width=1, location_height=1):
        self.rect = pygame.Rect(0, 0, location_width, location_height)
        self.screen_width = 0
        self.screen_height = 0
        self.half_screen_width = 0
        self.half_screen_height = 0
        self.update_screen_size(screen_size)

    def apply(self, rect):
        """ Returns rect at an offset based on camera position """
        return rect.move(self.rect.left, self.rect.top)

    def update_location_size(self, location_width, location_height):
        """ Updates dimensions of the current location """
        self.rect.width = location_width
        self.rect.height = location_height

    def update_screen_size(self, screen_size):
        """ Update the dimensions used to calculate offsets """
        self.screen_width = screen_size[0]
        self.screen_height = screen_size[1]
        self.half_screen_width = screen_size[0]/2
        self.half_screen_height = screen_size[1]/2

    def update_target(self, rect):
        """ Update the rect the camera is following """
        left, top, _, _ = rect
        _, _, width, height = self.rect
        left = -left + self.half_screen_width
        top = -top + self.half_screen_height

        left = min(0, left)
        left = max(-(self.rect.width - self.screen_width), left)

        top = max(-(self.rect.height - self.screen_height), top)
        top = min(0, top)

        self.rect = pygame.Rect(left, top, width, height)
        self.handle_undersized_location()

    def handle_undersized_location(self):
        """ Centers the location if map size is smaller than screen """
        if self.rect.width < self.render_window.current_width:
            x = (self.render_window.current_width - self.rect.width) / 2
            self.rect.x = x

        if self.rect.height < self.render_window.current_height:
            y = (self.render_window.current_height - self.rect.height) / 2
            self.rect.y = y
