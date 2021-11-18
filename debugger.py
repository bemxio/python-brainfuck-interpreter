import pygame

class ArrayVisualization:
    def __init__(self) -> None:
        pygame.init()
        self.surface = pygame.display.set_mode([500, 20])
        self.font = pygame.font.SysFont('Arial', 15)
    
    def grid(self):
        width, height = self.surface.get_size()
        size = 20

        for x in range(0, width, size):
            for y in range(0, height, size):
                pygame.draw.rect(
                    self.surface, 
                    (255, 255, 255), 
                    (x, y, size, size), 
                    1
                )

    def update(self, array):
        preview = array[:25]
        self.grid()

        
