import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parser import PDBProcessor
from src.analysis import generate_contact_map, plot_contact_map

def main():
    processor = PDBProcessor()
    pdb_id = "1UBQ" 
    
    print(f"--- Generating Analysis for {pdb_id} ---")
    coords = processor.get_ca_coordinates(pdb_id)
    
    if len(coords) > 0:
        dist_matrix, contact_map = generate_contact_map(coords, threshold=8.0)
        
        plot_contact_map(dist_matrix, title=f"Distance Matrix for {pdb_id}")
        
        plot_contact_map(contact_map, title=f"Contact Map for {pdb_id} (Threshold: 8Å)")
    else:
        print("Failed to extract coordinates.")

if __name__ == "__main__":
    main()