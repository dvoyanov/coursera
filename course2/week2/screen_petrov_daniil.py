#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Vec2d:
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

    def __sub__(self, other):
        return Vec2d((self.x - other.x, self.y - other.y))

    def __add__(self, other):
        return Vec2d((self.x + other.x, self.y + other.y))

    def __len__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __mul__(self, k):
        return Vec2d((self.x * k, self.y * k))

    def int_pair(self):
        return self.x, self.y


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []

    def add(self, point, speed):
        self.points.append(point)
        self.speeds.append(speed)

    def remove(self):
        if self.points:
            self.points.pop()
            self.speeds.pop()

    def set_points(self):
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + Vec2d(self.speeds[p])
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p] = (-self.speeds[p][0], self.speeds[p][1])
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p] = (self.speeds[p][0], -self.speeds[p][1])

    def draw_points(self, width=3, color=(255, 255, 255)):
        for p in self.points:
            pygame.draw.circle(gameDisplay, color, (int(p.x), int(p.y)), width)


class Knot(Polyline):
    def draw_points_knot(self, steps, width=3, color=(255, 255, 255)):
        points2 = self.get_knot(steps)
        for p_n in range(-1, len(points2) - 1):
            pygame.draw.line(gameDisplay, color,
                             (int(points2[p_n].x), int(points2[p_n].y)),
                             (int(points2[p_n + 1].x), int(points2[p_n + 1].y)),
                             width)

    def get_knot(self, count):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)
            res.extend(self.get_points(ptn, count))
        return res

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + self.get_point(points, alpha, deg - 1) * (1 - alpha)

    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res


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
    data.append(["A", "Add new knot"])
    data.append(["D", "Delete latest knot"])
    data.append(["X", "Delete latest point"])
    data.append(["Q", "Speed up (max 5)"])
    data.append(["W", "Speed down (min 1)"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [(0, 0), (800, 0), (800, 600), (0, 600)])
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")
    font = pygame.font.SysFont("courier", 24)

    steps = 35
    working = True
    knots = [Knot()]
    show_help = False
    pause = True
    speed_inc = 1

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    knots = [Knot()]
                if event.key == pygame.K_a:
                    knots.append(Knot())
                if event.key == pygame.K_d:
                    if len(knots) > 1:
                        knots.pop()
                if event.key == pygame.K_x:
                    knots[len(knots) - 1].remove()
                if event.key == pygame.K_q:
                    if speed_inc < 5:
                        speed_inc += 1
                        for knot in knots:
                            knot.speeds = [(speed[0] / (speed_inc - 1) * speed_inc, speed[1] / (speed_inc - 1) * speed_inc) for speed in knot.speeds]
                if event.key == pygame.K_w:
                    if speed_inc > 1:
                        speed_inc -= 1
                        for knot in knots:
                            knot.speeds = [(speed[0] / (speed_inc + 1) *  speed_inc, speed[1] / (speed_inc + 1) * speed_inc) for speed in knot.speeds]
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                knots[len(knots) - 1].add(Vec2d(event.pos), (random.random() * 2 * speed_inc, random.random() * 2 * speed_inc))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        gameDisplay.blit(font.render(f'knots: {len(knots)}', True, (128, 128, 255)), (0, 0))
        gameDisplay.blit(font.render(f'speed: x{speed_inc}', True, (128, 128, 255)), (0, 30))
        for knot in knots:
            knot.draw_points()
            knot.draw_points_knot(steps, 3, color)
        if not pause:
            for knot in knots:
                knot.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
