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

    def plot_antecedents(self) -> None:
        self.angle.view()
        self.applied_force.view()
        plt.show()

    def plot_consequents(self) -> None:
        self.applied_force.view()
        plt.show()

    def simulate(self, input_angle: float, input_angular_velocity: float) -> float:
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
