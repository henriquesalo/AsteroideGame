import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self, x, y, font_size=40, color=(255,255,255)):
        super().__init__()

        self.font = pygame.font.SysFont(pygame.font.get_default_font(), font_size)
        self.color = color
        self.score = 0
        self.image = self.font.render(f"Score: {self.score}", True, self.color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update_text(self):
        self.image = self.font.render(f"Score: {self.score}", True, self.color)
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def add_points(self, points):
        self.score += points
        self.update_text()

    def reset(self):
        self.score = 0
        self.update_text()

    def update(self, dt):
        pass