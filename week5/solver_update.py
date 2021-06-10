#!/usr/bin/env python3

import sys
import math


def read_input(filename):
    with open(filename) as f:
        cities = []
        for line in f.readlines()[1:]:  # Ignore the first line.
            xy = line.split(',')
            coordinates = [float(xy[0]), float(xy[1])]
            cities.append(coordinates)
        return cities


def format_tour(tour):
    return 'index\n' + '\n'.join(map(str, tour))


def print_tour(tour):
    print(format_tour(tour))


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

    return (a*b < 0) and (c*d < 0)


def solve_cross(cities, tour):
    print("test solve_cross")
    N = len(tour)
    #tourに入っている順で見たい
    for i in range(N-1):
        print("-----------i = ",i)
        for j in range(N-1):
            print("j = ",j)
            if j > i:
                if abs(j -i) <= 1:
                    print("1-2")
                    continue
            elif j <= i:
                if abs(j -i) <= 1:
                    print("1-3")
                    continue
            elif i == 0 and j == N-1:
                print("1-4")
                continue
            elif i == N-1 and j == 0:
                print("1-5")
                continue
            if find_cross(cities, tour[i], tour[i + 1], tour[j], tour[j+1]):
                print("find cross")
                swap_cross(tour, i, j+1)
                print("swaped cross")
    return tour


def swap_cross(tour, city1_index, city4_index):
    path = []
    for i in range(city1_index+1, city4_index):
        print("sw_i = ", i)
        path.append(tour[i])
        print("path1",path)
    for i in range(math.floor(len(path)/2)):
        print("swap")
        tmp = path[i]
        path[i] = path[len(path)-1-i]
        path[len(path)-1-i]  = tmp
        print("path2",path)
    tour[city1_index+1 : city4_index] = path

def test_find_cross(cities,tour):
    print("test_find_cross")
    print(find_cross(cities, tour[8], tour[9], tour[10], tour[11]))
    print(find_cross(cities ,tour[12], tour[13], tour[15], tour[0]))

if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = greedy(read_input(sys.argv[1]))
    test_find_cross(read_input(sys.argv[1]), tour)
    tour = solve_cross(read_input(sys.argv[1]), tour)
    print_tour(tour)

