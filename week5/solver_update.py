#!/usr/bin/env python3

import sys
import math

from common import print_tour, read_input  # @UnresolvedImport
from pickle import TRUE


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def greedy(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city
        print_tour(tour)
    return tour


def find_cross(cities, city1, city2, city3, city4):
    print(cities[city1][0])
    print(cities[city1][1])
    print(cities[city2][0])
    print(cities[city2][1])
    print(cities[city3][0])
    print(cities[city3][1])
    print(cities[city4][0])
    print(cities[city4][1])

    a = (cities[city1][0] - cities[city2][0]) * (cities[city3][1] - cities[city1][1])
    + (cities[city1][1] - cities[city2][1]) * (cities[city1][0] - cities[city3][0])
    b = (cities[city1][0] - cities[city2][0]) * (cities[city4][1] - cities[city1][1])
    + (cities[city1][1] - cities[city2][1]) * (cities[city1][0] - cities[city4][0])
    c = (cities[city3][0] - cities[city4][0]) * (cities[city1][1] - cities[city3][1])
    + (cities[city3][1] - cities[city4][1]) * (cities[city3][0] - cities[city1][0])
    d = (cities[city3][0] - cities[city4][0]) * (cities[city2][1] - cities[city3][1])
    + (cities[city3][1] - cities[city4][1]) * (cities[city3][0] - cities[city2][0])

    return a*b < 0 and c*d < 0


def swap_cross(cities, city1, city2, city3, city4):
    tmp = city2
    city2 = city3
    city3 = tmp


def is_cross(cities, tour):
    N = len(cities)
    for i in range(N):
        for j in range(i, N):
            if find_cross(cities, , , , ):
                return True
    return False


def solve(cities):
    while is_cross:
        find_cross(cities, , , , )
        swap_cross(cities, city1, city2, city3, city4):

    return tour


def test_find_cross(cities,tour):
    print("debug")
    print(tour[8])
    print(tour[9])
    print(tour[10])
    print(tour[11])
    print(tour[12])
    print(tour[13])
    print(tour[15])
    print(tour[0])
    print(find_cross(cities, tour[8], tour[9], tour[10], tour[11]))
    print(find_cross(cities ,tour[12], tour[13], tour[15], tour[0]))

if __name__ == '__main__':
    assert len(sys.argv) > 1
    tourrrrrr = greedy(read_input(sys.argv[1]))
    tour = solve()
    test_find_cross(read_input(sys.argv[1]), tour)
