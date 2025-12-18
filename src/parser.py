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
        """Extracts (x, y, z) of Carbon-Alpha atoms."""
        self.fetch_structure(pdb_id)
        file_path = os.path.join(self.storage_dir, f"pdb{pdb_id.lower()}.ent")
        
        structure = self.parser.get_structure(pdb_id, file_path)
        coords = []
        for model in structure:
            for chain in model:
                for residue in chain:
                    if 'CA' in residue: # Focus on the backbone
                        coords.append(residue['CA'].get_coord())
        return np.array(coords)