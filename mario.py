import pygame


class Mario():

    def __init__(self, screen):
        """инициализация марио"""

        self.screen = screen
        self.image = pygame.image.load('images/mario.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 1.7, self.image.get_height() * 1.7))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 421
        self.rect.bottom = 448  # низ марио
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.mright = False
        self.mleft = False
        self.back = 0

    def update_mario(self):
        """обновление позиции марио"""
        if self.mright and self.rect.right < self.screen_rect.right - 160:
            self.centerx += 6
        elif self.mright and self.rect.right >= self.screen_rect.right - 160 and self.back > -2030:
            self.back -= 6
        if self.mleft and self.rect.left > 1:
            self.centerx -= 6

        self.rect.centerx = self.centerx
