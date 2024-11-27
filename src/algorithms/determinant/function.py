from src.internal.errors import AlgorithmValueError


def validate_matrix(matrix: list[list[int]]) -> None:
    # матрица является списком и длина не равна 0
    if not isinstance(matrix, list) or len(matrix) < 1:
        raise AlgorithmValueError("Ошибка ввода матрицы")
    row_first_len = len(matrix[0])
    count = 0 # будем проверять не прямоугольная ли матрица
    # проходим по строчке
    for row in matrix:
        # Исключение, если это не список, длина равна 0 или в строчках не одно и то же количество элементов
        if not isinstance(row, list) or len(row) < 1 or len(row) != row_first_len:
            raise AlgorithmValueError("Количество элементов в матрице неверно")
        
        count += 1
    if count != row_first_len:
        raise AlgorithmValueError("Была введена прямоугольная матрица") 


def get_minor(matrix, row, col):
    minor = []
    for i in range(len(matrix)):
        if i != row:
            new_row = []
            for j in range(len(matrix[i])):
                if j != col:
                    new_row.append(matrix[i][j])
            minor.append(new_row)
    return minor


def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """

    validate_matrix(matrix)  # проверка корректности введённой матрицы
    order = len(matrix)
    if order == 1:
        return matrix[0][0]
    
    det = 0
    for col in range(order):
        sign = (-1) ** col
        minor_matrix = get_minor(matrix, 0, col)
        det += sign * matrix[0][col] * calculate_determinant(minor_matrix)
    return det


def main(input_matrix: list[list[float]]) -> dict[str, list[list[float]]]:
    return {"determinant": calculate_determinant(input_matrix)}


if __name__ == "__main__":
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")
