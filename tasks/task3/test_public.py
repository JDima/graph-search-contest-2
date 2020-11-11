import pytest

from .task import task3


class Case:
    def __init__(self, name: str, n: int, edges: list, probs: list):
        self._name = name
        self.n = n
        self.edges = edges
        self.probs = probs

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=6,
        edges=[
            (1, 2),
            (2, 3),
            (3, 1),
            (4, 5),
            (5, 6),
            (6, 4),
            (1, 4),
        ],
        probs=(0, 1),
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_tast3(case: Case) -> None:
    prob_a, prob_b = task3(
        n=case.n,
        edges=case.edges,
    )
    assert round(prob_a, 5) == round(case.probs[0], 5)
    assert round(prob_b, 5) == round(case.probs[1], 5)
