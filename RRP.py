import numpy as np
import sympy as sp
from forward_kinematics_dh_class import ForwardKinematicsDH 

# Definición de símbolos
q1, q2 = sp.symbols('q1 q2')
d3 = sp.symbols('d3')
l1, l2 = sp.symbols('l1 l2')

# Conversión de 180 grados a radianes
alpha2_rad = sp.pi 

# Tabla de Parámetros Denavit-Hartenberg (DH)
dh_params_scara_sym = [
    [q1, 0, l1, 0],          
    [q2, 0, l2, alpha2_rad], # alpha2 = 180° = pi radianes
    [0, d3, 0, 0],           # Articulación Prismática (variando d, theta=0)
]

# Cálculo de la Cinemática Directa Simbólica
# H_sym_class es la matriz de transformación homogénea H_0_3
H_sym_class = ForwardKinematicsDH.symbolic(dh_params_scara_sym)

print("Robot SCARA (RRP) - Cinemática Directa Simbólica\n")
print("Matriz de Transformación Homogénea (H_0_3) del Efector Final:")
sp.pprint(H_sym_class, use_unicode=True)

# ----------------------------------------------------------------------
# Ejemplo Numérico
print("\n" + "="*50)
print("Ejemplo Numérico (q1=0°, q2=90°, d3=0.1, l1=0.5, l2=0.5)")

# Usamos el formato [theta_i, d_i, a_i, alpha_i]
dh_params_scara_num = [
    [0,       0, 0.5, 0],         # q1=0°, l1=0.5
    [np.pi/2, 0, 0.5, np.pi],     # q2=90°, l2=0.5, alpha2=180°
    [0,       0.1, 0, 0],         # d3=0.1 (variable de la junta prismática)
]

H_num_class = ForwardKinematicsDH.numeric(dh_params_scara_num)

print("\nMatriz de Transformación Homogénea Numérica:")
print(H_num_class)