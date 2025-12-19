import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parser import PDBProcessor

def main():
    processor = PDBProcessor()
    
    pdb_id = "1UBQ"
    print(f"--- Processing Protein: {pdb_id} ---")
    
    try:
        coords = processor.get_ca_coordinates(pdb_id)
        print(f"Successfully extracted backbone.")
        print(f"Number of Amino Acids (CA atoms): {len(coords)}")
        print(f"First 3 atom coordinates (x, y, z):\n{coords[:3]}")
        print(f"Shape of coordinate array: {coords.shape}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()