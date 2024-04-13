import pygame

from VATTUBOY.resources.resource import Resource

class SpriteSheet(Resource):
    def __init__(self, name, source_file, sprite_width, sprite_height):
        super().__init__(name)
        self.__source_file = self._check_source(source_file)
        self.__sheet = None
        self.__sprite_width = sprite_width
        self.__sprite_height = sprite_height

        self.__sprites_on_row = 0
        self.__sprites_on_column = 0

        self.__sprites = []

        self.__open_sheet()

    def __open_sheet(self):
        self.__sheet = pygame.image.load(self.__source_file).convert()

        self.__load_sprites()

    def __load_sprites(self):
        self.__sprites_on_row = int(self.__sheet.get_width()/self.__sprite_width)
        self.__sprites_on_column = int(self.__sheet.get_height()/self.__sprite_height)

        for i in range(0, self.__sprites_on_row):
            for j in range(0, self.__sprites_on_column):
                x = i*self.__sprite_width
                y = j*self.__sprite_height

                self.__sprites.append(self.__load_sprite_at(x, y))

    def get_sprite(self, sprite_index):
        return self.__sprites[sprite_index]

    def __load_sprite_at(self, x, y):
        rect = pygame.Rect(x, y, self.__sprite_width, self.__sprite_height)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.__sheet, (0, 0), rect)
        image.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        return image

