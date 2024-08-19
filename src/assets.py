import os
import pygame

sprites = {}

def load_assets():
    path = os.path.join('flappy-bird-assets', 'sprites')
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file)).convert_alpha()

def get_asset(name):
    return sprites[name]