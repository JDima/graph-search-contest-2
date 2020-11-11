import pytest

from .task import task2


class Case:
    def __init__(self, name: str, roads: list, optimal_path: list):
        self._name = name
        self.roads = roads
        self.optimal_path = optimal_path

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        roads=[
            (1, 2, 1),
            (2, 3, 2),
            (3, 1, 6),
            (1, 2, 5),
            (2, 3, 3),
            (3, 1, 4),
        ],
        optimal_path=[1, 2, 3, 5, 4, 6],
    ),
    Case(
        name='base2',
        roads=[
            (1, 2, 1),
            (2, 3, 2),
            (1, 3, 3),
            (2, 4, 4),
        ],
        optimal_path=None,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    path = task2(roads=case.roads)
    assert path == case.optimal_path
