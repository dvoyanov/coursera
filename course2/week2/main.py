#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    """класс 2-х мерного вектора с начальными координатами в точке (0, 0)"""
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]

    def __add__(self, other):
        """возвращает сумму двух векторов"""
        return Vec2d((self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        """"возвращает разность двух векторов"""
        return Vec2d((self.x - other.x, self.y - other.y))

    def __mul__(self, other):
        """возвращает произведение вектора на число"""
        return Vec2d((self.x * other, self.y * other))

    def __len__(self):
        """возвращает длину вектора"""
        return math.sqrt(self.x * self.x + self.y * self.y)

    def int_pair(self):
        return int(self.x), int(self.y)


class Polyline:
    """Класс замкнутых ломаных"""
    def __init__(self, gameDisplay, width=3, color=(255, 255, 255)):
        self.points = []
        self.speeds = []
        self.gameDisplay = gameDisplay
        self.width = width
        self.color_point = color

    def change_speed(self, step):
        """Изменение скорости"""
        for i in range(len(self.speeds)):
            self.speeds[i] *= step

    def append_point(self, point, speed):
        """Добавление новой точки со скоростью"""
        self.points.append(Vec2d(point))
        self.speeds.append(Vec2d(speed))

    def delete_point(self):
        """Удаление последней добавленной точки"""
        if len(self.points) > 0:
            self.points.pop()
            self.speeds.pop()


    def set_points(self):
        """Изменение скорости в случае достижения края экрана"""
        for p in range(len(self.points)):
            self.points[p] += self.speeds[p]
            if self.points[p].x > self.gameDisplay.get_width() or self.points[p].x < 0:
                self.speeds[p].x = - self.speeds[p].x
            if self.points[p].y > self.gameDisplay.get_height() or self.points[p].y < 0:
                self.speeds[p].y = - self.speeds[p].y

    def draw_points(self):
        """Рисование точек"""
        for p in self.points:
            pygame.draw.circle(self.gameDisplay, self.color_point, p.int_pair(), self.width)


class Knot(Polyline):
    """Класс замкнутых кривых"""
    def __init__(self, gameDisplay, steps, width=3, color=(255, 255, 255)):
        super().__init__(gameDisplay, width)
        self.color_line = color
        self.steps = steps
        self.alpha = 1/steps

    def set_steps(self, step):
        if self.steps + step > 0:
            self.steps += step
            self.alpha = 1/self.steps

    def get_point(self, base_points, alpha, deg=None):
        if deg is None:
            deg = len(base_points) - 1
        if deg == 0:
            return base_points[0]
        return base_points[deg]*alpha + self.get_point(base_points, alpha, deg - 1)*(1 - alpha)

    def get_points(self, base_points):
        res = []
        for i in range(self.steps):
            res.append(self.get_point(base_points, i * self.alpha))
        return res

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = [(self.points[i] + self.points[i + 1]) * 0.5, self.points[i + 1],
                   (self.points[i + 1] + self.points[i + 2]) * 0.5]

            res.extend(self.get_points(ptn))
        return res

    def draw_points(self):
        super().draw_points()
        points_knot = self.get_knot()
        for p_n in range(-1, len(points_knot) - 1):
            pygame.draw.line(self.gameDisplay, self.color_line, points_knot[p_n].int_pair(),
                             points_knot[p_n + 1].int_pair(), self.width)


def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["F11", "Up speed"])
    data.append(["F12", "Down speed"])
    data.append(["DEL", "Delete last point"])
    data.append(["", ""])
    data.append([str(knot.steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    knot = Knot(gameDisplay, steps, 3, color)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    knot = Knot(gameDisplay, steps, 3, color)
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    knot.set_steps(1)
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_F11:
                    knot.change_speed(0.9)
                if event.key == pygame.K_F12:
                    knot.change_speed(1.1)
                if event.key == pygame.K_KP_MINUS:
                    knot.set_steps(-1) if steps > 1 else 0
                if event.key == pygame.K_DELETE:
                    knot.delete_point()
            if event.type == pygame.MOUSEBUTTONDOWN:
                knot.append_point(event.pos, (random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        knot.draw_points()
        if not pause:
            knot.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
