""" Alternative to pygame.image.load() that has scaling and automatically
convert alpha"""
import pygame


# Should be used instead of pygame.image.load()
def LoadImage(file_path, scale=1):
    image = pygame.image.load(file_path).convert_alpha()
    if scale != 1:
        new_width = image.get_width() * scale
        new_height = image.get_height() * scale
        image = pygame.transform.scale(image, (new_width, new_height))
    return image
