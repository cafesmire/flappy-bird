import pygame
import assets
import config
from layer import Layer

class GameMessage(pygame.sprite.Sprite):
    def __init__(self, game_status, *groups):
        self._layer = Layer.UI
        self.image = assets.get_asset('gameover') if game_status == 'gameover' else assets.get_asset('message')
        self.rect = self.image.get_rect(center=(config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT/2))
        super().__init__(*groups)