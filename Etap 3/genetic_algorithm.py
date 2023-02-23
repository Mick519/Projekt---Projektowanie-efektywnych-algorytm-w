import time
import random


class genetic_algorithm:

    # Algorytm wyznaczający metodą zachłanną startową ścieżkę
    @staticmethod
    def start_path(matrix):

        # Miasto startowe.
        previous_city = 0

        # Miasta, których nie odwiedziliśmy.
        remaining_cities = set(range(len(matrix)))

        # Aktualna ścieżka.
        path = []

        # Licznik
        counter = 0

        # Dopóki nie odwiedzimy wszystkich miast, wykonujemy następujące akcje.
        while len(remaining_cities) > 0:

            # Inkrementacja licznika.
            counter = counter + 1

            # Najlepsze miasto.
            best_city = []

            # Koszt podróży z poprzedniego do najlepszego miasta
            best_city_cost = float('inf')

            # Jeżeli licznik miast jest mniejszy od 4 miast to.
            if counter < 4:
                best_city = random.randint(0, len(matrix) - 1)

                while best_city not in remaining_cities:
                    best_city = random.randint(0, len(matrix) - 1)
            else:
                # Dla każdego miasta wśród pozostałych miast wykonujemy następujące akcje.
                for next_city in remaining_cities:

                    # Jeżeli koszt podróży do następnego miasta jest mniejszy od aktualnie najlepszego kosztu
                    if matrix[previous_city][next_city] < best_city_cost:
                        best_city_cost = matrix[previous_city][next_city]
                        best_city = next_city

            # Do ścieżki wstawiamy miasto, do którego koszt podróż jest najmniejszy
            path.append(best_city)

            # Jako poprzednie miasto ustawiamy najlepsze miasto.
            previous_city = best_city

            # Od listy pozostałych do rozpatrzenia miast odejmujemy najlepsze miasto
            remaining_cities = remaining_cities - {best_city}

        # Zwracamy ścieżkę.
        return path

    # Funkcja obliczająca koszt ścieżki.
    @staticmethod
    def get_path_cost(matrix, path):

        # Miejsce, w którym będziemy przechowywać koszt ścieżki.
        path_cost = 0

        # Dla każdego miasta wykonujemy następujące operacje.
        for current_city in range(len(path) - 1):
            # Dodanie do kosztu ścieżki odległości pomiędzy aktualnym miastem i następnym miastem.
            path_cost += matrix[path[current_city]][path[current_city + 1]]

        # Dodanie do kosztu ścieżki odległości pomiędzy ostatni miastem a pierwszym miastem (powrót na początek).
        path_cost += matrix[path[-1]][path[0]]

        # Zwrócenie kosztu ścieżki.
        return path_cost

    # Funkcja generująca populację ścieżek.
    def generate_population(self, matrix, population_size):

        # Miejsce, w którym będziemy przechowywać populację.
        population = []

        # Generujemy tyle ścieżek, ile wynosi rozmiar populacji.
        for _ in range(population_size):

            # Generujemy ścieżkę, pierwsze 3 miasta losowe, potem algorytmem zachłannym.
            path = self.start_path(matrix)

            # Dodanie ścieżki do populacji.
            population.append(path)

        # Zwrócenie populacji
        return population

    # Funkcja krzyżowania dwóch ścieżek z jednym punktem podziału.
    @staticmethod
    def one_point_crossover(first_path, second_path):

        # Wylosowanie punktu podziału.
        crossover_city = random.randint(1, len(first_path) - 1)

        # Skopiowanie do nowej ścieżki części pierwszej ścieżki (od jej początku, aż do punktu podziału).
        new_route = first_path[:crossover_city]

        # Dla każdego miasta z drugiej ścieżki wykonujemy następująca operację.
        for current_city in second_path:

            # Jeżeli aktualne miasto nie znajduje się w nowej ścieżce, to dodajemy je na jej koniec.
            if current_city not in new_route:
                new_route.append(current_city)

        # Zwrócenie nowej ścieżki.
        return new_route

    # Funkcja mutacji typu swap (zamieniamy 2 miasta ze sobą).
    @staticmethod
    def swap_mutation(path):

        # Losowanie dwóch miast z listy.
        first_city = random.randint(0, len(path) - 1)
        second_city = random.randint(0, len(path) - 1)

        # Zamiana miast miejscami.
        path[first_city], path[second_city] = path[second_city], path[first_city]

        # Zwrócenie nowej ścieżki.
        return path

    # Algorytm genetyczny.
    def genetic_algorithm(self, matrix, maximal_time, start_population_size, crossing_propagation, mutation_propagation):

        # Generowanie populacji początkowej.
        population = self.generate_population(matrix, start_population_size)

        # Wyznaczenie kryterium zakończenia algorytmu
        start_time = time.perf_counter_ns()
        end_time = start_time + int(maximal_time) * pow(10, 9)

        # Dopóki nie minie wyznaczony czas, wykonujemy następujące operacje.
        while time.perf_counter_ns() < end_time:

            # Posortowanie populacji wg. kosztu podróży dla danej ścieżki.
            population = sorted(population, key=lambda x: self.get_path_cost(matrix, x))

            # Metoda selekcji. Z populacji, którą aktualnie mamy zachowujemy połowę najlepszych ścieżek.
            population = population[:start_population_size // 2]

            # Wykonujemy operacje tyle razy, ile wynosi rozmiar początkowej populacji podzielony przez 2 z podłogą.
            for _ in range(start_population_size // 2):

                # Wybranie pierwszego i drugiego losowego rodzica z populacji
                first_parent = random.choice(population)
                second_parent = random.choice(population)
                child = first_parent

                # Wykonanie krzyżowania dwóch rodziców.
                crossing_random_number = random.randint(0, 100)

                if crossing_random_number < crossing_propagation:
                    child = self.one_point_crossover(first_parent, second_parent)

                # Wykonanie mutacji potomka.
                mutation_random_number = random.randint(0, 100)

                if mutation_random_number < mutation_propagation:
                    child = self.swap_mutation(child)

                # Dodanie potomka do populacji
                population.append(child)

        # Wybranie najlepszej ścieżki, czyli pierwszej ścieżki, z populacji.
        best_path = population[0]
        # Obliczenie kosztu dla tej ścieżki.
        best_path_cost = self.get_path_cost(matrix, best_path)

        # Dodajemy na koniec ścieżki miasto startowe.
        best_path += (best_path[0],)

        # Zwrócenie kosztu, ścieżki oraz czasu wykonania algorytmu.
        return best_path_cost, best_path
