import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt
from skfuzzy.control import Antecedent, Consequent, Rule, ControlSystemSimulation, ControlSystem
from Fuzzifier import Fuzzifier


class PendulumSwingUpFuzzifier(Fuzzifier):
    def define_antecedents(self) -> None:
        # region angle
        self.angle = Antecedent(np.arange(0, 401, 1), 'angle')

        self.angle['NLS'] = fuzz.trimf(self.angle.universe, [90, 130, 170])
        self.angle['NBS'] = fuzz.trimf(self.angle.universe, [30, 150, 170])
        self.angle['SALN'] = fuzz.trimf(self.angle.universe, [170, 175, 180])
        self.angle['Z'] = fuzz.trimf(self.angle.universe, [180, 180, 180])
        self.angle['SALP'] = fuzz.trimf(self.angle.universe, [180, 185, 190])
        self.angle['PBS'] = fuzz.trimf(self.angle.universe, [190, 210, 330])
        self.angle['PLS'] = fuzz.trimf(self.angle.universe, [190, 230, 270])
        # endregion

        # region angular velocity
        self.angular_velocity = Antecedent(np.arange(-10, 11, 0.1), 'angularVelocity')

        self.angular_velocity['NEG'] = fuzz.trapmf(self.angular_velocity.universe, [-10, -10, -1, 0])
        self.angular_velocity['ZS'] = fuzz.trapmf(self.angular_velocity.universe, [-0.1, 0, 0, 0.1])
        self.angular_velocity['POS'] = fuzz.trapmf(self.angular_velocity.universe, [0, 1, 10, 10])
        # endregion

    def define_rules(self) -> None:
        self.rules = [
            Rule(self.angle['NLS'] & self.angular_velocity['POS'], self.applied_force['NB']),
            Rule(self.angle['NBS'] & self.angular_velocity['POS'], self.applied_force['Z']),
            Rule(self.angle['SALN'] & self.angular_velocity['POS'], self.applied_force['N']),
            Rule(self.angle['Z'] & self.angular_velocity['ZS'], self.applied_force['P']),
            Rule(self.angle['SALP'] & self.angular_velocity['NEG'], self.applied_force['P']),
            Rule(self.angle['PBS'] & self.angular_velocity['NEG'], self.applied_force['Z']),
            Rule(self.angle['PLS'] & self.angular_velocity['NEG'], self.applied_force['PB'])
        ]

    def plot_antecedents(self) -> None:
        self.angle.view()
        self.angular_velocity.view()
        #plt.show()

    def simulate(self, attrs: 'list[float]') -> float:
        input_angle,  input_angular_velocity = attrs
        simulation = ControlSystemSimulation(ControlSystem(self.rules))

        simulation.input['angle'] = input_angle
        simulation.input['angularVelocity'] = input_angular_velocity
        simulation.compute()

        applied_force_value = simulation.output['appliedForce']

        self.plot_simulation(simulation)

        return applied_force_value

    def plot_simulation(self, simulation: ControlSystemSimulation) -> None:
        self.angle.view(simulation)
        self.angular_velocity.view(simulation)
        self.applied_force.view(simulation)

        plt.show()
