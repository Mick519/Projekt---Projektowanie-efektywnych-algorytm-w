import time
import random


class tabu_search_algorithm:

    @staticmethod
    # Algorytm wyznaczający metodą zachłanną startową ścieżkę
    def start_path(matrix):

        # Miasto startowe.
        previous_city = random.randint(0, len(matrix) - 1)

        # Miasta, których nie odwiedziliśmy.
        remaining_cities = set(range(len(matrix)))

        # Aktualna ścieżka.
        path = []

        # Dopóki nie odwiedzimy wszystkich miast, wykonujemy następujące akcje.
        while len(remaining_cities) > 0:

            # Najlepsze miasto.
            best_city = []

            # Koszt podróży z poprzedniego do najlepszego miasta
            best_city_cost = float('inf')

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

    @staticmethod
    # Funkcja obliczająca koszt podróży dla danej ścieżki
    def travel_cost(matrix, path):

        # Miejsce, w którym będziemy przechowywać całkowity koszt podróży.
        cost = 0

        # Obliczamy koszt ścieżki.
        for actual_city in set(path):
            cost += matrix[path[actual_city]][path[(actual_city + 1) % len(path)]]

        # Zwracamy koszt.
        return cost

    @staticmethod
    # Funkcja generująca sąsiadów dla podanej ścieżki.
    def generate_neighbours(path_length):

        # Miejsce, w którym będziemy przechowywać listę sąsiadów.
        neighbour_list = []

        for i in range(0, path_length):
            # Generujemy losowe wierzchołki
            x = random.randint(0, path_length - 1)
            y = random.randint(0, path_length - 1)
            while x == y:
                y = random.randint(0, path_length - 1)

            # Stworzenie nowego sąsiada.
            neighbour = (x, y)

            # Dodajemy sąsiada do listy sąsiadów, jeżeli się na niej nie znajduje.
            if neighbour not in neighbour_list:
                neighbour_list.append(neighbour)

        # Zwracamy listę sąsiadów
        return neighbour_list

    # Funkcja zamieniająca miejscami wybrane miasta
    @staticmethod
    def swap_neighbours(neighbour, path):
        # Wyciągnięcie informacji na temat tego, które wierzchołki mamy.
        first_city = int(neighbour[0])
        second_city = int(neighbour[1])

        # Pobranie aktualnej ścieżki i dokonanie w niej zmiany na podstawie informacji sąsiada.
        neighbour_path = path.copy()
        neighbour_path[first_city], neighbour_path[second_city] = neighbour_path[second_city], neighbour_path[first_city]

        return neighbour_path

    # Funkcja wstawiająca wybrane miasto w daną pozycję
    @staticmethod
    def insert_neighbours(neighbour, path):
        # Wyciągnięcie informacji na temat tego, które wierzchołki mamy.
        city_position = int(neighbour[0])
        new_position = int(neighbour[1])

        # Pobranie aktualnej ścieżki i dokonanie w niej zmiany na podstawie informacji sąsiada.
        neighbour_path = path.copy()

        # Zapisujemy numer miasta, który przenosimy.
        city = neighbour_path[city_position]

        # Usuwamy to miasto z listy.
        neighbour_path.pop(city_position)

        # Wstawiamy miasto na nową pozycję.
        neighbour_path.insert(new_position, city)

        return neighbour_path

    # Funkcja odwracająca zadany fragment ścieżki
    @staticmethod
    def invert_neighbours(neighbour, path):
        # Wyciągnięcie informacji na temat tego, które wierzchołki mamy.
        start_position = int(neighbour[0])
        end_position = int(neighbour[1])

        # Zamiana miejsce, jeżeli startowa pozycja jest mniejsza od końcowej
        if start_position > end_position:
            start_position, end_position = end_position, start_position

        # Pobranie aktualnej ścieżki i dokonanie w niej zmiany na podstawie informacji sąsiada.
        neighbour_path = path.copy()
        if start_position == 0:
            neighbour_path = list(reversed(neighbour_path[start_position:end_position])) + neighbour_path[end_position:]
        elif end_position == (len(path) - 1):
            neighbour_path = neighbour_path[0:start_position] + neighbour_path[end_position:(start_position - 1):-1]
        elif start_position == 0 and end_position == (len(path) - 1):
            neighbour_path = neighbour_path[end_position:(start_position - 1):-1]
        else:
            neighbour_path = neighbour_path[0:start_position] + neighbour_path[end_position:(start_position - 1):-1] + neighbour_path[(end_position + 1):]
        return neighbour_path

    # Algorytm tabu search.
    def tabu_search_algorithm(self, matrix, maximal_time, neighbour_type):

        # Maksymalna długość tabu list (i tym samym kadencji zakazanego rozwiązania).
        cadence_length = round(len(matrix) / 4)

        # Licznik iteracji bez poprawy wyniku.
        iteration_without_improvement_counter = 0

        # Po ilu iteracjach bez poprawy należy wygenerować nowe rozwiązanie
        max_iteration_without_improvement = len(matrix) * 3

        # Pierwsze wyznaczenie aktualnej ścieżki
        actual_path = self.start_path(matrix)

        # Pierwsze wyznaczenie kosztu aktualnej ścieżki
        actual_cost = self.travel_cost(matrix, actual_path)

        # Wyznaczenie najlepszej ścieżki
        best_path = actual_path

        # Wyznaczenie najlepszego kosztu
        best_path_cost = actual_cost

        # Lista zakazanych ruchów
        tabu_list = []

        # Aktualnie nie mamy najlepszej sąsiedniej ścieżki.
        best_neighbour_path = None

        # Koszt podróży dla najlepszej sąsiedniej ścieżki.
        best_neighbour_path_cost = float('inf')

        # Długość ścieżki
        path_length = len(actual_path)

        # Czas w [ms], po jakim znaleziono najlepsze rozwiązanie
        best_path_time = None

        # Wyznaczenie kryterium zakończenia algorytmu
        start_time = time.perf_counter_ns()
        end_time = start_time + int(maximal_time) * pow(10, 9)

        # Dopóki nie minie wyznaczony czas, wykonujemy następujące operacje.
        while time.perf_counter_ns() < end_time:

            # Generujemy sąsiadów
            neighbour_list = self.generate_neighbours(path_length)

            # Zerujemy najlepszego sąsiada.
            best_neighbour = None

            # Dla każdego sąsiada w liście sąsiadów wykonujemy następujące operacje
            for neighbour in neighbour_list:

                # Wygenerowanie sąsiedniej ścieżki.
                if neighbour_type == "1":
                    neighbour_path = self.swap_neighbours(neighbour, actual_path)
                elif neighbour_type == "2":
                    neighbour_path = self.insert_neighbours(neighbour, actual_path)
                elif neighbour_type == "3":
                    neighbour_path = self.invert_neighbours(neighbour, actual_path)
                else:
                    neighbour_path = self.swap_neighbours(neighbour, actual_path)

                # Obliczamy koszt podróży sąsiednią ścieżką.
                neighbour_path_cost = self.travel_cost(matrix, neighbour_path)

                # Jeżeli sąsiednia ścieżka nie jest na tabu list lub jeżeli sąsiednia ścieżka jest bardzo
                # korzystna (kryterium aspiracji).
                if neighbour not in tabu_list or neighbour_path_cost < best_path_cost:

                    # Usuwamy sąsiada z listy, jeżeli się na niej znajduje.
                    if neighbour in tabu_list:
                        tabu_list.remove(neighbour)

                    # Zapisujemy ścieżkę oraz koszt, jeżeli są one najlepsze spośród reszty sąsiadów.
                    if neighbour_path_cost < best_neighbour_path_cost:
                        best_neighbour = neighbour
                        best_neighbour_path = neighbour_path.copy()
                        best_neighbour_path_cost = neighbour_path_cost

            # Jeżeli koszt najlepszego sąsiada jest mniejszy od najlepszego kosztu, to uznajemy tego sąsiada za najlepszego.
            if best_neighbour_path_cost < best_path_cost:
                best_path = best_neighbour_path.copy()
                best_path_cost = best_neighbour_path_cost
                best_path_time = (time.perf_counter_ns() - start_time) / pow(10, 6)
            else:
                iteration_without_improvement_counter = iteration_without_improvement_counter + 1

            # Jeżeli ilość iteracji bez polepszenia rozwiązania wynosi zadaną wartość, to generujemy nowe startowe rozwiązanie
            # (strategia dywersyfikacji).
            if iteration_without_improvement_counter == max_iteration_without_improvement:
                actual_path = self.start_path(matrix)
                iteration_without_improvement_counter = 0
            else:
                actual_path = best_neighbour_path.copy()

            # Dodanie ścieżki na zabronioną listę
            tabu_list.append(best_neighbour)

            # Jeżeli długość tabu listy jest większa od długości kadencji, to usuwamy z listy najstarszego sąsiada.
            if len(tabu_list) > cadence_length:
                tabu_list.pop(0)

        # Dodajemy na koniec ścieżki miasto startowe.
        best_path += (best_path[0],)

        # Zwracamy najniższy koszt oraz najlepszą ścieżkę.
        return best_path_cost, best_path, best_path_time
