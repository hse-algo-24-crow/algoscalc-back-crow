from src.internal.errors import AlgorithmValueError


def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """

    pass


def main(input_matrix: list[list[float]]) -> dict[str, list[list[float]]]:
    return {"determinant": calculate_determinant(input_matrix)}


if __name__ == "__main__":
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")
