# Gini Impurity

from collections import Counter
from typing import Iterable, Sequence

def gini_from_probs(probs: Iterable[float]) -> float:
    """
    Gini impurity given class probabilities.
    """
    ps = list(probs)
    return 1.0 - sum(p * p for p in ps)

def gini_from_counts(counts: Iterable[int]) -> float:
    """
    Gini impurity given class counts (e.g., [n_class0, n_class1, ...]).
    """
    counts = list(counts)
    n = sum(counts)
    if n == 0:
        return 0.0
    return 1.0 - sum((c / n) ** 2 for c in counts)

def gini_from_labels(labels: Iterable) -> float:
    """
    Gini impurity from a list/iterable of class labels.
    """
    c = Counter(labels)
    return gini_from_counts(c.values())

def weighted_gini_split(left_labels: Sequence, right_labels: Sequence) -> float:
    """
    Weighted Gini for a binary split (left/right partitions).
    """
    n_left, n_right = len(left_labels), len(right_labels)
    n_total = n_left + n_right
    if n_total == 0:
        return 0.0
    g_left = gini_from_labels(left_labels)
    g_right = gini_from_labels(right_labels)
    return (n_left / n_total) * g_left + (n_right / n_total) * g_right


# single node
print(gini_from_labels([0, 0, 1, 1, 1]))     # -> 0.48

# using counts
print(gini_from_counts([2, 3]))               # -> 0.48

# using probabilities
print(gini_from_probs([0.4, 0.6]))            # -> 0.48

# split score
left  = [0, 0, 0]
right = [1, 1]
print(weighted_gini_split(left, right))       # -> 0.0 (pure split)
