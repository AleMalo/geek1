from ruchy import *

class Plansza:
    def __init__(self, clues1, clues2):
        self.c_player1 = clues1
        self.c_player2 = clues2
        print(clues1, clues2)
        print(self.c_player1, self.c_player2)

        pygame.init()

        screen = pygame.display.set_mode((1440, 810))

        FONTP1 = pygame.font.SysFont('Arial', 20, True)
        # print(FONTP1)

        background = Bg(0, 0)
        player1 = Player(1, 0, 0)
        player2 = Player(2, 1350, 630)
        chest_player1 = [Chest(random.randint(50, 1390), random.randint(50, 760), 1, self.c_player1, i) for i in range(5)]
        chest_player2 = [Chest(random.randint(50, 1390), random.randint(50, 760), 2, self.c_player2, i) for i in range(5)]

        for i in chest_player1: print(str(i.section))

        clues_player1 = [Clue(chest_player1[_].x, chest_player1[_].y, chest_player1[_].section, FONTP1, '#ffffff', _) for _ in range(5)]
        clues_player2 = [Clue(chest_player2[_].x, chest_player2[_].y, chest_player2[_].section, FONTP1, '#ffffff', _) for _ in range(5)]

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
                chest.open(player1, keys, pygame.K_e, clues_player1, screen)
                chest.draw(screen)

            for chest in chest_player2:
                chest.open(player2, keys, pygame.K_SPACE, clues_player2, screen)
                chest.draw(screen)

            for i in range(5):
                clues_player1[i].draw(chest_player1[i], screen)
                clues_player2[i].draw(chest_player2[i], screen)

            # for clue in clues_player1:
            #     clue.draw(screen)
            #
            # for clue in clues_player2:
            #     clue.draw(screen)

            player1.draw(screen)
            player2.draw(screen)

            pygame.display.update()

        pygame.quit()
