import pygame
from settings import Settings


def fontSizes():
    size4, dim4 = None, None
    size5, dim5 = None, None
    size6, dim6 = None, None
    i = 0
    while True:
        font = pygame.font.SysFont("norasi", i, True)
        text_width, text_height = font.size("0")

        if not (text_width * 4 > Settings.image_width):
            size4 = i
            dim4 = (text_width, text_height)
        else:
            break
        if not (text_width * 5 > Settings.image_width):
            size5 = i
            dim5 = (text_width, text_height)
        if not (text_width * 6 > Settings.image_width):
            size6 = i
            dim6 = (text_width, text_height)

        i += 1

    return size4, size5, size6, dim4, dim5, dim6


class Grabber:
    screen = pygame.Surface((Settings.image_width, Settings.image_height))
    pygame.font.init()
    size4, size5, size6, dim4, dim5, dim6 = fontSizes()
    font_1234 = pygame.font.SysFont("norasi", size4, True)
    font_5 = pygame.font.SysFont("norasi", size5, True)
    font_6 = pygame.font.SysFont("norasi", size6, True)

    @classmethod
    def drawNumber(cls, number):
        screen = pygame.Surface((Settings.image_width, Settings.image_height))
        block_color = None
        num_color = (255, 255, 255)
        label = None
        x, y = 0, 0
        if number == 2:
            block_color = (200, 200, 200)
            x += round((Settings.image_width - cls.dim4[0]) / 2)
            y += round((Settings.image_height - cls.dim4[1]) / 2)
        if number == 4:
            block_color = (150, 150, 150)
            x += round((Settings.image_width - cls.dim4[0]) / 2)
            y += round((Settings.image_height - cls.dim4[1]) / 2)
        elif number == 8:
            block_color = (255, 100, 10)
            x += round((Settings.image_width - cls.dim4[0]) / 2)
            y += round((Settings.image_height - cls.dim4[1]) / 2)
        elif number == 16:
            block_color = (255, 75, 10)
            x += round((Settings.image_width - cls.dim4[0] * 2) / 2)
            y += round((Settings.image_height - cls.dim4[1]) / 2)
        elif number == 32:
            block_color = (255, 35, 10)
            x += round((Settings.image_width - cls.dim4[0] * 2) / 2)
            y += round((Settings.image_height - cls.dim4[1]) / 2)
        elif number == 64:
            block_color = (255, 0, 0)
            x += round((Settings.image_width - cls.dim4[0] * 2) / 2)
            y += round((Settings.image_height - cls.dim4[1]) / 2)
        elif number == 128 or number == 256:
            block_color = (255, 200, 0)
            x += round((Settings.image_width - cls.dim4[0] * 3) / 2)
            y += round((Settings.image_height - cls.dim4[1]) / 2)
        elif number == 512:
            block_color = (255, 180, 0)
            x += round((Settings.image_width - cls.dim4[0] * 3) / 2)
            y += round((Settings.image_height - cls.dim4[1]) / 2)
        elif number == 1024 or number == 2048:
            block_color = (255, 150, 0)
            x += round((Settings.image_width - cls.dim4[0] * 4) / 2)
            y += round((Settings.image_height - cls.dim4[1]) / 2)
        elif number == 4096:
            block_color = (255, 100, 180)
            x += round((Settings.image_width - cls.dim4[0] * 4) / 2)
            y += round((Settings.image_height - cls.dim4[1]) / 2)
        elif number == 8192:
            block_color = (240, 0, 255)
            x += round((Settings.image_width - cls.dim4[0] * 4) / 2)
            y += round((Settings.image_height - cls.dim4[1]) / 2)
        elif number == 16384:
            block_color = (255, 0, 230)
            x += round((Settings.image_width - cls.dim5[0] * 5) / 2)
            y += round((Settings.image_height - cls.dim5[1]) / 2)
        elif number == 32768:
            block_color = (0, 255, 255)
            x += round((Settings.image_width - cls.dim5[0] * 5) / 2)
            y += round((Settings.image_height - cls.dim5[1]) / 2)
        elif number == 65536:
            block_color = (0, 0, 100)
            x += round((Settings.image_width - cls.dim5[0] * 5) / 2)
            y += round((Settings.image_height - cls.dim5[1]) / 2)
        elif 65536 < number <= 524288:
            block_color = (0, 0, 0)
            x += round((Settings.image_width - cls.dim6[0] * 6) / 2)
            y += round((Settings.image_height - cls.dim6[1]) / 2)
        pygame.draw.rect(cls.screen, block_color, (0, 0, Settings.image_width, Settings.image_height))
        if number <= 8192:
            label = cls.font_1234.render(str(number), 1, num_color)
        elif number <= 65536:
            label = cls.font_5.render(str(number), 1, num_color)
        elif number <= 524288:
            label = cls.font_6.render(str(number), 1, num_color)
        cls.screen.blit(label, (x, y))

    @classmethod
    def makeNumberImage(cls, number):
        cls.drawNumber(number)
        pygame.image.save(cls.screen, str(number) + ".png")

    @staticmethod
    def makeBoardImage():
        board_height = Settings.ROWS * 15 + (Settings.ROWS + 1) * 2
        board_width = Settings.COLS * 15 + (Settings.COLS + 1) * 2
        screen = pygame.Surface((board_width, board_height))
        border_color = (179, 179, 179)
        square_color = (242, 242, 242)
        for i in range(Settings.COLS + 1):
            x = i * 17
            y = 0
            pygame.draw.rect(screen, border_color, (x, y, 2, board_height))
        for j in range(Settings.ROWS + 1):
            x = 0
            y = j * 17
            pygame.draw.rect(screen, border_color, (x, y, board_width, 2))
        for row in range(Settings.ROWS):
            for column in range(Settings.COLS):
                x = column * 17 + 2
                y = row * 17 + 2
                pygame.draw.rect(screen, square_color, (x, y, 15, 15))
        pygame.image.save(screen, "board.png")
