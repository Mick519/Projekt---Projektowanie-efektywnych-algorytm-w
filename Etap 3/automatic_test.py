from graph_loader import graph_loader
from genetic_algorithm import genetic_algorithm


class automatic_test:

    @staticmethod
    def automatic_test():
        print("Performing automatic tests.")
        mutation_propagation = 1
        crossing_propagation = 85
        loader = graph_loader()
        algorithm = genetic_algorithm()

        matrix = loader.load_graph("ftv47.atsp")

        print("********************************************************")
        print("Testing ftv47.atsp: 30 sek, 100 start population")
        maximal_time = 30
        start_population_size = 100
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size, crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv47.atsp: 60 sek, 100 start population")

        maximal_time = 60
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size, crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv47.atsp: 120 sek, 100 start population")

        maximal_time = 120
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size, crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv47.atsp: 240 sek, 100 start population")

        maximal_time = 240
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size, crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv47.atsp: 30 sek, 1000 start population")

        maximal_time = 30
        start_population_size = 1000
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size, crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv47.atsp: 60 sek, 1000 start population")

        maximal_time = 60
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size, crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv47.atsp: 120 sek, 1000 start population")

        maximal_time = 120
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size, crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv47.atsp: 240 sek, 1000 start population")

        maximal_time = 240
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size, crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv47.atsp: 30 sek, 10000 start population")

        maximal_time = 30
        start_population_size = 10000
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size, crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv47.atsp: 60 sek, 10000 start population")

        maximal_time = 60
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv47.atsp: 120 sek, 10000 start population")

        maximal_time = 120
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv47.atsp: 240 sek, 10000 start population")

        maximal_time = 240
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        matrix = loader.load_graph("ftv170.atsp")

        print("********************************************************")
        print("Testing ftv170.atsp: 30 sek, 100 start population")
        maximal_time = 30
        start_population_size = 100
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv170.atsp: 60 sek, 100 start population")

        maximal_time = 60
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv170.atsp: 120 sek, 100 start population")

        maximal_time = 120
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv170.atsp: 240 sek, 100 start population")

        maximal_time = 240
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv170.atsp: 30 sek, 1000 start population")

        maximal_time = 30
        start_population_size = 1000
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv170.atsp: 60 sek, 1000 start population")

        maximal_time = 60
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv170.atsp: 120 sek, 1000 start population")

        maximal_time = 120
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv170.atsp: 240 sek, 1000 start population")

        maximal_time = 240
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv170.atsp: 30 sek, 10000 start population")

        maximal_time = 30
        start_population_size = 10000
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv170.atsp: 60 sek, 10000 start population")

        maximal_time = 60
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv170.atsp: 120 sek, 10000 start population")

        maximal_time = 120
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing ftv170.atsp: 240 sek, 10000 start population")

        maximal_time = 240
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        matrix = loader.load_graph("rbg403.atsp")

        print("********************************************************")
        print("Testing rbg403.atsp: 30 sek, 100 start population")
        maximal_time = 30
        start_population_size = 100
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing rbg403.atsp: 60 sek, 100 start population")

        maximal_time = 60
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing rbg403.atsp: 120 sek, 100 start population")

        maximal_time = 120
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing rbg403.atsp: 240 sek, 100 start population")

        maximal_time = 240
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing rbg403.atsp: 30 sek, 1000 start population")

        maximal_time = 30
        start_population_size = 1000
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing rbg403.atsp: 60 sek, 1000 start population")

        maximal_time = 60
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing rbg403.atsp: 120 sek, 1000 start population")

        maximal_time = 120
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing rbg403.atsp: 240 sek, 1000 start population")

        maximal_time = 240
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing rbg403.atsp: 30 sek, 10000 start population")

        maximal_time = 30
        start_population_size = 10000
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing rbg403.atsp: 60 sek, 10000 start population")

        maximal_time = 60
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing rbg403.atsp: 120 sek, 10000 start population")

        maximal_time = 120
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")

        print("********************************************************")
        print("Testing rbg403.atsp: 240 sek, 10000 start population")

        maximal_time = 240
        counter = 0

        while counter < 5:
            counter = counter + 1
            best_path_cost, best_path = algorithm.genetic_algorithm(matrix, maximal_time, start_population_size,
                                                                    crossing_propagation, mutation_propagation)
            print("Solution: " + str(counter))
            print("Cost: " + str(best_path_cost))
            print("Path: " + str(best_path))
            print(" ")
