import numpy as np
import sympy as sp
from forward_kinematics_dh_class import ForwardKinematicsDH 

# Definición de símbolos
q1, q2 = sp.symbols('q1 q2')
l1, l2 = sp.symbols('l1 l2')

# Tabla de Parámetros Denavit-Hartenberg (DH)
dh_params_planar_sym = [
    [q1, 0, l1, 0], 
    [q2, 0, l2, 0],
]

# Cálculo de la Cinemática Directa Simbólica
H_sym_class = ForwardKinematicsDH.symbolic(dh_params_planar_sym)

print("Robot Planar RR (2 GDL) - Cinemática Directa Simbólica\n")
print("Matriz de Transformación Homogénea (H_0_2) del Efector Final:")
sp.pprint(H_sym_class, use_unicode=True)

#-------------------------------------------------------------------
# Ejemplo Numérico 
print("\n" + "="*50)
print("Ejemplo Numérico (q1=45°, q2=-45°, l1=1, l2=1)")

# Usamos valores numéricos: q1=pi/4, q2=-pi/4, l1=1, l2=1
dh_params_planar_num = [
    [np.pi/4,  0, 1, 0],
    [-np.pi/4, 0, 1, 0], 
]

H_num_class = ForwardKinematicsDH.numeric(dh_params_planar_num)

print("\nMatriz de Transformación Homogénea Numérica:")
print(H_num_class)