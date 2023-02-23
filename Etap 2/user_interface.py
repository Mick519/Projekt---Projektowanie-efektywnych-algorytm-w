from graph_loader import graph_loader
from tabu_search_algorithm import tabu_search_algorithm
from automatic_test import automatic_test


class user_interface:

    @staticmethod
    def show_interface():
        matrix = None
        maximal_time = None
        neighbour_type = None
        loader = graph_loader()
        tabu_search = tabu_search_algorithm()
        print("Tabu search algorithm")
        n = 1
        while n == 1:
            print("(0) Exit program")
            print("(1) Load graph from file")
            print("(2) Set parameters for algorithm")
            print("(3) Perform tabu search algorithm")
            print("(4) Perform automatic test")
            print("Please select option: ")
            choice = input()
            if choice == "0":
                break
            elif choice == "1":
                print("Loading graph from file")
                print("Please provide file name: ")
                file_name = input()
                matrix = loader.load_graph(file_name)
            elif choice == "2":
                print("Setting parameters for algorithm")
                print("Please provide time to stop [s]: ")
                maximal_time = input()
                print("Please select neighbour type: [1] swap (default), [2] insert, [3] invert")
                neighbour_type = input()
                matrix = loader.load_graph(file_name)
            elif choice == "3":
                print("Performing algorithm")
                if matrix is not None and maximal_time is not None and neighbour_type is not None:
                    best_path_cost, best_path, best_path_time = tabu_search.tabu_search_algorithm(matrix, maximal_time, neighbour_type)
                    print("Result")
                    print("Best cost: ")
                    print(best_path_cost)
                    print("Best path: ")
                    print(best_path)
                    print("Best path found after [ms]: ")
                    print(best_path_time)
                else:
                    print("The graph was not loaded yet.")
            elif choice == "4":
                print("Performing automatic test")
                test = automatic_test()
                test.automatic_test()
            else:
                print("Incorrect value, please try again!")
