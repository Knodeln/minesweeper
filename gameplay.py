import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Minesweeper')
font = pygame.font.Font('freesansbold.ttf', 12)
bombImg = pygame.image.load('bomb.png')


def neighbors(matrix, rowNumber, colNumber):
    result = []
    for rowAdd in range(-1, 2):
        newRow = rowNumber + rowAdd
        if newRow >= 0 and newRow <= len(matrix) - 1:
            for colAdd in range(-1, 2):
                newCol = colNumber + colAdd
                if newCol >= 0 and newCol <= len(matrix) - 1:
                    if newCol == colNumber and newRow == rowNumber:
                        continue
                    result.append(matrix[newCol][newRow])
    return result


def init_world():
    world = np.random.choice((-1, 0), (25, 25), p=[0.25, 0.75])
    list_world = world.tolist()
    for x in range(len(list_world)):
        for y in range(len(list_world)):
            if list_world[y][x] == -1:
                continue
            else:
                temp = neighbors(list_world, x, y)
                i = temp.count(-1)
                list_world[y][x] = i
    return list_world


def click_matrix():
    return np.zeros((25, 25), int)


def render_world(world):
    running = True
    square = pygame.Surface((20, 20))
    square.fill((100, 100, 100))
    clicked = click_matrix()
    print(world)
    while running:
        screen.fill((255, 255, 255))
        for x in range(len(world)):
            for y in range(len(world)):
                screen.blit(square, (y * 20, x * 20))
                rect = pygame.Rect(y * 20, x * 20, 20, 20)
                pygame.draw.rect(screen, (0, 0, 0), rect, 2)

                if world[y][x] > 0 and clicked[y][x] == 1:
                    text = font.render(str(world[y][x]), True, (50, 150, 50))
                    screen.blit(text, ((y * 20) + 7, (x * 20) + 4))
                if world[y][x] < 0 and clicked[y][x] == 1:
                    screen.blit(bombImg, (y * 20, x * 20))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked[int(pos[0] / 20)][int(pos[1] / 20)] = 1

            if event.type == pygame.QUIT:
                running = False


def minesweeper():
    world = init_world()
    render_world(world)


if __name__ == "__main__":
    minesweeper()
