import sys
import pygame

class SpaceInvaders:
    """Class to manage game assets and behaviour"""
    def __init__(self):
        """initialise the game and create game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Space Invaders')

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    si = SpaceInvaders()
    si.run_game()