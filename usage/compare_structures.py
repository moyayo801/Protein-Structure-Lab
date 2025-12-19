import sys
import os
import numpy as np

# Path handling
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parser import PDBProcessor
from src.geometry import kabsch_algorithm, calculate_rmsd

def main():
    processor = PDBProcessor()
    
    coords_original = processor.get_ca_coordinates("1UBQ")
    
    theta = np.radians(45)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,              0,             1]
    ])
    coords_moved = np.dot(coords_original, rotation_matrix) + np.array([10, 20, 30])
    
    initial_rmsd = calculate_rmsd(coords_original, coords_moved)
    
    coords_aligned, coords_target_centered = kabsch_algorithm(coords_moved, coords_original)
    
    final_rmsd = calculate_rmsd(coords_aligned, coords_target_centered)
    
    print("--- Structural Comparison Results ---")
    print(f"Initial RMSD (Before Alignment): {initial_rmsd:.4f}")
    print(f"Final RMSD (After Kabsch Alignment): {final_rmsd:.4f}")
    
    if final_rmsd < 0.001:
        print("\n Success: The structures were perfectly superimposed!")
    else:
        print("\n Warning: Alignment failed to reach near-zero RMSD.")

if __name__ == "__main__":
    main()