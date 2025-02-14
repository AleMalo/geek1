from ruchy import *

class Plansza:
    def __init__(self):
        screen = pygame.display.set_mode((1240, 950))
        background = (30, 115, 53)

        player1 = Player(1, 1000, 700)
        player2 = Player(2, 100, 100)
        chest1 = Chest(300, 300)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                keys = pygame.key.get_pressed()
                player1.move(keys)
                player2.move(keys)

            screen.fill(background)
            player1.draw(screen)
            player2.draw(screen)
            chest1.draw(screen)

            pygame.display.update()

        pygame.quit()
