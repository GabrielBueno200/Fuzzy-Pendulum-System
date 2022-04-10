import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
from sympy import apart_list

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
applied_force = ctrl.Consequent(np.arange(-2, 2, 0.1), 'appliedForce')

applied_force['NB'] = fuzz.gaussmf(applied_force.universe, -1.5,1)
applied_force['Z'] = fuzz.gaussmf(applied_force.universe, -1,2)
applied_force['N'] = fuzz.gaussmf(applied_force.universe, -0.5,1)
applied_force['P'] = fuzz.gaussmf(applied_force.universe, 0.5,1)
applied_force['PB'] = fuzz.gaussmf(applied_force.universe, 1.5,1)

degree.view()
angular_velocity.view()
applied_force.view()

# Rules

regra_1 = ctrl.Rule(degree['NLS'] & angular_velocity['POS'], applied_force['NB'])
regra_2 = ctrl.Rule(degree['NBS'] & angular_velocity['POS'], applied_force['Z'])
regra_3 = ctrl.Rule(degree['SALN'] & angular_velocity['POS'], applied_force['N'])
regra_4 = ctrl.Rule(degree['Z'] & angular_velocity['ZS'], applied_force['P'])
regra_5 = ctrl.Rule(degree['SALP'] & angular_velocity['NEG'], applied_force['P'])
regra_6 = ctrl.Rule(degree['PBS'] & angular_velocity['NEG'], applied_force['Z'])
regra_7 = ctrl.Rule(degree['PLS'] & angular_velocity['NEG'], applied_force['PB'])

controler = ctrl.ControlSystem([regra_1, regra_2, regra_3, regra_4, regra_5, regra_6, regra_7])

# Simultaion
CalcAppliedForce = ctrl.ControlSystemSimulation(controler)

angulo = 350
velo = 7

CalcAppliedForce.input['degree'] = angulo
CalcAppliedForce.input['angularVelocity'] = velo
CalcAppliedForce.compute()

ValueAppliedForce = CalcAppliedForce.output['appliedForce']

print(ValueAppliedForce)

degree.view(sim=CalcAppliedForce)
angular_velocity.view(sim=CalcAppliedForce)
applied_force.view(sim=CalcAppliedForce)

plt.show()