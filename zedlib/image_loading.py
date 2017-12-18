import pygame


def load_image(file_path, scale=1):
    """ Load an image, automatically calls convert_alpha() """
    image = pygame.image.load(file_path).convert_alpha()
    if scale is not 1:
        new_width = image.get_width() * scale
        new_height = image.get_height() * scale
        image = pygame.transform.scale(image, (new_width, new_height))
    return image
