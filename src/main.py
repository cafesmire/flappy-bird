import config
import assets
import pygame
from background import Background
from floor import Floor
from bird import Bird
from pipe import Pipe
from game_message import GameMessage
from score import Score

def create_sprites(sprites):
    Background(0, sprites)
    Background(1, sprites)
    Floor(0, sprites)
    Floor(1, sprites)

    return Bird(sprites), GameMessage('message',sprites), Score(sprites)

def main():
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    create_pipe = pygame.USEREVENT
    running = True
    gameover = False
    gamestart = False

    assets.load_assets()
    sprites = pygame.sprite.LayeredUpdates()

    bird, game_start_message, score = create_sprites(sprites)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == create_pipe: 
                Pipe(sprites)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gamestart and not gameover:
                    gamestart = True
                    game_start_message.kill()
                    pygame.time.set_timer(create_pipe, 1500)
                if event.key == pygame.K_ESCAPE and gameover:
                    gameover = False
                    gamestart = False
                    sprites.empty()
                    bird, game_start_message, score = create_sprites(sprites)
            if not gameover:
                bird.handle_event(event)

        screen.fill(0)
        sprites.draw(screen)

        if gamestart and not gameover:
            sprites.update()

        if bird.check_collision(sprites) and not gameover:
            gameover=True
            gamestart=False
            GameMessage('gameover', sprites)
            pygame.time.set_timer(create_pipe, 0)
        
        for sprite in sprites:
            if type(sprite) is Pipe and sprite.has_passed():
                score.value += 1
        
        pygame.display.flip()
        clock.tick(config.FPS)
    
    pygame.quit()
        

if __name__ == '__main__':
    main()