#!/usr/bin/env python3

import sys
import math

from common import print_tour, read_input  # @UnresolvedImport


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
    return tour


def find_cross(cities, city1, city2, city3, city4):
    a = (cities[city1][0] - cities[city2][0]) * (cities[city3][1] - cities[city1][1])
    + (cities[city1][1] - cities[city2][1]) * (cities[city3][0] - cities[city1][0])
    b = (cities[city1][0] - cities[city2][0]) * (cities[city4][1] - cities[city1][1])
    + (cities[city1][1] - cities[city2][1]) * (cities[city4][0] - cities[city1][0])
    c = (cities[city3][0] - cities[city4][0]) * (cities[city1][1] - cities[city3][1])
    + (cities[city3][1] - cities[city4][1]) * (cities[city1][0] - cities[city3][0])
    d = (cities[city3][0] - cities[city4][0]) * (cities[city2][1] - cities[city3][1])
    + (cities[city3][1] - cities[city4][1]) * (cities[city2][0] - cities[city3][0])

    return a*b < 0 and c*d < 0


def swap_cross(cities):

    return tour


def test_find_cross(cities,tour):
    N = len(cities)

    for i in range(N-2):
        for j in range(i+2, N-2):
            print("i = ",i)
            print("tour i = ", tour[i])
            print("tour i+1 = ", tour[i+1])
            print("j = ",j)
            print("tour j = ", tour[j])
            print("tour j+1 = ", tour[j+1])
            if (i != N-2) and (j == N-2):
                print(find_cross(cities, tour[i], tour[i+1], tour[j], tour[0]))
            else:
                print(find_cross(cities ,tour[i], tour[i+1], tour[j], tour[j + 1]))

if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = greedy(read_input(sys.argv[1]))
    print_tour(tour)
    test_find_cross(read_input(sys.argv[1]), tour)
