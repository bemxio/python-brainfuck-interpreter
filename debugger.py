import pygame
import time

class ArrayVisualization:
    def __init__(self) -> None:
        pygame.init()

        resolution = (1000, 90)
        self.width, self.height = resolution

        self.surface = pygame.display.set_mode(resolution)
        self.font = pygame.font.SysFont('consolas', 22)

    def update(self, array, code, index):
        preview = array[:25]

        beginning = index - 20
        if beginning < 0:
            beginning = 0

        recent = code[beginning:index]
        self.surface.fill((0, 0, 0))

        text = self.font.render(str(preview), True, (255, 255, 255))
        self.surface.blit(text, (10, 10))

        text = self.font.render("".join(recent), True, (255, 255, 255))
        self.surface.blit(text, (10, 50))

        pygame.display.update()
        pygame.event.pump()

        time.sleep(0.05)
