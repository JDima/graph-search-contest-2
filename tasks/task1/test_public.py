import pytest

from .task import task1


class Case:
    def __init__(self, name: str, n: int, roads: list, optimal_value: int):
        self._name = name
        self.n = n
        self.roads = roads
        self.optimal_value = optimal_value

        self._roads_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for (a, b, c) in roads:
            self._roads_matrix[a][b] = c
            self._roads_matrix[b][a] = c

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=5,
        roads=[
            (0, 1, 1),
            (1, 4, 3),
            (4, 2, 2),
            (2, 3, 2),
            (3, 0, 1),
        ],
        optimal_value=9,
    ),
    Case(
        name='base2',
        n=7,
        roads=[
            (0, 6, 2),
            (6, 1, 1),
            (6, 5, 42),
            (1, 4, 3),
            (4, 2, 2),
            (2, 5, 5),
            (5, 3, 1),
        ],
        optimal_value=55,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    path = task1(
        n=case.n,
        roads=case.roads,
    )
    prev = None
    sum_value = 0
    for crossroads in path:
        if prev is None:
            prev = crossroads
            continue
        assert case._roads_matrix[prev, crossroads] > 0
        sum_value += case._roads_matrix[prev, crossroads]
        prev = crossroads
    assert sum_value == case.optimal_value
