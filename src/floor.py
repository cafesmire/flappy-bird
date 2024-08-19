import assets
import config
import pygame
from layer import Layer

class Floor(pygame.sprite.Sprite):
    def __init__(self, index, *group):
        self._layer = Layer.FLOOR
        self.image = assets.get_asset('base')
        self.rect = self.image.get_rect(bottomleft=(config.SCREEN_WIDTH * index, config.SCREEN_HEIGHT))
        self.mask = pygame.mask.from_surface(self.image)
        super().__init__(*group)
        
    def update(self):
        self.rect.x -= 1

        if self.rect.right <= 0:
            self.rect.x = config.SCREEN_WIDTH