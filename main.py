from PendulumSwingUpFuzzifier import PendulumSwingUpFuzzifier


def main():
    angle = float(input("Type an entry angle: "))
    applied_force = float(input("Type the force to be applied: "))

    swing_up_fuzzifier = PendulumSwingUpFuzzifier()
    swing_up_fuzzifier.plot_antecedents()
    swing_up_fuzzifier.plot_consequents()

    swing_up_result = swing_up_fuzzifier.simulate(angle, applied_force)

    print(f"Applied force for pendulum swing up: {swing_up_result}")

if __name__ == "__main__":
    main()
