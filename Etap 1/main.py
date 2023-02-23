import re
import numpy
from itertools import permutations
import time


def main_menu_interface():
    n = 1
    while n == 1:
        print("(0) End program")
        print("(1) Bruteforce algorithm")
        print("(2) Held karp algorithm")
        print("Please select which algorith do you want to test: ")
        choice = input()
        if choice == "0":
            break
        elif choice == "1":
            bruteforce_menu_interface()
        elif choice == "2":
            help_karp_menu_interface()
        else:
            print("Incorrect value, please try again!")


def bruteforce_menu_interface():
    print("Bruteforce algorithm")
    n = 1
    while n == 1:
        print("(0) Return to previous menu")
        print("(1) Load graph from file")
        print("(2) Generate random graph")
        print("(3) Display graph")
        print("(4) Perform algorithm")
        print("(5) Perform automatic test")
        print("Please select option: ")
        choice = input()
        if choice == "0":
            break
        elif choice == "1":
            print("Loading graph from file")
            print("Please provide file name: ")
            file_name = input()
            matrix = load_graph(file_name)
        elif choice == "2":
            print("Generating random graph")
            print("Please provide number of cities: ")
            city_number = input()
            matrix = generate_graph(city_number)
        elif choice == "3":
            print("Displaying graph")
            display_graph(matrix)
        elif choice == "4":
            print("Performing algorithm")
            result = brute_force_algorithm(matrix)
            print("Result")
            print(result)
        elif choice == "5":
            print("Performing automatic test")
            brute_force_automatic_test()
        else:
            print("Incorrect value, please try again!")


def help_karp_menu_interface():
    print("Held karp algorithm")
    n = 1
    while n == 1:
        print("(0) Return to previous menu")
        print("(1) Load graph from file")
        print("(2) Generate random graph")
        print("(3) Display graph")
        print("(4) Perform algorithm_v1")
        print("(5) Perform algorithm_v2")
        print("(6) Perform automatic test")
        print("Please select option: ")
        choice = input()
        if choice == "0":
            break
        elif choice == "1":
            print("Loading graph from file")
            print("Please provide file name: ")
            file_name = input()
            matrix = load_graph(file_name)
        elif choice == "2":
            print("Generating random graph")
            print("Please provide number of cities: ")
            city_number = input()
            matrix = generate_graph(city_number)
        elif choice == "3":
            print("Displaying graph")
            display_graph(matrix)
        elif choice == "4":
            print("Performing algorithm")
            result = held_karp_algorithm_v1(matrix)
            print("Result")
            print(result)
        elif choice == "5":
            print("Performing algorithm")
            result = held_karp_algorithm_v2(matrix)
            print("Result")
            print(result)
        elif choice == "6":
            print("Performing automatic test")
            held_karp_automatic_test()
        else:
            print("Incorrect value, please try again!")


def load_graph(file_path: str):
    # Wczytanie linii z pliku
    graph = open(file_path).readlines()

    # Usuwanie pustych przestrzeni
    graph_stripped = []
    for line in graph[1:]:
        single_line = re.sub(' +', ' ', line.strip())
        graph_stripped.append(single_line)

    # Usuwanie pustych lini oraz wstawienie wartości do macierzy
    matrix = []
    for line in graph_stripped:
        if line.strip() != '':
            value_list = line.split(' ')

            matrix_row = []
            for value in value_list:
                matrix_row.append(int(value))

            matrix.append(matrix_row)

    return matrix


def generate_graph(city_number: int):
    matrix = numpy.random.randint(1, 107, size=(int(city_number), int(city_number)))
    numpy.fill_diagonal(matrix, -1)
    return matrix


def display_graph(matrix: int):
    matrix = numpy.array(matrix)
    print(matrix)


def brute_force_algorithm(matrix: int):
    #Miejsce w którym będziemy przechowywać wynik
    result = (float('inf'),)

    # Dla każdej permutacji zbioru miast wykonujemy następujące operacje
    for permutation in permutations(range(len(matrix))):
        permutation += (permutation[0],)

        #Obliczamy całkowity koszt podróży dla danej permutacji zbioru
        cost = 0
        for i in range(len(permutation) - 1):
            cost += matrix[permutation[i]][permutation[i + 1]]

        #Jeżeli koszt jest niższy od poprzedniego to zapisujemy wynik (koszt oraz ścieżkę) w result
        if cost < result[0]:
            result = (cost, permutation)

    #Po zakończeniu pętli zwracamy result
    return result


