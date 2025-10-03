![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
# PROYECTO CINEMÁTICA DIRECTA EN REPOSITORIO DE GIT

This project provides tools to compute the forward kinematics of serial robotic manipulators using Denavit-Hartenberg (DH) parameters. It supports both numerical and symbolic calculations, making it useful for both simulation and analytical studies.

## Features
- Compute forward kinematics numerically using NumPy
- Compute forward kinematics symbolically using SymPy
- Unified class interface for both calculation types
- Example scripts for quick testing

## File Structure
- `forward_kinematics_dh.py`: Numeric DH forward kinematics functions (NumPy)
- `forward_kinematics_dh_symbolic.py`: Symbolic DH forward kinematics functions (SymPy)
- `forward_kinematics_dh_class.py`: Unified class with both numeric and symbolic methods
- `example.py`: Example usage of numeric and symbolic functions (separate functions)
- `example2.py`: Example usage of the unified class for both numeric and symbolic calculations

## How to Use
1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd dh_forward_kinematics_python
   ```
2. **Install dependencies**
   This project requires `numpy` and `sympy`. Install them with:
   ```sh
   pip install numpy sympy
   ```
3. **Run examples**
   - For basic function usage:
     ```sh
     python example.py
     ```
   - For class-based usage:
     ```sh
     python example2.py
     ```

## How It Works
- **Numeric calculation:**
  - Provide a list of DH parameters (theta, d, a, alpha) for each joint as numbers.
  - The code computes the transformation matrix using NumPy.
- **Symbolic calculation:**
  - Provide DH parameters as SymPy symbols or expressions.
  - The code computes the transformation matrix symbolically, allowing for analytical manipulation.
- **Unified class:**
  - The `ForwardKinematicsDH` class provides both `numeric()` and `symbolic()` static methods for easy switching between calculation types.

## Example
```
from forward_kinematics_dh_class import ForwardKinematicsDH
import numpy as np
import sympy as sp

# Numeric
dh_params = [[np.pi/4, 0, 1, 0], [np.pi/4, 0, 1, 0]]
H = ForwardKinematicsDH.numeric(dh_params)
print(H)

# Symbolic
th1, th2 = sp.symbols('th1 th2')
a1, a2 = sp.symbols('a1 a2')
dh_params_sym = [[th1, 0, a1, 0], [th2, 0, a2, 0]]
H_sym = ForwardKinematicsDH.symbolic(dh_params_sym)
sp.pprint(H_sym)
```

## License
MIT
