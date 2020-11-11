import pytest

from .task import task6


class Case:
    def __init__(self, name: str, n: int, edges: list, prob: list):
        self._name = name
        self.n = n
        self.edges = edges
        self.prob = prob

    def __str__(self) -> str:
        return 'task6_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=4,
        edges=[
            (1, 2),
            (1, 3),
            (2, 4),
            (4, 1),
        ],
        prob=0.5,
    ),
    Case(
        name='base2',
        n=7,
        edges=[
            (1, 2),
            (2, 3),
            (2, 4),
            (3, 4),
            (3, 5),
            (5, 6),
            (6, 7),
            (5, 7),
        ],
        prob=0.71429,
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_tast5(case: Case) -> None:
    prob = task6(
        n=case.n,
        edges=case.edges,
    )
    assert round(prob, 5) == round(case.prob, 5)
