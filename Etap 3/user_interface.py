from graph_loader import graph_loader
from genetic_algorithm import genetic_algorithm
from automatic_test import automatic_test


class user_interface:

    @staticmethod
    def show_interface():
        matrix = None
        maximal_time = None
        start_population_size = None
        mutation_propagation = None
        crossing_propagation = None
        loader = graph_loader()
        algorithm = genetic_algorithm()
        print("Genetic algorithm")
        n = 1
        while n == 1:
            print("(0) Exit program")
            print("(1) Load graph from file")
            print("(2) Set parameters for algorithm")
            print("(3) Perform genetic algorithm")
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
                print("Please start population size: ")
                start_population_size = input()
                print("Please provide mutation factor: ")
                mutation_propagation = input()
                print("Please provide crossing factor: ")
                crossing_propagation = input()
            elif choice == "3":
                print("Performing algorithm")
                if matrix is not None and maximal_time is not None and start_population_size is not None and mutation_propagation is not None and crossing_propagation is not None:
                    best_route_cost, best_route = algorithm.genetic_algorithm(matrix, int(maximal_time), int(start_population_size), int(crossing_propagation), int(mutation_propagation))
                    print("Result")
                    print("Best cost: ")
                    print(best_route_cost)
                    print("Best path: ")
                    print(best_route)
                else:
                    print("The graph was not loaded yet.")
            elif choice == "4":
                print("Performing automatic test")
                test = automatic_test()
                test.automatic_test()
            else:
                print("Incorrect value, please try again!")
