![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
# PROYECTO CINEMÁTICA DIRECTA EN REPOSITORIO DE GIT
## Introdicción
La cinemática directa es esencial en robótica porque permite calcular la posición y orientación del efector final a partir de las variables articulares. En este proyecto se implementa la cinemática directa simbólica de tres configuraciones de robots: un planar RR (2 GDL), un antropomórfico RRR (3 GDL) y un SCARA (RRP), utilizando la metodología de Denavit-Hartenberg (DH).

El desarrollo se realizó en Python, empleando las librerías NumPy y Sympy para el manejo de cálculos numéricos y simbólicos. Se generaron matrices de transformación homogénea que describen el movimiento del robot, siguiendo los parámetros DH del libro Control de robots manipuladores de Fernando Reyes Cortés.


## Metodología
La metodología para este proyecto se dividió en dos niveles: la implementación de funciones base para la cinemática directa y la aplicación de estas funciones a tres configuraciones de robots manipuladores (RR, RRR y RRP/SCARA).

### Preparación del entorno y librerías
•	El proyecto se desarrolló en Python, utilizando las librerías:
   -NumPy: para cálculos numéricos.
   -Sympy: para cálculos simbólicos.
•	Se organizaron los programas en módulos separados:
	- forward_kinematics_dh.py: implementa el cálculo numérico de matrices DH.
	- forward_kinematics_dh_symbolic.py: implementa el cálculo simbólico de matrices DH.
o	forward_kinematics_dh_class.py: integra ambas funcionalidades en una clase reutilizable.


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
