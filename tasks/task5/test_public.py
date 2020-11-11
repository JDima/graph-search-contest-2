import pytest

from .task import task5


class Case:
    def __init__(self, name: str, n: int, edges: list, count: list):
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
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_tast5(case: Case) -> None:
    count = task5(
        n=case.n,
        edges=case.edges,
    )
    assert count == case.count
