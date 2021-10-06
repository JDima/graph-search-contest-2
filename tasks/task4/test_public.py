import pytest

from .task import task4


class Case:
    def __init__(self, name: str, n: int, connects: list,
                 critical_places: set):
        self._name = name
        self.n = n
        self.connects = connects
        self.critical_places = critical_places

    def __str__(self) -> str:
        return 'task4_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=5,
        connects=[
            (5, [1, 2, 3, 4]),
        ],
        critical_places={5},
    ),
    Case(
        name='base2',
        n=6,
        connects=[
            (2, [1, 3]),
            (5, [4, 6, 2]),
        ],
        critical_places={5, 2},
    ),
    Case(
        name='base3',
        n=6,
        connects=[
            (1, [2, 3]),
            (4, [3, 6]),
            (5, [3, 6])
        ],
        critical_places={1, 3},
    ),
    Case(
        name='base4',
        n=4,
        connects=[
            (2, [1, 3]),
            (3, [4])
        ],
        critical_places={2, 3},
    ),
    Case(
        name='base5',
        n=9,
        connects=[
            (1, [2, 3, 9]),
            (8, [6, 2]),
            (5, [3, 6]),
            (4, [3, 7])
        ],
        critical_places={1, 4, 3},
    ),
    Case(
        name='base6',
        n=3,
        connects=[
            (1, [2, 3]),
            (2, [3])
        ],
        critical_places=set(),
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task4(case: Case) -> None:
    result = task4(
        n=case.n,
        connects=case.connects,
    )
    assert set(result) == case.critical_places
