import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# Input
degree = ctrl.Antecedent(np.arange(0, 401, 1), 'degree')

degree['NLS'] = fuzz.trimf(degree.universe, [90,130,170])
degree['NBS'] = fuzz.trimf(degree.universe, [30,150,170])
degree['SALN'] = fuzz.trimf(degree.universe, [170,175,180])
degree['Z'] = fuzz.trimf(degree.universe, [180,180,180])
degree['SALP'] = fuzz.trimf(degree.universe, [180,185,190])
degree['PBS'] = fuzz.trimf(degree.universe, [190,210,330])
degree['PLS'] = fuzz.trimf(degree.universe, [190,230,270])


angular_velocity = ctrl.Antecedent(np.arange(-10, 11, 0.1), 'angularVelocity')

angular_velocity['NEG'] = fuzz.trapmf(angular_velocity.universe, [-15,-10,-1,0])
angular_velocity['ZS'] = fuzz.trapmf(angular_velocity.universe, [-0.1, -0.05, 0.05, 0.1])
angular_velocity['POS'] = fuzz.trapmf(angular_velocity.universe, [0,1,20,30])

# Output
applied_force = ctrl.Consequent(np.arange(-2, 2, 0.1), 'appliedForce'p)

degree.view()
angular_velocity.view()
applied_force.view()
plt.show()