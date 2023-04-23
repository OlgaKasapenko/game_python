import pygame
import sys
from src.bird_part import bird


def buttons(bird):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        bird.buttonup = True
      elif event.key == pygame.K_DOWN:
        bird.buttondown = True
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        bird.buttonup = False
      elif event.key == pygame.K_DOWN:
        bird.buttondown = False
