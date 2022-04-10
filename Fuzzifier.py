import matplotlib.pyplot as plt
from skfuzzy import control as ctrl


class Fuzzifier:
    angle: ctrl.Antecedent
    angular_velocity: ctrl.Antecedent

    applied_force: ctrl.Consequent

    rules: list[ctrl.Rule]

    def __init__(self):
        self.define_antecedents()
        self.define_consequents()
        self.define_rules()

    def define_antecedents(self):
        pass

    def define_consequents(self):
        pass

    def define_rules(self):
        pass

    def plot_antecedents(self):
        self.angle.view()
        self.applied_force.view()
        plt.show()

    def plot_consequents(self):
        self.applied_force.view()
        plt.show()

    def simulate(self, angle: float, angular_velocity: float) -> float:
        control_system = ctrl.ControlSystem(self.rules)
        simulation = ctrl.ControlSystemSimulation(control_system)

        simulation.input['angle'] = angle
        simulation.input['angularVelocity'] = angular_velocity
        simulation.compute()

        applied_force_value = simulation.output['appliedForce']

        self.plot_simulation(simulation)

        return applied_force_value

    def plot_simulation(self, simulation: ctrl.ControlSystemSimulation):
        self.angle.view(simulation)
        self.angular_velocity.view(simulation)
        self.applied_force.view(simulation)

        plt.show()
