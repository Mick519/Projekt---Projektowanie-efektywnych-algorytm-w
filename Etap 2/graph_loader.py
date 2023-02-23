import re


class graph_loader:

    @staticmethod
    def load_graph(file_name):

        file_type = file_name[0: 3]

        if file_type == "tsp":
            # Wczytanie linii z pliku
            graph = open(file_name).readlines()

            # Usuwanie pustych przestrzeni
            graph_stripped = []
            for line in graph[1:]:
                single_line = re.sub(' +', ' ', line.strip())
                graph_stripped.append(single_line)

            # Usuwanie pustych linii oraz wstawienie wartości do macierzy
            matrix = []
            for line in graph_stripped:
                if line.strip() != '':
                    value_list = line.split(' ')

                    matrix_row = []
                    for value in value_list:
                        matrix_row.append(int(value))

                    matrix.append(matrix_row)

            return matrix

        elif file_type == "ftv":

            # Wczytanie linii z pliku
            graph = open(file_name).readlines()

            # Usuwanie pustych przestrzeni
            graph_stripped = []
            for line in graph[7:]:
                single_line = re.sub(' +', ' ', line.strip())
                graph_stripped.append(single_line)

            # Usuwanie pustych linii oraz wstawienie wartości do macierzy

            city_number = int(file_name[3: len(file_name) - 5]) + 1
            matrix = []
            matrix_row = []
            counter = city_number
            for line in graph_stripped:
                if line.strip() != 'EOF':
                    value_list = line.split(' ')

                    if line.strip() != '':
                        for value in value_list:
                            matrix_row.append(int(value))
                            counter = counter - 1

                            if counter == 0:
                                matrix.append(matrix_row)
                                matrix_row = []
                                counter = city_number

            return matrix

        elif file_type == "rbg":

            # Wczytanie linii z pliku
            graph = open(file_name).readlines()

            # Usuwanie pustych przestrzeni
            graph_stripped = []
            for line in graph[7:]:
                single_line = re.sub(' +', ' ', line.strip())
                graph_stripped.append(single_line)

            # Usuwanie pustych linii oraz wstawienie wartości do macierzy
            matrix = []
            matrix_row = []
            is_it_last_line = False
            for line in graph_stripped:
                if line.strip() != 'EOF':

                    is_it_last_line = True

                    value_list = line.split(' ')

                    if line.strip() != '':
                        for value in value_list:
                            matrix_row.append(int(value))

                    if len(value_list) != 17:
                        matrix.append(matrix_row)
                        matrix_row = []
                        is_it_last_line = False
                else:
                    if is_it_last_line:
                        matrix.append(matrix_row)
                        matrix_row = []

            return matrix