import pygame
import pygame_menu
import sys
from src.bird_part import bird
from src.cloud_part import Cloud
import src.button as button
from pygame import sprite
from pygame.sprite import Group
import time

def run():
  """function for the process in the game as a whole"""
  pygame.init()
  screen = pygame.display.set_mode((500, 500))
  pygame.display.set_caption("Игра")
  pygame.mixer.music.load("./music/birds_song.mp3")
  black_color = (0, 0, 0)
  bird_1 = bird(screen)
  cloud_1 = Group()
  number_of_clouds = 0
  count = 0
  game_over_pic = pygame.image.load('./images/game_over.png')
  pygame.mixer.music.play(-1)

  while True:
    """adding clouds"""
    if number_of_clouds == 0:
      new_cloud = Cloud(screen)
      cloud_1.add(new_cloud)
      number_of_clouds += 1
      count += 1
    """manage the bird"""
    button.buttons(bird_1)
    bird_1.bird_position()
    screen.fill(black_color)
    for cl in cloud_1.sprites():
      cl.drawcl()
    bird_1.output()
    cloud_1.update(count)
    """deleting clouds if they are outside"""
    for cl in cloud_1.copy():
      if cl.rect.right <= screen.get_rect().left:
        cloud_1.remove(cl)
        number_of_clouds -= 1
    for cl in cloud_1.copy():
      if bird_1.rect.right <= cl.rect.right and bird_1.rect.left >= cl.rect.left and bird_1.rect.top <= cl.rect.bottom and bird_1.rect.bottom >= cl.rect.top:
        data_file = open("./data/data.txt", "a")
        data_file.write(str(str(count) + ' ' + user_name.get_value()) + '\n')
        data_file.close()
        pygame.mixer.music.load("./music/game_over_sound.mp3")
        pygame.mixer.music.play(0)
        screen.blit(game_over_pic, (0, 0))
        pygame.display.flip()
        time.sleep(3)
        sys.exit()
    pygame.display.flip()

def sort_key(line):
  """comparator for sorting"""
  parts = line.split()
  return int(parts[0])

def sort_lines(filename):
  """sort lines into a file"""
  with open(filename, 'r') as f:
      lines = f.readlines()
  lines = sorted(lines, key=sort_key, reverse=True)
  with open(filename, 'w') as f:
      f.writelines(lines)

def read_beg_of_file(filename):
  """return first 3 strings of the file"""
  with open(filename, 'r') as f:
    text = ''
    for i in range(3):
      text += f.readline()
  return text

def record_t():
  """showing record table"""
  pygame.mixer.music.load("./music/джентельмены_удачи.mp3")
  pygame.mixer.music.play(-1)
  pygame.init()
  screen2 = pygame.display.set_mode((500, 500))
  pygame.display.set_caption("Рекорды")
  menu2 = pygame_menu.Menu('рекорды', 500, 500, theme=pygame_menu.themes.THEME_DARK)
  sort_lines('./data/data.txt')
  text = read_beg_of_file('./data/data.txt')
  menu2.add.label(text)
  menu2.add.button('Назад', menu_main)
  menu2.mainloop(screen2)

def menu_main():
  """function for main menu screen"""
  pygame.init()
  pygame.mixer.music.load("./music/menu_sound.mp3")
  pygame.mixer.music.play(-1)
  screen0 = pygame.display.set_mode((500, 500))
  pygame.display.set_caption("Игра")
  menu = pygame_menu.Menu('хотите сыграть?', 500, 500, theme=pygame_menu.themes.THEME_DARK)
  global user_name
  user_name = menu.add.text_input('Имя :', default='Маша')
  menu.add.button('Играть!', run)
  menu.add.button('Таблица рекордов', record_t)
  menu.add.button('Выйти', pygame_menu.events.EXIT)
  menu.mainloop(screen0)