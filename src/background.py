import assets
import config
import pygame
from layer import Layer

class Background(pygame.sprite.Sprite):
    def __init__(self, index, *group):
        self._layer = Layer.BACKGROUND
        self.image = assets.get_asset('background-day')
        self.rect = self.image.get_rect(topleft=(config.SCREEN_WIDTH * index, 0))
        super().__init__(*group)

    def update(self):
        self.rect.x -= 1

        if self.rect.right <= 0:
            self.rect.x = config.SCREEN_WIDTH