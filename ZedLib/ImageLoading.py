import pygame


# Should be used instead of pygame.image.load()
def LoadImage(file_path, scale=1):
    image = pygame.image.load(file_path).convert_alpha()
    if scale != 1:
        new_width = image.current_w * scale
        new_height = image.current_h * scale
        pygame.transform.scale(image, (new_width, new_height), image)
    return image
