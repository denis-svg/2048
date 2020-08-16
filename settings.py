class Settings:
    """you can modify only screen height and width and it's preferable to be a multiply of (ROWS * 15 + (ROWS + 1) * 2)
    and (COLS + 1) * 2)"""
    screen_width = 560
    screen_height = 560
    ROWS, COLS = 8, 8
    COEFICIENT_X = screen_width / (ROWS * 15 + (ROWS + 1) * 2)
    COEFICIENT_Y = screen_height / (COLS * 15 + (COLS + 1) * 2)
    image_width = round(15 * COEFICIENT_X)
    image_height = round(15 * COEFICIENT_Y)
    boarder_width = round(2 * COEFICIENT_X)
    boarder_height = round(2 * COEFICIENT_Y)
