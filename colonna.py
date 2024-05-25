class Colonna():

    def __init__(self, screen, image):
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = 750
        self.rect.bottom = 448
        self.centerx = float(self.rect.centerx)
