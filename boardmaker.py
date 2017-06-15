import pygame
import math
import re


class Board(object):
    def __init__(self, size, rect):
        self.array = []
        self.size = size
        self.rect = rect

    def populate(self):
        for i in range(self.size):
            self.array.append([])
            for g in range(self.size):
                if i == 0 or g == 0 or i == self.size - 1 or g == self.size - 1:
                    if (g == 1 and i == 0) or (g == self.size - 2 and i == self.size - 1):
                        self.array[i].append(0)  # Start and end locations
                    else:
                        self.array[i].append(1)
                else:
                    self.array[i].append(1)

    def loadgraph(self):  # Loads the graph from the maze.pl file
        f = open("maze.pl", "r")
        for i in range(self.size):
            for j in range(self.size):
                x = f.readline()
                x = re.search("(\d+),(\d+),(\d+)", x)  # board((g1),(g2),(g3))
                self.array[int(x.group(2))][int(x.group(1))] = int(x.group(3))
        f.close()

    def graph(self, surface):  # Draws the maze to the screen
        mult = math.floor(self.rect[0] / self.size)
        for i in range(self.size):  # Draw the cells
            for g in range(self.size):
                if int(self.array[g][i]) == 1:  # Wall
                    pygame.draw.rect(surface, (43, 149, 197), ((i * mult, g * mult), (mult, mult)))
                else:  # Empty
                    pygame.draw.rect(surface, (220, 234, 241), ((i * mult, g * mult), (mult, mult)))

        for i in range(self.size):  # Draw the lines to divide cells
            for g in range(self.size):
                pygame.draw.line(surface, (0, 0, 0), (i * mult, 0), (i * mult, self.rect[0]), 1)
                pygame.draw.line(surface, (0, 0, 0), (0, g * mult), (self.rect[0], g * mult), 1)

    def change_pos(self, pos, bool):
        if bool:
            self.array[pos[1]][pos[0]] = 0
        else:
            self.array[pos[1]][pos[0]] = 1

    def display(self):
        for i in self.array:
            for g in i:
                print g,
            print "\n"

    def ret_prolog(self):
        f = open("maze.pl", "w")
        for j, i in enumerate(self.array):
            for g, h in enumerate(i):
                if (int(g) == 1 and int(j) == 0) or (int(g) == self.size - 2 and int(j) == self.size - 1):
                    pass
                else:
                    f.write("board(%d,%d,%d). \n" % (int(g), int(j), int(h)))
        f.write("start(1,0,0). \n")
        f.write("board(%d,%d,%d). \n" % (self.size - 2, self.size - 1, 0))

        f.close()


def get_tile(pos, size, rect):
    mult = math.floor(rect / size)
    x = int(pos[0] // mult)
    y = int(pos[1] // mult)
    return x, y


def main():
    pygame.init()
    done = False
    size = (900, 900)  # Width and height of the window
    screen = pygame.display.set_mode(size)

    dimensions = 20  # Size of the maze
    maze = Board(dimensions, size)
    maze.populate()

    while not done:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Escape to close program
                    done = True

                if event.key == pygame.K_SPACE:  # Space to save the grid to maze.pl file
                    maze.ret_prolog()

                if event.key == pygame.K_l:  # L to load from the maze.pl file
                    maze.loadgraph()

        if pygame.mouse.get_pressed()[0]:  # Hold left click to remove walls
            position = (get_tile(pos, dimensions, size[0]))
            maze.change_pos(position, True)

        if pygame.mouse.get_pressed()[2]:  # Hold right click to add walls
            position = (get_tile(pos, dimensions, size[0]))
            maze.change_pos(position, False)

        screen.fill((0, 0, 0))
        maze.graph(screen)
        pygame.display.flip()


pygame.quit()

if __name__ == '__main__':
    main()
