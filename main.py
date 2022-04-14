from Fuzzifier import Fuzzifier
from PendulumStabilizationFuzzifier import PendulumStabilizationFuzzifier
from PendulumSwingUpFuzzifier import PendulumSwingUpFuzzifier

SWING_UP_OPTION = 1
STABILIZATION_OPTION = 2


def calculate(fuzzifier: Fuzzifier, attrs: 'list[float]') -> float:
    fuzzifier.plot_antecedents()
    fuzzifier.plot_consequents()

    output = fuzzifier.simulate(attrs)
    return output


def main():
    print("Simulation options:")
    print(f"{SWING_UP_OPTION} - Swing Up")
    print(f"{STABILIZATION_OPTION} - Stabilization")

    simulation_option = 0
    while simulation_option not in (SWING_UP_OPTION, STABILIZATION_OPTION):
        simulation_option = int(input("Choose a simulation option: "))

    # entries
    angle = float(input("\nType an entry angle: "))
    angular_velocity = float(input("Type the angular velocity: "))

    if simulation_option == SWING_UP_OPTION:
        attrs = [angle, angular_velocity]
        swing_up_output = calculate(PendulumSwingUpFuzzifier(), attrs)
        print(f"Applied force for pendulum swing up: {swing_up_output}")

    elif simulation_option == STABILIZATION_OPTION:
        cart_position = float(input("Type the cart position: "))
        cart_velocity = float(input("Type the cart velocity: "))
        attrs = [angle, angular_velocity, cart_position, cart_velocity]

        stabilization_output = calculate(PendulumStabilizationFuzzifier(), attrs)
        print(f"Applied force for pendulum swing up: {stabilization_output}")


if __name__ == "__main__":
    main()
