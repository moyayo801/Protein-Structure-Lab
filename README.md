# 🔬 Protein-Structure-Lab: 3D Geometry & Structural Analysis

A specialized toolkit for the quantitative analysis of protein structures. This repository implements structural superposition, similarity metrics, and residue interaction mapping—core components of computational structural biology and drug design.

## 🚀 Features

* **PDB Infrastructure:** Automated fetching of structures from the Protein Data Bank (PDB) and extraction of $C\alpha$ backbone coordinates.
* **Kabsch Algorithm:** Optimal structural alignment through Singular Value Decomposition (SVD).
* **RMSD Quantification:** Calculation of Root-Mean-Square Deviation to measure structural divergence.
* **Residue Contact Maps:** 2D interaction fingerprints utilizing Euclidean distance matrices.

---

## 📐 Mathematical Foundations

### Structural Superposition (Kabsch Algorithm)
To compare two structures $P$ and $Q$, we must find the optimal rotation matrix $R$ that minimizes the distance between them.

1. **Centroid Translation:**
   Moving both structures to the origin:
   $$P_{centered} = P - \mu_P, \quad Q_{centered} = Q - \mu_Q$$

2. **Covariance Matrix:**
   $$H = P_{centered}^T Q_{centered}$$

3. **Singular Value Decomposition (SVD):**
   We decompose $H$ into $U \Sigma V^T$ to find the optimal rotation $R$:
   
   $$R = V \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \det(VU^T) \end{pmatrix} U^T$$

### Similarity Metric (RMSD)
The Root-Mean-Square Deviation (RMSD) is the standard measure of structural divergence:

$$RMSD = \sqrt{\frac{1}{N} \sum_{i=1}^{N} ||P_i - Q_i||^2}$$

---

## 📂 Project Structure

* `src/`: Core logic for parsing, geometry math, and interaction analysis.
* `usage/`: Demonstration scripts including structural verification and visualization.
* `data/`: Local cache for PDB files (ignored by git).

## 📊 Visualization
The toolkit generates **Contact Maps**, which are binary representations of the 3D structure. Two residues $i$ and $j$ are considered "in contact" if:
$$Distance(i, j) \leq 8.0 \, \text{Å}$$

---

## 🛠️ Installation & Usage

1. **Setup Environment:**
```bash
python -m venv .venv
source .venv/bin/activate 
pip install -r requirements.txt
```
2. **Run Analysis:**
```bash
# Compare two structures
python usage/compare_structures.py

# Visualize Contact Maps
python usage/visualize_structure.py
```