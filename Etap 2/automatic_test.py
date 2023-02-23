from graph_loader import graph_loader
from tabu_search_algorithm import tabu_search_algorithm


class automatic_test:

    @staticmethod
    def automatic_test():
        loader = graph_loader()
        tabu_search = tabu_search_algorithm()

        print("********************************************************")
        print("Testing ftv47.atsp: 2 min, swap_neighbours")
        matrix = loader.load_graph("ftv47.atsp")
        maximal_time = 120
        neighbour_type = 1
        counter = 0

        while counter < 10:
            counter = counter + 1
            best_path_cost, best_path, best_path_time = tabu_search.tabu_search_algorithm(matrix, maximal_time, neighbour_type)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print("Timer [ms]: " + str(best_path_time))
            print(" ")

        print("********************************************************")
        print("Testing ftv170.atsp: 4 min, swap_neighbours")
        matrix = loader.load_graph("ftv170.atsp")
        maximal_time = 240
        neighbour_type = 1
        counter = 0

        while counter < 10:
            counter = counter + 1
            best_path_cost, best_path, best_path_time = tabu_search.tabu_search_algorithm(matrix, maximal_time, neighbour_type)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print("Timer [ms]: " + str(best_path_time))
            print(" ")

        print("********************************************************")
        print("Testing rbg403.atsp: 6 min, swap_neighbours")
        matrix = loader.load_graph("rbg403.atsp")
        maximal_time = 360
        neighbour_type = 1
        counter = 0

        while counter < 10:
            counter = counter + 1
            best_path_cost, best_path, best_path_time = tabu_search.tabu_search_algorithm(matrix, maximal_time, neighbour_type)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print("Timer [ms]: " + str(best_path_time))
            print(" ")

        print("********************************************************")
        print("Testing ftv47.atsp: 2 min, insert_neighbours")
        matrix = loader.load_graph("ftv47.atsp")
        maximal_time = 120
        neighbour_type = 2
        counter = 0

        while counter < 10:
            counter = counter + 1
            best_path_cost, best_path, best_path_time = tabu_search.tabu_search_algorithm(matrix, maximal_time, neighbour_type)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print("Timer [ms]: " + str(best_path_time))
            print(" ")

        print("********************************************************")
        print("Testing ftv170.atsp: 4 min, insert_neighbours")
        matrix = loader.load_graph("ftv170.atsp")
        maximal_time = 240
        neighbour_type = 2
        counter = 0

        while counter < 10:
            counter = counter + 1
            best_path_cost, best_path, best_path_time = tabu_search.tabu_search_algorithm(matrix, maximal_time, neighbour_type)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print("Timer [ms]: " + str(best_path_time))
            print(" ")

        print("********************************************************")
        print("Testing rbg403.atsp: 6 min, insert_neighbours")
        matrix = loader.load_graph("rbg403.atsp")
        maximal_time = 360
        neighbour_type = 2
        counter = 0

        while counter < 10:
            counter = counter + 1
            best_path_cost, best_path, best_path_time = tabu_search.tabu_search_algorithm(matrix, maximal_time, neighbour_type)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print("Timer [ms]: " + str(best_path_time))
            print(" ")

        print("********************************************************")
        print("Testing ftv47.atsp: 2 min, invert_neighbours")
        matrix = loader.load_graph("ftv47.atsp")
        maximal_time = 120
        neighbour_type = 3
        counter = 0

        while counter < 10:
            counter = counter + 1
            best_path_cost, best_path, best_path_time = tabu_search.tabu_search_algorithm(matrix, maximal_time, neighbour_type)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print("Timer [ms]: " + str(best_path_time))
            print(" ")

        print("********************************************************")
        print("Testing ftv170.atsp: 4 min, invert_neighbours")
        matrix = loader.load_graph("ftv170.atsp")
        maximal_time = 240
        neighbour_type = 3
        counter = 0

        while counter < 10:
            counter = counter + 1
            best_path_cost, best_path, best_path_time = tabu_search.tabu_search_algorithm(matrix, maximal_time, neighbour_type)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print("Timer [ms]: " + str(best_path_time))
            print(" ")

        print("********************************************************")
        print("Testing rbg403.atsp: 6 min, invert_neighbours")
        matrix = loader.load_graph("rbg403.atsp")
        maximal_time = 360
        neighbour_type = 3
        counter = 0

        while counter < 10:
            counter = counter + 1
            best_path_cost, best_path, best_path_time = tabu_search.tabu_search_algorithm(matrix, maximal_time, neighbour_type)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print("Timer [ms]: " + str(best_path_time))
            print(" ")

        return 0
