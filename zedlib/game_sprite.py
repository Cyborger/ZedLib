import zedlib
import pygame
import math


class GameSprite:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.position = zedlib.Position(x, y)
        self.x_acceleration = 0.0
        self.y_acceleration = 0.0
        self.x_velocity = 0.0
        self.y_velocity = 0.0
        self.max_y_velocity = None
        self.max_x_velocity = None
        self.move_x = 0.0
        self.move_y = 0.0

        self.update_rect_x()
        self.update_rect_y()

    def draw(self, surface, camera = None):
        """ Draw image on a given surface, a zedlib.Camera can also be used """
        if camera:
            surface.blit(self.image, camera.apply(self.rect))
        else:
            surface.blit(self.image, self.rect)

    def update_rect_x(self):
        """ Update x position of the rect, from self.position """
        self.rect.x = self.position.get_position()[0]

    def update_rect_y(self):
        """ Update y position of the rect, from self.position """
        self.rect.y = self.position.get_position()[1]

    def update_movement(self, collisions=[]):
        """ Update the position of rect and handle collisions """
        self.apply_acceleration()

        if self.move_x and self.move_y:
            movement = self.get_diagonal_movement(math.fabs(self.move_x))
            self.move_x = math.copysign(movement[0], self.move_x)
            self.move_y = math.copysign(movement[1], self.move_y)

        self.move_x += self.x_velocity
        self.position.move_x(self.move_x)
        self.handle_horizonal_collisions(collisions)
        self.move_x = 0.0

        self.move_y += self.y_velocity
        self.position.move_y(self.move_y)
        self.handle_vertical_collisions(collisions)
        self.move_y = 0.0

    def apply_acceleration(self):
        self.x_velocity += self.x_acceleration
        self.y_velocity += self.y_acceleration
        if self.max_x_velocity:
            if self.x_velocity > self.max_x_velocity:
                self.x_velocity = self.max_x_velocity
        if self.max_y_velocity:
            if self.y_velocity > self.max_y_velocity:
                self.y_velocity = self.max_y_velocity

    def handle_horizonal_collisions(self, collisions):
        """ Stop rect from moving through collisions horizontally """
        self.update_rect_x()
        collision_objects = pygame.sprite.spritecollide(self, collisions, False)
        for collision_obj in collision_objects:
            collision_obj.horizontal_collide(self)
            self.position.set_x(self.rect.x)
        if collision_objects: self.collision_occured()

    def handle_vertical_collisions(self, collisions):
        """ Stop rect from moving through collisions vertically """
        self.update_rect_y()
        collision_objects = pygame.sprite.spritecollide(self, collisions, False)
        for collision_obj in collision_objects:
            collision_obj.vertical_collide(self)
            self.position.set_y(self.rect.y)
        if collision_objects: self.collision_occured()

    def collision_occured(self):
        """ Called when sprite has collided with an object """
        pass

    def get_diagonal_movement(self, speed):
        """ Reduce diagonal movement to be equal to normal movement speed """
        move_speed = math.sqrt( (speed*speed)/2.0 )
        return (move_speed, move_speed)
