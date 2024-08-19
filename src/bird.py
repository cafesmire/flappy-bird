import assets
import config
import pygame
from pipe import Pipe
from floor import Floor
from layer import Layer

class Bird(pygame.sprite.Sprite):
    def __init__(self, *group):
        self._layer = Layer.PLAYER
        self.images = [
            assets.get_asset('yellowbird-downflap'),
            assets.get_asset('yellowbird-midflap'),
            assets.get_asset('yellowbird-upflap')]
        
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(-50,50))
        self.mask = pygame.mask.from_surface(self.image)

        self.animation_time = 100
        self.time_passed = pygame.time.get_ticks()
        self.flap = 0

        super().__init__(*group)

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.time_passed > self.animation_time:
            self.time_passed = now
            self.images.insert(0, self.images.pop())
            self.image = self.images[0]

        self.flap += config.GRAVITY
        self.rect.y += self.flap

        if self.rect.x <= 50:
            self.rect.x += 3

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.flap = 0
            self.flap -= 6

    def check_collision(self, sprites):
        for sprite in sprites:
            if ((type(sprite) is Pipe or type(sprite) is Floor) and sprite.mask.overlap(self.mask,
                                                                                        (self.rect.x - sprite.rect.x,
                                                                                        self.rect.y - sprite.rect.y)) or self.rect.bottom < 0):
                return True
        return False
        