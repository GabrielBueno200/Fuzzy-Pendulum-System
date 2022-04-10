import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from Fuzzifier import Fuzzifier


class PendulumSwingUpFuzzifier(Fuzzifier):
    def define_antecedents(self):
        self.angle = ctrl.Antecedent(np.arange(0, 401, 1), 'angle')

        self.angle['NLS'] = fuzz.trimf(self.angle.universe, [90, 130, 170])
        self.angle['NBS'] = fuzz.trimf(self.angle.universe, [30, 150, 170])
        self.angle['SALN'] = fuzz.trimf(self.angle.universe, [170, 175, 180])
        self.angle['Z'] = fuzz.trimf(self.angle.universe, [180, 180, 180])
        self.angle['SALP'] = fuzz.trimf(self.angle.universe, [180, 185, 190])
        self.angle['PBS'] = fuzz.trimf(self.angle.universe, [190, 210, 330])
        self.angle['PLS'] = fuzz.trimf(self.angle.universe, [190, 230, 270])
        # endregion

        # region angular velocity
        self.angular_velocity = ctrl.Antecedent(np.arange(-10, 11, 0.1), 'angularVelocity')

        self.angular_velocity['NEG'] = fuzz.trapmf(self.angular_velocity.universe, [-10, -10, -1, 0])
        self.angular_velocity['ZS'] = fuzz.trapmf(self.angular_velocity.universe, [-0.1, 0, 0, 0.1])
        self.angular_velocity['POS'] = fuzz.trapmf(self.angular_velocity.universe, [0, 1, 10, 10])
        # endregion

    def define_consequents(self):
        self.applied_force = ctrl.Consequent(np.arange(-2, 2, 0.1), 'appliedForce')

        self.applied_force['NVVB'] = fuzz.trapmf(self.applied_force.universe, [-6, -6, -4.8, -3.6])
        self.applied_force['NVB'] = fuzz.trimf(self.applied_force.universe, [-4.8, -3.6, -2.4])
        self.applied_force['NB'] = fuzz.trimf(self.applied_force.universe, [-3.6, -2.4, -1.2])
        self.applied_force['N'] = fuzz.trimf(self.applied_force.universe, [-2.4, -1.2, 0])
        self.applied_force['Z'] = fuzz.trimf(self.applied_force.universe, [-1.2, 0, 1.2])
        self.applied_force['P'] = fuzz.trimf(self.applied_force.universe, [0, 1.2, 2.4])
        self.applied_force['PB'] = fuzz.trimf(self.applied_force.universe, [1.2, 2.4, 3.6])
        self.applied_force['PVB'] = fuzz.trimf(self.applied_force.universe, [2.4, 3.6, 4.8])
        self.applied_force['PVVB'] = fuzz.trapmf(self.applied_force.universe, [3.6, 4.8, 6, 6])

    def define_rules(self):
        self.rules = [
            ctrl.Rule(self.angle['NLS'] & self.angular_velocity['POS'], self.applied_force['NB']),
            ctrl.Rule(self.angle['NBS'] & self.angular_velocity['POS'], self.applied_force['Z']),
            ctrl.Rule(self.angle['SALN'] & self.angular_velocity['POS'], self.applied_force['N']),
            ctrl.Rule(self.angle['Z'] & self.angular_velocity['ZS'], self.applied_force['P']),
            ctrl.Rule(self.angle['SALP'] & self.angular_velocity['NEG'], self.applied_force['P']),
            ctrl.Rule(self.angle['PBS'] & self.angular_velocity['NEG'], self.applied_force['Z']),
            ctrl.Rule(self.angle['PLS'] & self.angular_velocity['NEG'], self.applied_force['PB'])
        ]
