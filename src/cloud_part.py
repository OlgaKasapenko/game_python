import pygame
import random

class Cloud(pygame.sprite.Sprite):
  def __init__(self, screen):
    super(Cloud, self).__init__()
    self.screen = screen
    self.rect = pygame.Rect(0, 0, 100, 300)
    self.a = random.randint(100, 250)
    self.b = random.randint(100, 250)
    self.c = random.randint(100, 250)
    self.color = (self.a, self.b, self.c)
    self.speed = 0.5
    self.start_y_point = random.randint(screen.get_rect().top, screen.get_rect().bottom)
    self.rect.center = (screen.get_rect().right, self.start_y_point)
    self.centx = float(self.rect.centerx)

  def update(self, count):
    self.centx -= self.speed + 0.1 * count
    self.rect.centerx = self.centx

  def drawcl(self):
    pygame.draw.rect(self.screen, self.color, self.rect)

