import numpy as np
from scipy.spatial import distance_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def generate_contact_map(coords, threshold=8.0):
    """
    Generates a binary contact map based on a distance threshold.
    Standard threshold for CA-CA contacts is 8.0 Angstroms.
    """
    dist_matrix = distance_matrix(coords, coords)
    
    contact_map = (dist_matrix <= threshold).astype(int)
    
    return dist_matrix, contact_map

def plot_contact_map(matrix, title="Protein Contact Map"):
    """
    Visualizes the contact map or distance matrix using Seaborn.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(matrix, cmap="YlGnBu", square=True)
    plt.title(title)
    plt.xlabel("Residue Index")
    plt.ylabel("Residue Index")
    plt.show()