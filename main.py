import cv2
import matplotlib.pyplot as plt

class Image:

    image_matrix = None

    def __init__(self, image_location):
        # lendo a imagem em escala de cinza
        self.image_matrix = cv2.imread(image_location, 0)
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
                if image_matrix[line, column] + change_value < 0:
                    image_matrix[line, column] = 0
                else:
                    if image_matrix[line, column] + change_value > 255:
                        image_matrix[line, column] = 255
                    else:
                        image_matrix[line, column] += change_value

        cv2.imshow("imagem", image_matrix)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




if __name__ == '__main__':
    img = Image("bird.png")
    # Running Exercise 1
    img.show_histogram(img.image_matrix)

    # Running Exercise 2
    img.change_bright(img.image_matrix, -50)




