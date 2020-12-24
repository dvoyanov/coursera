class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        len_1 = len(grid)
        len_2 = len(grid[0])
        lights = []
        obstacles = []
        for i in range(len_1):
            for j in range(len_2):
                if grid[i][j] == 1:
                    lights.append((j, i))
                elif grid[i][j] == -1:
                    obstacles.append((j, i))
        self.adaptee.set_dim((len_2, len_1))
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        return self.adaptee.generate_lights()

