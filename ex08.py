import cv2
import matplotlib.pyplot as plt
import sys

class Image:

    image_matrix = None
    _image_location = ""

    def __init__(self, image_location):
        # lendo a imagem em escala de cinza
        self.image_matrix = cv2.imread(image_location, 0)
        self._image_location = image_location
        # todo: load image into an opencv object

    '''
    Exercício 1
    Construa um programa para implementar e mostrar o histograma de uma
    imagem qualquer. O algoritmo deve receber como parâmetro uma matriz que
    armazena o conjunto de pixels da imagem. Não podem ser usados
    métodos/funções prontos de bibliotecas para construir o vetor do histograma,
    mas podem ser usados métodos prontos para exibir ("plotar") o gráfico
    resultante.
    '''
    def show_histogram(self, image_matrix):
        lines = len(image_matrix)
        columns = len(image_matrix[0])
        max_contrast_resolution = 256
        # creates a vector with a position for each gray level
        histogram_values = [0 for x in range(max_contrast_resolution)]

        # Run each pixel of the image matrix
        for line in range(lines):
            for column in range(columns):
                pixel_value = image_matrix[line, column]
                histogram_values[pixel_value] += 1

        plt.ylabel("Quantidade de Pixels")
        plt.xlabel("Níveis de Cinza")

        # Plots the histogram
        plt.bar(x=list(range(max_contrast_resolution)),
                height=histogram_values,
                width=1)
        # shows the plot
        plt.show()

    '''
    Exercício 2
    Implemente um programa (método, procedimento, função) em qualquer
    linguagem de programação que receba uma imagem e a exiba com todos os
    pixels mais claros ou mais escuros. O nível de clareamento ou escurecimento,
    assim como a matriz de pixels, devem ser recebidos como parâmetros. 
    '''
    def change_bright(self, image_matrix, change_value):
        lines = len(image_matrix)
        columns = len(image_matrix[0])
        # Run each pixel of the image matrix
        for line in range(lines):
            for column in range(columns):
                # avoid to go less than the min of scale (0)
                if image_matrix[line, column] + change_value < 0:
                    image_matrix[line, column] = 0
                else:
                    # avoid to go upper to max of scale (255)
                    if image_matrix[line, column] + change_value > 255:
                        image_matrix[line, column] = 255
                    else:
                        image_matrix[line, column] += change_value
        self.show_histogram(image_matrix)
        cv2.imshow("imagem", image_matrix)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    '''
    Exercício 3
    Continuar a implementação do programa iniciado no exercício anterior, incluindo
    um desses filtros (você escolhe):
        • média
        • mediana
        • equalização (x)
    '''
    def equalization_filter(self, image_matrix):
        lines = len(image_matrix)
        columns = len(image_matrix[0])
        max_contrast_resolution = 256
        # creates a vector with a position for each frequency of gray level
        frequency_gray_levels = [0 for x in range(max_contrast_resolution)]
        # Run each pixel of the image matrix to get each frequency
        for line in range(lines):
            for column in range(columns):
                pixel_gray_level = image_matrix[line, column]
                frequency_gray_levels[pixel_gray_level] += 1

        cumulative_value = 0
        # creates a vector with a position for each cumulative frequency of a gray level
        cumulative_frequency_gray_levels = [0 for x in range(max_contrast_resolution)]
        gray_level = 0
        # run each frequency to determine the cumulative frequency
        for gray_level in range(max_contrast_resolution):
            cumulative_value += frequency_gray_levels[gray_level]
            cumulative_frequency_gray_levels[gray_level] = cumulative_value

        # in class slide, the I
        ideal_pixels_number = lines * columns / max_contrast_resolution

        # create a dictionary for each gray level with the equalization value
        equalization_values = {}

        for gray_level in range(max_contrast_resolution):
            cumulative_frequency = cumulative_frequency_gray_levels[gray_level]
            equalization_value = max(0, (round((cumulative_frequency/ideal_pixels_number))-1))
            equalization_values[gray_level] = equalization_value

        # apply the equalization to each images pixel
        for line in range(lines):
            for column in range(columns):
                image_matrix[line, column] = equalization_values[image_matrix[line, column]]

        self.show_histogram(image_matrix)
        cv2.imshow("imagem", image_matrix)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def horizontal_mask(self, image_matrix):
        result = 0
        lines = len(image_matrix)
        columns = len(image_matrix[0])
        line_end = lines - 3
        column_end = columns -3
        # Run each pixel of the image matrix
        for line in range(0, line_end, 3):
            for column in range(0, column_end, 3):
                result += image_matrix[line][column] * -1
                result += image_matrix[line][column + 1] * -1
                result += image_matrix[line][column + 2] * -1
                result += image_matrix[line + 1][column] * 2
                result += image_matrix[line + 1][column + 1] * 2
                result += image_matrix[line + 1][column + 2] * 2
                result += image_matrix[line + 2][column] * -1
                result += image_matrix[line + 2][column + 1] * -1
                result += image_matrix[line + 2][column + 2] * -1
        #print(self._image_location, "horizontal mask", result)
        return abs(result)

    def vertical_mask(self, image_matrix):
        result = 0
        lines = len(image_matrix)
        columns = len(image_matrix[0])
        line_end = lines - 3
        column_end = columns -3
        # Run each pixel of the image matrix
        for line in range(0,line_end,3):
            for column in range(0,column_end,3):
                result += image_matrix[line][column] * -1
                result += image_matrix[line][column + 1] * 2
                result += image_matrix[line][column + 2] * -1
                result += image_matrix[line + 1][column] * -1
                result += image_matrix[line + 1][column + 1] * 2
                result += image_matrix[line + 1][column + 2] * -1
                result += image_matrix[line + 2][column] * -1
                result += image_matrix[line + 2][column + 1] * 2
                result += image_matrix[line + 2][column + 2] * -1
        #print(self._image_location, "vertical mask", result)
        return abs(result)

    def diagonal_mask(self, image_matrix):
        result = 0
        lines = len(image_matrix)
        columns = len(image_matrix[0])
        line_end = lines - 3
        column_end = columns -3
        # Run each pixel of the image matrix
        for line in range(0,line_end,3):
            for column in range(0,column_end,3):
                result += image_matrix[line][column] * 2
                result += image_matrix[line][column + 1] * -1
                result += image_matrix[line][column + 2] * -1
                result += image_matrix[line + 1][column] * -1
                result += image_matrix[line + 1][column + 1] * 2
                result += image_matrix[line + 1][column + 2] * -1
                result += image_matrix[line + 2][column] * -1
                result += image_matrix[line + 2][column + 1] * -1
                result += image_matrix[line + 2][column + 2] * 2
        #print(self._image_location, "diagonal mask", result)
        return abs(result)

    def print_line_type(self, image_matrix):
        abs_horizontal_mask = self.horizontal_mask(image_matrix)
        abs_vertical_mask = self.vertical_mask(image_matrix)
        abs_diagonal_mask = self.diagonal_mask(image_matrix)

        if abs_horizontal_mask > abs_vertical_mask:
            if abs_diagonal_mask > abs_horizontal_mask:
                print(self._image_location, "diagonal")
            else:
                print(self._image_location, "horizontal")
        else:
            if abs_diagonal_mask > abs_vertical_mask:
                print(self._image_location, "diagonal")
            else:
                print(self._image_location, "vertical")

    def find_object(self, seed, image_matrix, object_list):
        background_color = 255
        line_ini = seed[0] - 1
        line_end = line_ini + 3

        col_ini = seed[1] - 1
        col_end = col_ini + 3
        object_list[seed] = True
        for line in range(line_ini, line_end):
            for column in range(col_ini, col_end):
                if column != seed[1] or line != seed[0]:
                    if (line, column) not in object_list.keys():
                        if image_matrix[line][column] < background_color:
                            self.find_object((line, column), image_matrix, object_list)

        return object_list

    def get_object_qty(self, image_matrix, background_color):
        has_object = True
        qty = 0
        while has_object == True:
            has_object = False
            obj = {}
            for line in range(len(image_matrix)):
                for column in range(len(image_matrix[0])):
                    if image_matrix[line][column] < background_color:
                        has_object = True
                        obj1 = self.find_object((line, column), image_matrix, obj)
                        qty += 1
                        for i in obj1.keys():
                            image_matrix[i[0]][i[1]] = background_color
        print(qty, "objetos")






if __name__ == '__main__':
    sys.setrecursionlimit(3000)
    img = Image("4objetos.bmp")
    #img = Image("horizontal.bmp")
    img.get_object_qty(img.image_matrix, 255)
    # img = Image("horizontal.bmp")
    # img.print_line_type(img.image_matrix)
    #
    # img = Image("inclinada.bmp")
    # img.print_line_type(img.image_matrix)
    #
    # img = Image("vertical.bmp")
    # img.print_line_type(img.image_matrix)

