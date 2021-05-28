## Exercício 2

1 - Construa um programa para implementar e mostrar o histograma de uma
imagem qualquer. O algoritmo deve receber como parâmetro uma matriz que
armazena o conjunto de pixels da imagem. Não podem ser usados
métodos/funções prontos de bibliotecas para construir o vetor do histograma,
mas podem ser usados métodos prontos para exibir ("plotar") o gráfico
resultante.

```python
import cv2
import matplotlib.pyplot as plt

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

```

### Imagem
![picture](https://github.com/renatobanzai/sin5014_ex02/blob/master/bird.png?raw=true)

### Histograma
![picture](https://github.com/renatobanzai/sin5014_ex02/blob/master/bird_histograma.png?raw=true)

2 - Implemente um programa (método, procedimento, função) em qualquer
linguagem de programação que receba uma imagem e a exiba com todos os
pixels mais claros ou mais escuros. O nível de clareamento ou escurecimento,
assim como a matriz de pixels, devem ser recebidos como parâmetros. 

```python
import cv2
import matplotlib.pyplot as plt

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

    cv2.imshow("imagem", image_matrix)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
### Imagem Original
![picture](https://github.com/renatobanzai/sin5014_ex02/blob/master/bird.png?raw=true)

### Histograma Imagem Original
![picture](https://github.com/renatobanzai/sin5014_ex02/blob/master/bird_histograma.png?raw=true)

### Imagem aumentando o brilho em 50
![picture](https://github.com/renatobanzai/sin5014_ex02/blob/master/bird_bright_change_more_50.png?raw=true)

### Histograma da Imagem aumentando o brilho em 50
![picture](https://github.com/renatobanzai/sin5014_ex02/blob/master/bird_bright_change_more_50_histogram.png?raw=true)

### Imagem escurecendo em 50
![picture](https://github.com/renatobanzai/sin5014_ex02/blob/master/bird_bright_change_less_50.png?raw=true)

### Histograma da Imagem escurecendo em 50
![picture](https://github.com/renatobanzai/sin5014_ex02/blob/master/bird_bright_change_less_50_histogram.png?raw=true)

3 - Continuar a implementação do programa iniciado no exercício anterior, incluindo
um desses filtros (você escolhe):
- média
- mediana
- equalização (x)

```python
import cv2
import matplotlib.pyplot as plt
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
```
### Imagem Original
![picture](https://github.com/renatobanzai/sin5014_ex02/blob/master/bird.png?raw=true)

### Histograma da Imagem Original
![picture](https://github.com/renatobanzai/sin5014_ex02/blob/master/bird_histograma.png?raw=true)

### Imagem com Filtro de Equalização
![picture](https://github.com/renatobanzai/sin5014_ex02/blob/master/bird_equalization_filter.png?raw=true)

### Histograma da Imagem com Filtro de Equalização
![picture](https://github.com/renatobanzai/sin5014_ex02/blob/master/bird_equalization_histogram.png?raw=true)

