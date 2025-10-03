import numpy as np
import sympy as sp
from forward_kinematics_dh_class import ForwardKinematicsDH 

# Definición de símbolos
q1, q2, q3 = sp.symbols('q1 q2 q3')
l1, l2, l3 = sp.symbols('l1 l2 l3')

# Tabla de Parámetros Denavit-Hartenberg (DH)
dh_params_rrr_sym = [
    [q1, 0, l1, sp.pi/2], 
    [q2, 0, l2, 0],       
    [q3, 0, l3, 0],       
]

# Cálculo de la Cinemática Directa Simbólica
# H_sym_class será la matriz de transformación homogénea H_0_3
H_sym_class = ForwardKinematicsDH.symbolic(dh_params_rrr_sym)

print("Robot RRR (3 GDL) - Cinemática Directa Simbólica\n")
print("Matriz de Transformación Homogénea (H_0_3) del Efector Final:")
sp.pprint(H_sym_class, use_unicode=True)

# ----------------------------------------------------------------------
# Ejemplo Numérico
print("\n" + "="*50)
print("Ejemplo Numérico (q1=30°, q2=45°, q3=0°, l1=1, l2=1, l3=0.5)")

# Nota: La clase 'numeric' espera valores flotantes. 
# Usamos el formato [theta_i, d_i, a_i, alpha_i]
dh_params_rrr_num = [
    [np.pi/6, 0, 1, np.pi/2], # q1=30°, l1=1, alpha1=90°
    [np.pi/4, 0, 1, 0],       # q2=45°, l2=1, alpha2=0
    [0,       0, 0.5, 0],     # q3=0°, l3=0.5, alpha3=0
]

H_num_class = ForwardKinematicsDH.numeric(dh_params_rrr_num)

print("\nMatriz de Transformación Homogénea Numérica:")
print(H_num_class)