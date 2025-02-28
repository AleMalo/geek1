import pygame
import math
import random

password1 = ''
chest_answers1 = []
password2 = ''
chest_answers2 = []

class Player:
    def __init__(self, number, x, y):
        self.x = x
        self.y = y
        self.speed = 3
        self.number = number
        if number == 1:
            self.image = pygame.image.load('images/hacker1.PNG')
        else:
            self.image = pygame.image.load('images/hacker2.PNG')

    def move(self, keys):
        if self.number == 1:
            if keys[pygame.K_d]:
                self.x += self.speed
            if keys[pygame.K_a]:
                self.x -= self.speed
            if keys[pygame.K_w]:
                self.y -= self.speed
            if keys[pygame.K_s]:
                self.y += self.speed
        else:
            if keys[pygame.K_RIGHT]:
                self.x += self.speed
            if keys[pygame.K_LEFT]:
                self.x -= self.speed
            if keys[pygame.K_UP]:
                self.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Bg:
    def __init__(self, x, y):
        self.image = pygame.image.load('images/background.png')
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Chest:
    def __init__(self, x, y, number, clues, id):
        self.x = x
        self.y = y
        self.id = id
        self.opened = False
        if len(clues) == 5:
            self.section = clues[id]
            print('done', self.section)
        if number == 1:
            self.image1 = pygame.image.load('images/chest_closed1.PNG')
            self.image2 = pygame.image.load('images/chest_open1.PNG')
        else:
            self.image1 = pygame.image.load('images/chest_closed2.PNG')
            self.image2 = pygame.image.load('images/chest_open2.PNG')

        self.image = self.image1

    def is_near(self, player):
        distance = math.sqrt((self.x - player.x) ** 2 + (self.y - player.y) ** 2)
        return distance < 80

    def open(self, player, keys, open_key, clues, screen):
        if self.is_near(player) and keys[open_key]:
            self.opened = True
            self.image = self.image2
            clues[self.id].draw(self, screen)
            print('clue is drawn')

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Clue:
    def __init__(self, x, y, section, font, color, id):
        self.x = x + 22
        self.y = y + 22
        self.section = section
        self.font = font
        self.color = color
        self.id = id

        self.text = self.font.render(f'{self.id}: {self.section}', True, self.color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x, self.y)

    def draw(self, chest, screen):
        if chest.opened:
            screen.blit(self.text, self.text_rect)
            print('x:', self.x, self.section)
