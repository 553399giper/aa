import pygame
import singletons # подключаем модуль

def main():
    pygame.init()

    Display = singletons.Display().getInstance() # получаем наш объект создав переменную Display
    Display.init() # устанавливаем наш экран в определённый режим (с разрешением 400*400)

    done = False  # пока done не станет True, будут крутится цикл while
    clock = pygame.time.Clock()
    while not done:
        Display.getSurface.fill(Display.getBGColor) # функция fill действует как(?); наше полотно экрана заполняется черным цветом
        events = pygame.event.get() # на каждой операции цикла запрашиваем какие события произошли

        for event in events:
            if event.type == pygame.QUIT:   # ЕСТЬ ЛИ СОБЫТИЯ ВЫХОДА ИЗ ИГРЫ
                done = True  # если есть то завершаем цикл

        pygame.display.update() # Обновить экран
        clock.tick(Display.getFPS) # tick рассчитает сколько миллисекунд нужно при 30к/с

    pygame.quit()  # завершаем движок pygame

main()
