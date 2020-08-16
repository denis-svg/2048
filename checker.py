from grabber import Grabber
from os import stat, remove
from settings import Settings
import pygame


class Checker:
    @staticmethod
    def checkingMissingImages():
        try:
            if stat("board.png").st_size > 0:
                """if the image is found then check height and width to make sure it's not an board from different 
                game """
                image = pygame.image.load("board.png")
                current_width, current_height = image.get_width(), image.get_height()
                if current_width != Settings.COLS * 15 + (Settings.COLS + 1) * 2 or current_height != Settings.ROWS * 15 + (Settings.ROWS + 1) * 2:
                    """If the board it is from different game then delete it and make the new one"""
                    remove("board.png")
                    Grabber.makeBoardImage()
        except OSError:
            """if there is no board then make one"""
            Grabber.makeBoardImage()

        current_number = 2
        while current_number <= 524288:
            try:
                if stat(str(current_number) + ".png").st_size > 0:
                    """if the image is found then check height and width to make sure it's not a number from different 
                                    game """
                    image = pygame.image.load(str(current_number) + ".png")
                    current_width, current_height = image.get_width(), image.get_height()
                    if current_width != Settings.image_width or current_height != Settings.image_height:
                        """If the number it is from different game then delete it and make the new one"""
                        remove(str(current_number) + ".png")
                        Grabber.makeNumberImage(current_number)
            except OSError:
                """if there is no number then make one"""
                Grabber.makeNumberImage(current_number)
            current_number *= 2

    @staticmethod
    def initImages():
        """Put every number image in a dict then return it"""
        images = {}
        current_number = 2
        while current_number <= 524288:
            images[str(current_number)] = pygame.image.load(str(current_number) + ".png")
            current_number *= 2

        return images
