import pygame
import singletons

class _menuItem:
    def __init__(self, text, defaultColor, selectedColor, pos, description, fontSize = 48):  # текст по умолчанию, текст выделенный, расположение, описание, размер шрифта
        font = pygame.font.Font('fonts/Arial.ttf', fontSize)  # СКАЧАТЬ и установить шрифты papercut.ttf !
                                                        # создаём объект front для получения шрифта, через вызов Font у пигейма
        self.__pos = pos  # положение элемента меню
        self.__index = 0 # для ориентации в меню(выделение)
        self.__description = description
        self.__items = (font.render(text, True, defaultColor),   # кортеж для выбора цвета в меню
                        font.render(text, True, selectedColor))

    def select(self): # срабатывает при выборе элемента меню
        self.__index = 1

    def deselect(self):
        self.__index = 0

    def getItemData(self):
        return self.__items[self.__index], self.__pos

    @property
    def description(self)
        return self.__description


class Menu:
    defaultColor = (32, 68, 71) # цвет элемента меню по умолчанию
    selectedColor = (100, 19, 16)  # цвет элемента меню выбранного

    def __init__(self):
        self.__items = [] # Список []
        self.__display = singletons.Display().getInstance() # импортируем дисплей из сингелтона

        self.__center_x = self.__display.getScreenResolution[0] / 2 - 100
        self.__center_y = self.__display.getScreenResolution[1] / 2 - 100













