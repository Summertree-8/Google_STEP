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

    '''
    Equation of a line between city1 and city2
    y = (city1_y - city2_y)/(city1_x - city2_x)・x + city1_y - (city1_y - city2_y)/(city1_x - city2_x)・city1_x
    <=>
    y・(city1_x - city2_x) = (city1_y - city2_y)・x + city1_y(city1_x - city2_x) - (city1_y - city2_y)・city1_x
    <=>
    (city1_x - city2_x)("y" -city1_y) + (city1_y - city2_y)(city1_x - "x") = 0

    input coordinates of city3
    A: (city1_x - city2_x)("city3_y "-city1_y) + (city1_y - city2_y)(city1_x - "city3_x") = 0

    input coordinates of city4
    B: (city1_x - city2_x)("city4_y "-city1_y) + (city1_y - city2_y)(city1_x - "city4_x") = 0

    if city3 and city 4 are on different sides of line between city1 and city2,
    A*B < 0

    '''
    a = (cities[city1][0] - cities[city2][0]) * (cities[city3][1] - cities[city1][1])\
    + (cities[city1][1] - cities[city2][1]) * (cities[city1][0] - cities[city3][0])

    b = (cities[city1][0] - cities[city2][0]) * (cities[city4][1] - cities[city1][1])\
    + (cities[city1][1] - cities[city2][1]) * (cities[city1][0] - cities[city4][0])

    c = (cities[city3][0] - cities[city4][0]) * (cities[city1][1] - cities[city3][1])\
    + (cities[city3][1] - cities[city4][1]) * (cities[city3][0] - cities[city1][0])

    d = (cities[city3][0] - cities[city4][0]) * (cities[city2][1] - cities[city3][1])\
    + (cities[city3][1] - cities[city4][1]) * (cities[city3][0] - cities[city2][0])

    print("a = ",a)
    print("b = ",b)
    print("c = ",c)
    print("d = ",d)

    return (a*b < 0) and (c*d < 0)


def swap_cross(cities, city1, city2, city3, city4):
    tmp = city2
    city2 = city3
    city3 = tmp


def is_cross(cities, tour):
    N = len(cities)
    for i in range(N):
        print("hey")
        print(i)
#         j = i + 2
#         if i == N-2:
#                 x = N-1
#                 y = N
#                 z = 0
#         elif i == N-1:
#                 x = N
#                 y = 0
#                 z = 1
#         elif i == N:
#                 x = 0
#                 y = 1
#                 z = 2
#         else:
#                 x = i + 1
#                 y = j
#                 z = j + 1
#         print("x = ", x)
#         print("y = ", y)
#         print("z = ", z)
        for j in range(i+2 , i-2):
            print("hello")
            if find_cross(tour, i, i + 1, j, j+1):
                return True
    return False


# def solve(cities, tour):
#     while is_cross:
#         find_cross(cities, , , , )
#         swap_cross(cities, city1, city2, city3, city4):
#
#     return tour


# def test_find_cross(cities,tour):
#     print("test_find_cross")
#     print(tour[8])
#     print(tour[9])
#     print(tour[10])
#     print(tour[11])
#     print(tour[12])
#     print(tour[13])
#     print(tour[15])
#     print(tour[0])
#     print(find_cross(cities, tour[8], tour[9], tour[10], tour[11]))
#     print(find_cross(cities ,tour[12], tour[13], tour[15], tour[0]))

if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = greedy(read_input(sys.argv[1]))
    print(is_cross(read_input(sys.argv[1]), tour))
#     tour = solve()
#     test_find_cross(read_input(sys.argv[1]), tour)
