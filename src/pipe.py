import config
import assets
from layer import Layer
import pygame
import random

class Pipe(pygame.sprite.Sprite):
    def __init__(self, *group):
        self._layer = Layer.OBSTACLE
        self.gap = 100
        self.passed = False
        self.sprite = assets.get_asset('pipe-green')
        self.sprite_rect = self.sprite.get_rect()
        sprite_floor_height = assets.get_asset('base').get_rect().height
        min_y = 100
        max_y = config.SCREEN_HEIGHT - sprite_floor_height - self.gap

        self.bottom_pipe = self.sprite
        self.bottom_rect = self.bottom_pipe.get_rect(topleft=(0,self.sprite_rect.height + self.gap))

        self.top_pipe = pygame.transform.flip(self.sprite, flip_x=False, flip_y=True)
        self.top_rect = self.top_pipe.get_rect(topleft=(0,0))

        self.image = pygame.surface.Surface((self.sprite_rect.width, self.sprite_rect.height * 2 + self.gap), pygame.SRCALPHA)
        self.image.blit(self.bottom_pipe, self.bottom_rect)
        self.image.blit(self.top_pipe, self.top_rect)

        self.rect = self.image.get_rect(midleft=(config.SCREEN_WIDTH,random.uniform(min_y, max_y)))
        self.mask = pygame.mask.from_surface(self.image)
        super().__init__(*group)

    def update(self):
        self.rect.x -= 2

        if self.rect.right <= 0:
            self.kill()

    def has_passed(self):
        if self.rect.x < 50 and not self.passed:
            self.passed = True
            return True
        return False

