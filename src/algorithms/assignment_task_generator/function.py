import random
import copy
from typing import Any
# import sys
from src.internal.errors import AlgorithmTypeError, AlgorithmValueError
from src.internal.errors.exceptions import AlgorithmRuntimeError

# sys.path.append("C:\\Users\\sofav\\algoscalc-back-crow")
# print(sys.path)
COSTS = "costs"

ORDER_TYPE_ERR_MSG = "Порядок матрицы не является целым числом"
MIN_COST_TYPE_ERR_MSG = "Минимальная стоимость назначения не является целым числом"
MAX_COST_TYPE_ERR_MSG = "Максимальная стоимость назначения не является целым числом"
MIN_COST_ERR_MSG = "Минимальная стоимость назначения должна быть больше нуля"
MAX_COST_ERR_MSG = "Максимальная стоимость назначения должна быть больше нуля"
ORDER_ERR_MSG = "Количество задач должно быть больше нуля"
MIN_MAX_COST_ERR_MSG = "Минимальная длительность этапа должна быть меньше максимальной"


def __validate_params(order: int, min_cost: int, max_cost: int) -> None:
    if not isinstance(order, int):
        raise AlgorithmTypeError(ORDER_TYPE_ERR_MSG)
    if order <= 0:
        raise AlgorithmValueError(ORDER_ERR_MSG)
    if not isinstance(min_cost, int):
        raise AlgorithmTypeError(MIN_COST_TYPE_ERR_MSG)
    if min_cost <= 0:
        raise AlgorithmValueError(MIN_COST_ERR_MSG)
    if not isinstance(max_cost, int):
        raise AlgorithmTypeError(MAX_COST_TYPE_ERR_MSG)
    if max_cost <= 0:
        raise AlgorithmValueError(MAX_COST_ERR_MSG)
    if min_cost > max_cost:
        raise AlgorithmValueError(MIN_MAX_COST_ERR_MSG)


def generate_matrix(order: int, min_cost: int, max_cost: int):
    """
    Генератор условий задачи о назначениях
    :param order: Порядок матрицы затрат.
    :param min_cost: Минимальная стоимость назначения.
    :param max_cost: Максимальная стоимость назначения.
    :return: Квадратная матрица затрат заданного порядка.
    """
    __validate_params(order, min_cost, max_cost)

    # создаем матрицу заданного порядка
    matrix = [[0 for _ in range(order)] for _ in range(order)]

    # заполняем матрицу рандомно сгенерированными значениями
    for i in range(order):
        for j in range(order):
            matrix[i][j] = random.randint(min_cost, max_cost)

    # создаем копию матрицы
    # до тех пор пока в матрице присутствует совершенное парасочетание перезаполняем ее
    while  has_perfect_matching(order, matrix):
        for i in range(order):
            for j in range(order):
                matrix[i][j] = random.randint(min_cost, max_cost)
    return matrix


def  has_perfect_matching(order: int, matrix: list[list[int]]) -> bool:
    """
    Проверка матрицы на наличие в ней совершенного парасочетания
    :param order: Порядок матрицы затрат,
    :param matrix: Матрица затрат.
    :return: булевое значение, где True - парасочетание найдено, False - не найдено
    """

    clone = copy.copy(matrix)
    # редукция матрицы по строкам
    for idx in range(order):
        clone[idx] = [int(x-min(clone[idx])) for x in clone[idx]]

    # редукция матрицы по столбцам
    minimum = float('inf')
    i = 0
    while i != order:
        for j in range(order):
            minimum = min(clone[j][i], minimum)
        for j in range(order):
            clone[j][i] -= minimum
        i += 1
        minimum = float('inf')

    graph = [[] for _ in range(order)]

    # для каждой из работ сохраняем возможных работников
    for i in range(order):
        for j in range(order):
            if clone[i][j] == 0:
                graph[i].append(j)

    # итоговое назначение работников на работы
    result = [-1] * order

    max_matches = 0 # счетчик ребер в максимальном парасочетании
    for u in range(order):
        seen = [False] * order
        if bpm(u, seen, graph, result):
            max_matches += 1

    return max_matches == order # если число ребер в максимальном парасочетании равно количеству работ => совершенное парасочетание найдено

def bpm(u, seen, graph, result):
    """
    Проверяет возможность назначения работников на работы. Поиск в глубину.
    :param u: работа,
    :param graph: связи между работниками и работами,
    :param result: итоговое распределение работников на работы,
    :param seen: просмотренные работники.
    :return: булевое значение
    """

    # Перебираем всех работников, которые могут быть назначены работе
    for v in graph[u]:
        if not seen[v]:  # Если работник еще не был проверен
            seen[v] = True # Помечаем работника как проверенного
            # Если работник не назначен ни на одну работу или
            # если мы можем переназначить текущую работу работника
            if result[v] == -1 or bpm(result[v], seen, graph, result):
                result[v] = u # Назначаем работника на работу
                return True
    return False

    
def main(order: int, min_cost: int, max_cost: int) -> dict[str, Any]:
    return {COSTS: generate_matrix(order, min_cost, max_cost)}

if __name__ == "__main__":
    print(main(10, 0, 0))
