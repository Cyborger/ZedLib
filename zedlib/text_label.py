import zedlib
import pygame


class TextLabel(zedlib.Surface):
    def __init__(self, text, rect, font, color=(255, 255, 255), aa=False):
        super().__init__(pygame.Surface((rect.width, rect.height)),
                         pygame.SRCALPHA, 32)
        self.rect = rect
        self.image.convert_alpha()
        self.font = font
        self.color = color
        self.aa = aa
        self.draw_text(text)

    def draw_text(self, text):
        line_spacing = -2
        font_height = self.font.size("Tg")[1]
        y = 0

        while text:
            i = 1
            if y + font_height > self.rect.bottom:
                break
            while (self.font.size(text[:i])[0] < self.rect.width
                   and i < len(text)):
                i += 1

            if i < len(text):
                i = text.rfind(" ", 0, i) + 1
            surface = self.font.render(text[:i], self.aa, self.color)
            self.image.blit(surface, (0, y))
            y += font_height + line_spacing

            text = text[i:]
