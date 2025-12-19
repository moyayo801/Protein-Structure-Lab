from Bio.PDB import PDBList, PDBParser
import numpy as np
import os

class PDBProcessor:
    def __init__(self, storage_dir='data'):
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)
        self.pdbl = PDBList()
        self.parser = PDBParser(QUIET=True)

    def fetch_structure(self, pdb_id):
        """Downloads a PDB file."""
        return self.pdbl.retrieve_pdb_file(pdb_id.lower(), pdir=self.storage_dir, file_format='pdb')

    def get_ca_coordinates(self, pdb_id):
        """
        Extracts the (x, y, z) coordinates of Carbon-Alpha (CA) atoms.
        Uses a flattened search to ensure atoms are found even in complex hierarchies.
        """
        self.fetch_structure(pdb_id)
        file_path = os.path.join(self.storage_dir, f"pdb{pdb_id.lower()}.ent")
        
        structure = self.parser.get_structure(pdb_id, file_path)
        coords = []
        
        # Flattened search: look at every atom in the entire file
        for atom in structure.get_atoms():
            # Check for the Carbon-Alpha name
            # We use .strip() because PDB files sometimes have " CA " or "CA"
            if atom.get_name().strip() == 'CA':
                coords.append(atom.get_coord())
        
        coords_array = np.array(coords)
        
        if coords_array.size == 0:
            print(f"Error: Still no CA atoms found for {pdb_id}.")
        else:
            print(f"Success: Extracted {len(coords_array)} CA atoms.")
            
        return coords_array