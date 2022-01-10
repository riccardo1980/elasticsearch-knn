import numpy as np


def cosine_similarity(x1: np.ndarray, x2: np.ndarray) -> np.ndarray:
    """
     cosine-similarity implementation (naive-version)

    :param x1:
    :param x2:
    :return: cosine similarity
    """
    return np.dot(x1, x2) / (np.linalg.norm(x1) * np.linalg.norm(x2))
