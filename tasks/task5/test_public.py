import pytest

from .task import task5


class Case:
    def __init__(self, name: str, n: int, edges: list, count: int):
        self._name = name
        self.n = n
        self.edges = edges
        self.count = count

    def __str__(self) -> str:
        return 'task5_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=3,
        edges=[
            (1, 2),
            (2, 3),
            (1, 3),
        ],
        count=0,
    ),
    Case(
        name='base2',
        n=6,
        edges=[
            (1, 3),
            (6, 1),
            (6, 3),
            (4, 1),
            (6, 4),
            (5, 2),
            (3, 2),
            (3, 5),
        ],
        count=1,
    ),
    Case(
        name='base3',
        n=9,
        edges=[
            (1, 2),
            (1, 3),
            (1, 9),
            (3, 4),
            (4, 7),
            (3, 5),
            (5, 6),
            (6, 8),
            (2, 8)
        ],
        count=3,
    ),
    Case(
        name='base4',
        n=12,
        edges=[
            (1, 2),
            (1, 9),
            (9, 10),
            (2, 6),
            (6, 8),
            (8, 11),
            (2, 4),
            (4, 3),
            (4, 5),
            (5, 7),
            (7, 12),
            (12, 3)
        ],
        count=6,
    ),
    Case(
        name='base5',
        n=8,
        edges=[
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (3, 7),
            (3, 8)
        ],
        count=4,
    ),
    Case(
        name='base6',
        n=2,
        edges=[
            (1, 2),
        ],
        count=0,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task5(case: Case) -> None:
    count = task5(
        n=case.n,
        edges=case.edges,
    )
    assert count == case.count
