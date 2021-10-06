import pytest

from .task import task3


class Case:
    def __init__(self, name: str, n: int, edges: list, probs: tuple):
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
    Case(
        name='base2',
        n=10,
        edges=[
            (6, 4),
            (6, 1),
            (2, 6),
            (1, 2),
            (1, 4),
            (4, 8),
            (5, 8),
            (8, 3),
            (5, 3),
            (7, 5),
            (7, 9),
            (9, 10),
            (10, 7)
        ],
        probs=(0.5, 0.5),
    ),
    Case(
        name='base3',
        n=14,
        edges=[
            (6, 4),
            (6, 1),
            (2, 6),
            (1, 2),
            (1, 4),
            (4, 8),
            (5, 8),
            (8, 3),
            (5, 3),
            (7, 5),
            (7, 9),
            (9, 10),
            (10, 7),
            (3, 12),
            (11, 12),
            (11, 13),
            (11, 14),
            (12, 13),
            (12, 14),
            (13, 14)
        ],
        probs=(0.666666, 0.333333),
    ),
    Case(
        name='base4',
        n=16,
        edges=[
            (6, 4),
            (6, 1),
            (2, 6),
            (1, 2),
            (1, 4),
            (4, 8),
            (5, 8),
            (8, 3),
            (5, 3),
            (7, 5),
            (7, 9),
            (9, 10),
            (10, 7),
            (3, 12),
            (11, 12),
            (11, 13),
            (11, 14),
            (12, 13),
            (12, 14),
            (13, 14),
            (6, 15),
            (6, 16)
        ],
        probs=(0.4, 0.6),
    ),
    Case(
        name='base5',
        n=5,
        edges=[
            (2, 1),
            (2, 3),
            (2, 4),
            (2, 5)
        ],
        probs=(0, 1),
    ),
    Case(
        name='base6',
        n=4,
        edges=[
            (2, 1),
            (1, 3),
            (1, 4),
            (2, 3),
            (2, 4),
            (3, 4)
        ],
        probs=(0, 0),
    ),
    Case(
        name='base7',
        n=1,
        edges=[
        ],
        probs=(0, 0),
    ),
    Case(
        name='base8',
        n=2,
        edges=[
            (2, 1),
        ],
        probs=(0, 1),
    ),
    Case(
        name='base9',
        n=6,
        edges=[
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6)
        ],
        probs=(0.4, 0.6),
    ),
    Case(
        name='base10',
        n=14,
        edges=[
            (6, 4),
            (6, 1),
            (2, 6),
            (1, 2),
            (1, 4),
            (4, 8),
            (5, 8),
            (8, 3),
            (5, 3),
            (7, 5),
            (7, 9),
            (9, 10),
            (10, 7),
            (3, 12),
            (11, 12),
            (12, 13),
            (13, 14),
            (14, 11),
            (3, 13)
        ],
        probs=(0.5, 0.5),
    ),
    Case(
        name='base11',
        n=14,
        edges=[
            (6, 4),
            (6, 1),
            (2, 6),
            (1, 2),
            (1, 4),
            (4, 8),
            (5, 8),
            (8, 3),
            (5, 3),
            (7, 5),
            (7, 9),
            (9, 10),
            (10, 7),
            (3, 12),
            (11, 12),
            (12, 13),
            (13, 14),
            (14, 11),
            (4, 13)
        ],
        probs=(0, 1),
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task3(case: Case) -> None:
    prob_a, prob_b = task3(
        n=case.n,
        edges=case.edges,
    )
    assert round(prob_a, 5) == round(case.probs[0], 5)
    assert round(prob_b, 5) == round(case.probs[1], 5)
