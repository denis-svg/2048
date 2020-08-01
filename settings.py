class Settings:
    """you can modify only screen height and width and it's preferable to be a multiply of 70"""
    screen_width = 560
    screen_height = 560
    COEFICIENT_X = screen_width / 70
    COEFICIENT_Y = screen_height / 70
    image_width = round(15 * COEFICIENT_X)
    image_height = round(15 * COEFICIENT_Y)
    boarder_width = round(2 * COEFICIENT_X)
    boarder_height = round(2 * COEFICIENT_Y)
