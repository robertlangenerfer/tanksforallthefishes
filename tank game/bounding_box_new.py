class bounding_box:  # class for bounding box

    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def collision(A, B):
        if (abs(B.x - A.x) <= ((A.width + B.width) / 2)) and (abs(B.y - A.y) <= (A.height + B.height)/2):
            return True
        else:
            return False








