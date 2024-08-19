import pygame
import assets
import config
from layer import Layer

class Score(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.UI
        self.value = 0
        self.image = pygame.Surface((0,0), pygame.SRCALPHA)

        self.__create()
        super().__init__(*groups)

    def __create(self):
        self.str_value = str(self.value)

        self.images = []
        self.width = 0

        for value in self.str_value:
            image = assets.get_asset(value)
            self.images.append(image)
            self.width += image.get_width()

        self.height = self.images[0].get_height()
        self.image = pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(config.SCREEN_WIDTH/2, 50))

        x = 0
        for img in self.images:
            self.image.blit(img, (x, 0))
            x += img.get_width()
        
    def update(self):
        self.__create()