import importlib
import time

class ArrayVisualization():
    def __init__(self, wait="delay", delay=0.1):
        self.pygame = importlib.import_module("pygame")
        self.pygame.init()
        
        resolution = (1000, 90)
        self.width, self.height = resolution
        self.type, self.delay = wait, delay

        self.surface = self.pygame.display.set_mode(resolution)
        self.font = self.pygame.font.SysFont('consolas', 22)

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

        self.pygame.display.update()

        while self.type == "step":
            with self.pygame.event.get() as event:
                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_SPACE:
                        break
        
        if self.type == "delay":
            self.pygame.event.pump()
            self.pygame.time.delay(int(self.delay * 1000))