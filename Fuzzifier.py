from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
from skfuzzy.control import Antecedent, Consequent, Rule, ControlSystem, ControlSystemSimulation


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

    @abstractmethod
    def define_consequents(self) -> None:
        pass

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
