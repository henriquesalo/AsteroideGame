import sys
import pygame
from score import Score
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable
    #criando um novo objeto
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    Score.containers = (updatable, drawable)
    score = Score(10, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                game_over(screen, score)

            for shot in shots:
                if asteroid.check_collisions(shot):
                    shot.kill()
                    asteroid.split()
                    # incrementando +1 ponto sempre que destruir algum asteroide
                    score.add_points(1)

        screen.fill("black")

        for objects in drawable:
            objects.draw(screen)

        # garantindo que o score vai aparecer acima de tudo
        screen.blit(score.image, score.rect)

        pygame.display.flip()
        dt = fps.tick(60) / 1000 # Limitando o fps para 60 frames por segundo

def game_over(screen, score):
    font_big = pygame.font.SysFont(pygame.font.get_default_font(), 80)
    font_small = pygame.font.SysFont(pygame.font.get_default_font(), 40)

    # Renderiza textos 
    game_over_text = font_big.render("GAME OVER", True, (255, 0, 0))
    score_text = font_small.render(f"Pontuação final: {score.score}", True, (255, 255, 255))
    restart_text = font_small.render("Pressione ENTER para jogar novamente ou ESC para sair", True, (200, 200, 200))

    # Pegando posições centralizadas
    game_over_rect = game_over_text.get_rect(center=(screen.get_width() /2, screen.get_height() / 2 - 100))
    score_rect = score_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    restart_rect = restart_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2 + 100))

    # printando na tela
    screen.fill((0, 0, 0))
    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    screen.blit(restart_text, restart_rect)
    pygame.display.flip()

    # Loop de espera até usuário decidir
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # ENTER → reinicia
                    Score.reset(score)
                    main()
                elif event.key == pygame.K_ESCAPE:  # ESC → sai
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