def algorithm_v1(current_city: int, unvisited_cities: int, matrix: int):

    # Jeżeli wszystkie miasta zostały odwiedzone rozpoczynamy zwijanie rekurencji
    if len(unvisited_cities) == 0:
        # Zwracamy koszt podróży od naszego aktualnego miasta do miasta początkowego
        return matrix[current_city][0]

    all_possible_paths = []
    # Dla każdego nie odwiedzonego miasta wykonujemy następujące operacje
    for next_city in unvisited_cities:
        # Do listy wszystkich możliwych ścieżek dodajemy koszt podróży z miasta w którym aktualnie jesteśmy oraz wywołujemy ponownie
        # naszą funkcję, która zwróci nam koszt podróży do kolejnych miast.
        cost = matrix[current_city][next_city] + algorithm_v1(next_city, unvisited_cities - {next_city}, matrix)
        all_possible_paths.append(cost)

    # Zwracamy minimalną wartość z listy wszystkich możliwych ścieżek z danego miasta
    result = min(all_possible_paths)

    return result


def held_karp_algorithm_v1(matrix: int):

    # Obliczamy ilość miast oraz wszystke nie odwiedzone jeszcze miasta
    matrix_length = len(matrix)
    unvisited_cities = set(range(1, matrix_length))

    # Pierwsze wywołanie funkcji rekurancyjnej (jako argumenty podajemy miasto startowe, wszystkie nie odwiedzone miasta macierz)
    result = algorithm_v1(0, unvisited_cities, matrix)

    return result


def algorithm_v2(current_city: int, unvisited_cities: int, matrix: int):

    # Jeżeli wszystkie miasta zostały odwiedzone rozpoczynamy zwijanie rekurencji
    if len(unvisited_cities) == 0:
        # Zwracamy koszt podróży od naszego aktualnego miasta do miasta początkowego
        path = [0, current_city]
        result = [matrix[current_city][0], path]
        return result

    all_possible_paths = []
    # Dla każdego nie odwiedzonego miasta wykonujemy następujące operacje
    for next_city in unvisited_cities:
        # Do listy wszystkich możliwych ścieżek dodajemy koszt podróży z miasta w którym aktualnie jesteśmy oraz wywołujemy ponownie
        # naszą funkcję, która zwróci nam koszt podróży do kolejnych miast.
        current_cost = matrix[current_city][next_city]
        next_cost = algorithm_v2(next_city, unvisited_cities - {next_city}, matrix)
        cost = current_cost + next_cost[0]
        path = next_cost[1] + [current_city]
        all_possible_paths.append([cost, path])

    # Konwertujemy tablicę na tablicę numpy w celu wyszukania najkrótszej ścieżki.
    all_possible_paths_numpy = numpy.array(all_possible_paths, dtype=object)

    # Zwracamy minimalną wartość podróży oraz ścieżkę z listy wszystkich możliwych ścieżek z danego miasta
    result = all_possible_paths_numpy[numpy.argmin(all_possible_paths_numpy[:, 0]), :]

    return result


def held_karp_algorithm_v2(matrix: int):

    # Obliczamy ilość miast oraz wszystke nie odwiedzone jeszcze miasta
    matrix_length = len(matrix)
    unvisited_cities = set(range(1, matrix_length))

    # Pierwsze wywołanie funkcji rekurancyjnej (jako argumenty podajemy miasto startowe, wszystkie nie odwiedzone miasta macierz)
    result = algorithm_v2(0, unvisited_cities, matrix)

    # Odwracamy kolejność ścieżki
    result[1].reverse()

    return result


def test_brute_force_instances(city_number: int):
    instances = []

    i = 0
    while i <= 150:
        matrix = generate_graph(city_number)
        instances.append(matrix)
        i = i + 1

    total_time = 0
    start = 0
    end = 0
    i = 0
    for instance in instances:
        i = i + 1

        if i > 50:
            start = time.perf_counter_ns()

        brute_force_algorithm(instance)

        if i > 50:
            end = time.perf_counter_ns()

        total_time += (end - start)

    average_time = total_time / 100

    return average_time


def brute_force_automatic_test():
    i = 0
    while i < 7:
        i = i + 1
        average_time = test_brute_force_instances(i + 3)
        print("For [" + str(i + 3) + "] cities the average time is: " + str(average_time) + " ns" )


def test_held_karp_instances(city_number: int):
    instances = []

    i = 0
    while i <= 150:
        matrix = generate_graph(city_number)
        instances.append(matrix)
        i = i + 1

    total_time = 0
    start = 0
    end = 0
    i = 0
    for instance in instances:
        i = i + 1

        if i > 50:
            start = time.perf_counter_ns()

        held_karp_algorithm_v1(instance)

        if i > 50:
            end = time.perf_counter_ns()

        total_time += (end - start)

    average_time = total_time / 100

    return average_time


def held_karp_automatic_test():
    i = 0
    while i < 7:
        i = i + 1
        average_time = test_held_karp_instances(i + 3)
        print("For [" + str(i + 3) + "] cities the average time is: " + str(average_time) + " ns")


def main():
    main_menu_interface()


if __name__ == '__main__':
    main()
