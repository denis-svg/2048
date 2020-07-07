import pygame
from sys import exit
from random import choice

class G2048:
	def __init__(self):
		pygame.font.init()
		self.font_1234 = pygame.font.SysFont("norasi", 35, True)
		self.font_5 = pygame.font.SysFont("norasi", 31, True) 
		self.font_6 = pygame.font.SysFont("norasi", 25, True)
		""" Screen settings """
		self.screen_width = 350
		self.screen_height = 350 
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
		pygame.display.set_caption("2048")

		""" Board settings """
		self.picture = pygame.image.load("board.png")
		self.picture = pygame.transform.scale(self.picture, (self.screen_width, self.screen_height))

		""" Game variables """
		self.board = [  [0, 0, 0, 0],
						[0, 0, 0, 0], 
						[0, 0, 0, 0],
						[0, 0, 0, 0]  ]

	def run_game(self):
		self.__random_pick()
		while True:
			self.__check_events()
			self.__update_screen()

	def __random_pick(self):
		available = []
		for row in range(len(self.board)):
			for column in range(len(self.board)):
				if self.board[row][column] == 0:
					available.append((row, column))

		random_row, random_column = choice(available)
		self.board[random_row][random_column] = 2

	def __can_move_right(self) -> bool:
		for row in range(len(self.board)):
			for column in range(len(self.board) - 1):
				if self.board[row][column] != 0:
					if (self.board[row][column + 1] == 0) or (self.board[row][column] == self.board[row][column + 1]):
						return True

		return False

	def __can_move_left(self) -> bool:
		for row in range(len(self.board)):
			for column in range(len(self.board) - 1, 0, -1):
				if self.board[row][column] != 0:
					if (self.board[row][column - 1] == 0) or (self.board[row][column] == self.board[row][column - 1]):
						return True

		return False

	def __can_move_up(self) -> bool:
		for column in range(len(self.board)):
			for row in range(len(self.board) - 1, 0, -1):
				if self.board[row][column] != 0:
					if (self.board[row - 1][column] == 0) or (self.board[row][column] == self.board[row - 1][column]):
						return True

		return False

	def __can_move_down(self) -> bool:
		for column in range(len(self.board)):
			for row in range(len(self.board) - 1):
				if self.board[row][column] != 0:
					if (self.board[row + 1][column] == 0) or (self.board[row][column] == self.board[row + 1][column]):
						return True

		return False

	def __move_right(self):
		for row in range(len(self.board)):
			for column in range(len(self.board) - 2, -1, -1):
				if self.board[row][column] != 0:
					j = column + 1
					posibleCollision = [True for _ in range(4)]
					while j <= 3:
						if self.board[row][j] == 0:
							self.board[row][j] = self.board[row][j - 1]
							self.board[row][j - 1] = 0
						elif self.board[row][j] == self.board[row][j - 1] and posibleCollision[j]:
							posibleCollision[j] = False
							self.board[row][j] *= 2
							self.board[row][j - 1] = 0
							break
						else:
							break

						j += 1

	def __move_left(self):
		for row in range(len(self.board)):
			for column in range(1, len(self.board)):
				if self.board[row][column] != 0:
					j = column - 1
					posibleCollision = [True for _ in range(4)]
					while j >= 0:
						if self.board[row][j] == 0:
							self.board[row][j] = self.board[row][j + 1]
							self.board[row][j + 1] = 0
						elif self.board[row][j] == self.board[row][j + 1] and posibleCollision[j]:
							posibleCollision[j] = False
							self.board[row][j] *= 2
							self.board[row][j + 1] = 0
							break
						else:
							break

						j -= 1

	def __move_up(self):
		for column in range(len(self.board)):
			for row in range(1, len(self.board)):
				if self.board[row][column] != 0:
					i = row - 1
					posibleCollision = [True for _ in range(4)]
					while i >= 0:
						if self.board[i][column] == 0:
							self.board[i][column] = self.board[i + 1][column]
							self.board[i + 1][column] = 0
						elif self.board[i][column] == self.board[i + 1][column] and posibleCollision[i]:
							posibleCollision[i] = False
							self.board[i][column] *= 2
							self.board[i + 1][column] = 0
							break
						else:
							break

						i -= 1

	def __move_down(self):
		for column in range(len(self.board)):
			for row in range(len(self.board) - 2, -1, -1):
				if self.board[row][column] != 0:
					posibleCollision = [True for _ in range(4)]
					i = row + 1
					while i <= 3:
						if self.board[i][column] == 0:
							self.board[i][column] = self.board[i - 1][column]
							self.board[i - 1][column] = 0
						elif self.board[i][column] == self.board[i - 1][column] and posibleCollision[i]:
							posibleCollision[i] = False
							self.board[i][column] *= 2
							self.board[i - 1][column] = 0
							break
						else:
							break

						i += 1

	def __update_pos(self, dir, x, y):
		if dir == "up":
			pass
		elif dir == "down":
			pass
		elif dir == "left":
			pass
		elif dir == "right":
			pass

	def __check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					if self.__can_move_up():
						print("up")
						self.__move_up()
						self.__random_pick()
				if event.key == pygame.K_DOWN:
					if self.__can_move_down():
						print("down")
						self.__move_down()
						self.__random_pick()
				if event.key == pygame.K_LEFT:
					if self.__can_move_left():
						print("left")
						self.__move_left()
						self.__random_pick()
				if event.key == pygame.K_RIGHT:
					if self.__can_move_right():
						print("right")
						self.__move_right()
						self.__random_pick()

	def __draw_number(self, number, row, column):
		block_color = None
		num_color = (255, 255, 255)
		x, y = column * 85 + 10, row * 85 +10		
		if number == 2:
			block_color = (200, 200, 200)
			x += 29
			y += 7
		if number == 4:
			block_color = (150, 150, 150)
			x += 29
			y += 7
		elif number == 8:
			block_color = (255, 100, 10)
			x += 29
			y += 7
		elif number == 16:
			block_color = (255, 75, 10)
			x += 20
			y += 7
		elif number == 32:
			block_color = (255, 35, 10)
			x += 20
			y += 7
		elif number == 64:
			block_color = (255, 0, 0)
			x += 20
			y += 7
		elif number == 128 or number == 256:
			block_color = (255, 200, 0)
			x += 12
			y += 7
		elif number == 512:
			block_color = (255, 180, 0)
			x += 12
			y += 7
		elif number == 1024 or number == 2048:
			block_color = (255, 150, 0)
			x += 3
			y += 7
		elif number == 4096:
			block_color = (255,100,180)
			x += 3
			y += 7
		elif number == 8192:
			block_color = (240, 0, 255)
			x += 3
			y += 7
		elif number == 16384:
			block_color = (255, 0, 230)
			y += 10
		elif number == 32768:
			block_color = (0, 255, 255)
			y += 10
		elif number == 65536:
			block_color = (0, 0, 100)
			y += 10
		elif number > 65536 and number <= 524288:
			block_color = (0, 0, 0)
			x += 1
			y += 15
		pygame.draw.rect(self.screen, block_color, (column * 85 + 10, row * 85 + 10, 75, 75))
		if number <= 8192:
			label = self.font_1234.render(str(number), 1, num_color)
		elif number <= 65536:
			label = self.font_5.render(str(number), 1, num_color)
		elif number <= 524288:
			label = self.font_6.render(str(number), 1, num_color)
		self.screen.blit(label, (x, y))

	def __update_screen(self):
		self.screen.blit(self.picture, (0, 0))
		for row in range(len(self.board)):
			for column in range(len(self.board)):
				if self.board[row][column] != 0:
					self.__draw_number(self.board[row][column], row, column)
		pygame.display.update()


if __name__ == "__main__":
	obj = G2048()
	obj.run_game()