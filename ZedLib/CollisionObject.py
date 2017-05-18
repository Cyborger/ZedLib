""" A basic collision object that stops sprites from walking through it"""


class CollisionObject:
    def __init__(self, image, x=0, y=0):
        self.image = image
        self.rect = self.image.get_rect()

    def HorizontalCollide(self, sprite):
        if sprite.move_x > 0:
            sprite.rect.right = self.rect.left
        elif sprite.move_x < 0:
            sprite.rect.left

    def VerticalCollide(self, sprite):
        if sprite.move_y > 0:
            sprite.rect.bottom = self.rect.top
        elif sprite.move_y < 0:
            sprite.rect.top = self.rect.bottom
