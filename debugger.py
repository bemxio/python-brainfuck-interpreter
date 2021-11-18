import pygame
import time

class ArrayVisualization:
    def __init__(self) -> None:
        pygame.init()

        resolution = (1000, 100)
        self.width, self.height = resolution

        self.surface = pygame.display.set_mode(resolution)
        self.font = pygame.font.SysFont('consolas', 22)

    def update(self, array):
        preview = array[:25]

        self.surface.fill((0, 0, 0))
        text = self.font.render(str(preview), True, (255, 255, 255))
        self.surface.blit(text, (10, 10))

        pygame.display.update()
        pygame.event.pump()

        time.sleep(0.01)
