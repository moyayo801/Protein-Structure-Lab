import numpy as np

def kabsch_algorithm(P, Q):
    """
    Finds the optimal rotation matrix to align P to Q.
    P: (N, 3) matrix
    Q: (N, 3) matrix
    """
    centroid_P = np.mean(P, axis=0)
    centroid_Q = np.mean(Q, axis=0)
    P_centered = P - centroid_P
    Q_centered = Q - centroid_Q

    H = np.dot(P_centered.T, Q_centered)

    U, S, Vt = np.linalg.svd(H)

    d = np.linalg.det(np.dot(Vt.T, U.T))
    step_matrix = np.eye(3)
    if d < 0:
        step_matrix[2, 2] = -1

    R = np.dot(Vt.T, np.dot(step_matrix, U.T))

    P_aligned = np.dot(P_centered, R)

    return P_aligned, Q_centered

def calculate_rmsd(P, Q):
    """Calculates Root-Mean-Square Deviation."""
    return np.sqrt(np.mean(np.sum((P - Q)**2, axis=1)))