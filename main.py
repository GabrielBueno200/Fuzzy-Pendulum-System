from Fuzzifier import Fuzzifier
from PendulumSwingUpFuzzifier import PendulumSwingUpFuzzifier

SWING_UP_OPTION = 1
STABILIZATION_OPTION = 2


def calculate(fuzzifier: Fuzzifier, angle: float, input_angular_velocity: float) -> float:
    fuzzifier.plot_antecedents()
    fuzzifier.plot_consequents()

    output = fuzzifier.simulate(angle, input_angular_velocity)
    return output


def main():
    print("Simulation options:")
    print(f"{SWING_UP_OPTION} - Swing Up")
    print(f"{STABILIZATION_OPTION} - Stabilization")

    simulation_option = int(input("Choose a simulation option: "))

    # entries
    angle = float(input("\nType an entry angle: "))
    angular_velocity = float(input("Type the angular velocity: "))

    if simulation_option == SWING_UP_OPTION:
        swing_up_output = calculate(PendulumSwingUpFuzzifier(), angle, angular_velocity)
        print(f"Applied force for pendulum swing up: {swing_up_output}")


if __name__ == "__main__":
    main()
