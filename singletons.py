import pygame
class Display:
    __instance = None                # два __ - приватный

    __SCREEN_RESOLUTION = (400, 400) # размер окна; type: tuple(int, int) - кортеж
    __BG_COLOR = (0, 0, 0)           # черный цвет
    __FPS = 30                       # число кадров с секунду

    def __init__(self):              # в функции __init__ устанавливаем режим дисплея; конструктор
        self.__surface = None        # переменная

    def init(self):                  # функция инициализирует экран
        if self.__surface is None:    # если surface is None , то
            self.__surface = pygame.display.set_mode(self.__SCREEN_RESOLUTION) # установили режим (set_mode)
                                                                               # и передали наше разрешение экрана (self.__SCREEN_RESOLUTION)
    @classmethod                     # функция статична
    def getInstance(cls):
        if cls.__instance is None:   # если instance пустой то
            cls.__instance = Display() # создаём объект
        return cls.__instance

    @property
    def getScreenResolution(self):   # функция
        return self.__SCREEN_RESOLUTION # возвращает разрешение экрана

    @property
    def getBGColor(self):
        return self.__BG_COLOR

    @property
    def getFPS(self):
        return self.__FPS

    @property
    def getSurface(self):
        return self.__surface

