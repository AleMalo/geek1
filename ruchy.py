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
    def __init__(self, x, y, number, id):
        self.x = x
        self.y = y
        self.id = id
        self.section = ''
        if number == 1:
            self.image1 = pygame.image.load('images/chest_closed1.PNG')
            self.image2 = pygame.image.load('images/chest_open1.PNG')
            if len(chest_answers1) == 5:
                self.section = chest_answers1[self.id]
        else:
            self.image1 = pygame.image.load('images/chest_closed2.PNG')
            self.image2 = pygame.image.load('images/chest_open2.PNG')
            if len(chest_answers1) == 5:
                self.section = chest_answers2[self.id]

        self.image = self.image1

    def is_near(self, player):
        distance = math.sqrt((self.x - player.x) ** 2 + (self.y - player.y) ** 2)
        return distance < 80

    def open(self, player, keys, open_key):
        if self.is_near(player) and keys[open_key]:
            self.image = self.image2

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
