from grabber import Grabber
from os import stat, remove
from settings import Settings
import pygame


class Checker:
    @staticmethod
    def checkingMissingImages():
        current_number = 2
        while current_number <= 524288:
            try:
                if stat(str(current_number) + ".png").st_size > 0:
                    image = pygame.image.load(str(current_number) + ".png")
                    current_width, current_height = image.get_width(), image.get_height()
                    if current_width != Settings.image_width and current_height != Settings.image_height:
                        remove(str(current_number) + ".png")
                        Grabber.make_image(current_number)
            except OSError:
                Grabber.make_image(current_number)
            current_number *= 2

    @staticmethod
    def initImages():
        images = {}
        current_number = 2
        while current_number <= 524288:
            images[str(current_number)] = pygame.image.load(str(current_number) + ".png")
            current_number *= 2

        return images
