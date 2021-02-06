from typing import Optional

import pytest

from .task import task2


class Case:
    def __init__(self, name: str, roads: list, optimal_path: Optional[list]):
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
    Case(
        name='base3',
        roads=[
            (1, 2, 1),
            (1, 5, 4),
            (2, 4, 3),
            (4, 5, 6),
            (1, 3, 2),
            (3, 1, 5),
            (3, 1, 7),
            (1, 3, 8)
        ],
        optimal_path=[1, 2, 5, 7, 8, 4, 6, 3]
    ),
    Case(
        name='base4',
        roads=[
            (4, 5, 10),
            (5, 1, 9),
            (1, 6, 11),
            (6, 4, 12),
            (4, 3, 2),
            (3, 2, 7),
            (2, 7, 4),
            (7, 4, 8),
            (4, 8, 6),
            (8, 9, 3),
            (9, 10, 5),
            (10, 4, 1)
        ],
        optimal_path=[1, 2, 7, 4, 8, 10, 9, 11, 12, 6, 3, 5]
    ),
    Case(
        name='base5',
        roads=[
            (1, 2, 3),
            (1, 2, 5),
            (2, 3, 4),
            (2, 3, 6),
            (2, 3, 8),
            (2, 3, 7),
            (1, 3, 2),
            (1, 3, 1)
        ],
        optimal_path=[1, 2, 3, 4, 6, 7, 8, 5]
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    path = task2(roads=case.roads)
    assert path == case.optimal_path
