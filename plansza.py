from ruchy import *


class Plansza:
    def __init__(self):
        screen = pygame.display.set_mode((1440, 810))

        background = Bg(0, 0)
        player1 = Player(1, 0, 0)
        player2 = Player(2, 1350, 630)
        chest_player1 = [Chest(random.randint(50, 1390), random.randint(50, 760), 1) for _ in range(5)]
        chest_player2 = [Chest(random.randint(50, 1390), random.randint(50, 760), 2) for _ in range(5)]

        running = True
        while running:
            screen.fill((0, 0, 0))
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            player1.move(keys)
            player2.move(keys)

            background.draw(screen)
            for chest in chest_player1:
                chest.open(player1, keys, pygame.K_e)
                chest.draw(screen)

            for chest in chest_player2:
                chest.open(player2, keys, pygame.K_SPACE)
                chest.draw(screen)

            player1.draw(screen)
            player2.draw(screen)

            pygame.display.update()

        pygame.quit()
