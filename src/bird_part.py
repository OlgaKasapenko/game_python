import pygame

class bird():
  """class for functions for object - bird"""

  def __init__(self, screen):
    """add fields corresponding to the location of the bird on the screen"""
    self.screen = screen
    self.image = pygame.image.load('./images/birdik.png')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    self.rect.centerx = self.screen_rect.centerx / 2
    self.rect.centery = self.screen_rect.centery
    self.centy = float(self.rect.centery)
    self.buttonup = False
    self.buttondown = False

  def output(self):
    """draw a bird"""
    self.screen.blit(self.image, self.rect)

  def bird_position(self):
    """move the bird if the up or down buttons are pressed"""
    if self.buttondown and self.rect.bottom < self.screen_rect.bottom:
      self.centy += 1
    if self.buttonup and self.rect.top > self.screen_rect.top:
      self.centy -= 1
    self.rect.centery = self.centy
    
