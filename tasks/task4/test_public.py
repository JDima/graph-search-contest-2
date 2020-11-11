import pytest

from .task import task4


class Case:
    def __init__(self, name: str, n: int, connects: list,
                 critical_places: list):
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
        critical_places=set([5]),
    ),
    Case(
        name='base2',
        n=6,
        connects=[
            (2, [1, 3]),
            (5, [4, 6, 2]),
        ],
        critical_places=set([5, 2]),
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_tast4(case: Case) -> None:
    result = task4(
        n=case.n,
        connects=case.connects,
    )
    assert set(result) == case.critical_places
