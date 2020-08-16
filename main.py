"""You can delete every image that is creating and re run the code it's gonna work anyway"""
import pygame
from sys import exit
from random import choice
from settings import Settings
from checker import Checker


class G2048:
    def __init__(self):
        self.screen = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))
        pygame.display.set_caption("2048")
        """ Game variables """
        self.board = [[0 for j in range(Settings.COLS)] for i in range(Settings.ROWS)]
        self.start = True
        self.changes = True
        """ Checking missing number images """
        Checker.checkingMissingImages()
        self.images = Checker.initImages()
        """ Board settings """
        self.picture = pygame.image.load("board.png")
        self.picture = pygame.transform.scale(self.picture, (Settings.screen_width, Settings.screen_height))

    def runGame(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick()
            print(clock.get_fps())
            if self.__noMoves():
                self.__resetGame()
                self.changes = True
            self.__checkEvents()
            if self.changes:
                self.__updateScreen()
                self.changes = False

    def __updateScreen(self):
        self.screen.blit(self.picture, (0, 0))
        if self.start:
            self.__randomPick()
            self.start = False
        for row in range(Settings.ROWS):
            for column in range(Settings.COLS):
                if self.board[row][column] != 0:
                    self.__drawNumber(self.board[row][column], row, column)
        pygame.display.update()

    def __drawNumber(self, number, row, column):
        x = column * (Settings.image_width + Settings.boarder_width) + Settings.boarder_width
        y = row * (Settings.image_height + Settings.boarder_height) + Settings.boarder_height

        self.screen.blit(self.images[str(number)], (x, y))

    def __checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.__canMoveUp():
                        self.__moveUp()
                        self.__randomPick()
                        self.changes = True
                if event.key == pygame.K_DOWN:
                    if self.__canMoveDown():
                        self.__moveDown()
                        self.__randomPick()
                        self.changes = True
                if event.key == pygame.K_LEFT:
                    if self.__canMoveLeft():
                        self.__moveLeft()
                        self.__randomPick()
                        self.changes = True
                if event.key == pygame.K_RIGHT:
                    if self.__canMoveRight():
                        self.__moveRight()
                        self.__randomPick()
                        self.changes = True

    def __noMoves(self):
        for i in range(Settings.ROWS):
            for j in range(Settings.COLS):
                if self.board[i][j] == 0:
                    return False

        if self.__canMoveRight():
            return False
        if self.__canMoveLeft():
            return False
        if self.__canMoveUp():
            return False
        if self.__canMoveDown():
            return False

        return True

    def __resetGame(self):
        self.board = [[0 for j in range(Settings.COLS)] for i in range(Settings.ROWS)]
        self.start = True

    def __randomPickAnimation(self, row, column, number):
        image_width = round(Settings.image_width / 15)
        image_height = round(Settings.image_height / 15)
        adder_width = round(Settings.image_width / 7.5)
        adder_height = round(Settings.image_height / 7.5)
        for _ in range(7):
            image = pygame.image.load(str(number) + '.png')
            x = column * (Settings.image_width + Settings.boarder_width) + Settings.boarder_width + round((Settings.image_width - image_width) / 2)
            y = row * (Settings.image_height + Settings.boarder_height) + Settings.boarder_height + round((Settings.image_height - image_height) / 2)
            image = pygame.transform.scale(image, (image_width, image_height))
            self.screen.blit(image, (x, y))
            pygame.display.update()
            pygame.time.delay(20)
            image_width += adder_width
            image_height += adder_height

    def __randomPick(self):
        available = []
        for row in range(Settings.ROWS):
            for column in range(Settings.COLS):
                if self.board[row][column] == 0:
                    available.append((row, column))

        random_row, random_column = choice(available)
        random_number = choice([2, 2, 2, 4])
        self.board[random_row][random_column] = random_number
        self.__randomPickAnimation(random_row, random_column, random_number)

    def __canMoveRight(self) -> bool:
        for row in range(Settings.ROWS):
            for column in range(Settings.COLS - 1):
                if self.board[row][column] != 0:
                    if (self.board[row][column + 1] == 0) or (self.board[row][column] == self.board[row][column + 1]):
                        return True

        return False

    def __canMoveLeft(self) -> bool:
        for row in range(Settings.ROWS):
            for column in range(Settings.COLS - 1, 0, -1):
                if self.board[row][column] != 0:
                    if (self.board[row][column - 1] == 0) or (self.board[row][column] == self.board[row][column - 1]):
                        return True

        return False

    def __canMoveUp(self) -> bool:
        for column in range(Settings.COLS):
            for row in range(Settings.ROWS - 1, 0, -1):
                if self.board[row][column] != 0:
                    if (self.board[row - 1][column] == 0) or (self.board[row][column] == self.board[row - 1][column]):
                        return True

        return False

    def __canMoveDown(self) -> bool:
        for column in range(Settings.COLS):
            for row in range(Settings.ROWS - 1):
                if self.board[row][column] != 0:
                    if (self.board[row + 1][column] == 0) or (self.board[row][column] == self.board[row + 1][column]):
                        return True

        return False

    def __moveRight(self):
        for row in range(Settings.ROWS):
            for column in range(Settings.COLS - 2, -1, -1):
                if self.board[row][column] != 0:
                    j = column + 1
                    possible_collision = [True for _ in range(Settings.COLS)]
                    while j <= Settings.COLS - 1:
                        if self.board[row][j] == 0:
                            self.board[row][j] = self.board[row][j - 1]
                            self.board[row][j - 1] = 0
                        elif self.board[row][j] == self.board[row][j - 1] and possible_collision[j]:
                            possible_collision[j] = False
                            self.board[row][j] *= 2
                            self.board[row][j - 1] = 0
                            break
                        else:
                            break

                        j += 1

    def __moveLeft(self):
        for row in range(Settings.ROWS):
            for column in range(1, Settings.COLS):
                if self.board[row][column] != 0:
                    j = column - 1
                    possible_collision = [True for _ in range(Settings.COLS)]
                    while j >= 0:
                        if self.board[row][j] == 0:
                            self.board[row][j] = self.board[row][j + 1]
                            self.board[row][j + 1] = 0
                        elif self.board[row][j] == self.board[row][j + 1] and possible_collision[j]:
                            possible_collision[j] = False
                            self.board[row][j] *= 2
                            self.board[row][j + 1] = 0
                            break
                        else:
                            break

                        j -= 1

    def __moveUp(self):
        for column in range(Settings.COLS):
            for row in range(1, Settings.ROWS):
                if self.board[row][column] != 0:
                    i = row - 1
                    possible_collision = [True for _ in range(Settings.ROWS)]
                    while i >= 0:
                        if self.board[i][column] == 0:
                            self.board[i][column] = self.board[i + 1][column]
                            self.board[i + 1][column] = 0
                        elif self.board[i][column] == self.board[i + 1][column] and possible_collision[i]:
                            possible_collision[i] = False
                            self.board[i][column] *= 2
                            self.board[i + 1][column] = 0
                            break
                        else:
                            break

                        i -= 1

    def __moveDown(self):
        for column in range(Settings.COLS):
            for row in range(Settings.ROWS - 2, -1, -1):
                if self.board[row][column] != 0:
                    possible_collision = [True for _ in range(Settings.ROWS)]
                    i = row + 1
                    while i <= Settings.ROWS - 1:
                        if self.board[i][column] == 0:
                            self.board[i][column] = self.board[i - 1][column]
                            self.board[i - 1][column] = 0
                        elif self.board[i][column] == self.board[i - 1][column] and possible_collision[i]:
                            possible_collision[i] = False
                            self.board[i][column] *= 2
                            self.board[i - 1][column] = 0
                            break
                        else:
                            break

                        i += 1


if __name__ == "__main__":
    obj = G2048()
    obj.runGame()
