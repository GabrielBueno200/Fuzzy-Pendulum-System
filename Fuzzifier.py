from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy.control import Antecedent, Consequent, Rule, ControlSystemSimulation


class Fuzzifier(ABC):
    angle: Antecedent
    angular_velocity: Antecedent

    applied_force: Consequent

    rules: list[Rule]

    def __init__(self):
        self.define_antecedents()
        self.define_consequents()
        self.define_rules()

    @abstractmethod
    def define_antecedents(self) -> None:
        pass

    def define_consequents(self) -> None:
        self.applied_force = Consequent(np.arange(-6, 6, 0.2), 'appliedForce')

        self.applied_force['NVVB'] = fuzz.trapmf(self.applied_force.universe, [-6, -6, -4.8, -3.6])
        self.applied_force['NVB'] = fuzz.trimf(self.applied_force.universe, [-4.8, -3.6, -2.4])
        self.applied_force['NB'] = fuzz.trimf(self.applied_force.universe, [-3.6, -2.4, -1.2])
        self.applied_force['N'] = fuzz.trimf(self.applied_force.universe, [-2.4, -1.2, 0])
        self.applied_force['Z'] = fuzz.trimf(self.applied_force.universe, [-1.2, 0, 1.2])
        self.applied_force['P'] = fuzz.trimf(self.applied_force.universe, [0, 1.2, 2.4])
        self.applied_force['PB'] = fuzz.trimf(self.applied_force.universe, [1.2, 2.4, 3.6])
        self.applied_force['PVB'] = fuzz.trimf(self.applied_force.universe, [2.4, 3.6, 4.8])
        self.applied_force['PVVB'] = fuzz.trapmf(self.applied_force.universe, [3.6, 4.8, 6, 6])

    @abstractmethod
    def define_rules(self) -> None:
        pass

    @abstractmethod
    def plot_antecedents(self) -> None:
        pass

    def plot_consequents(self) -> None:
        self.applied_force.view()
        plt.show()

    @abstractmethod
    def simulate(self, attrs: list[float]) -> float:
        pass

    @abstractmethod
    def plot_simulation(self, simulation: ControlSystemSimulation) -> None:
        pass
