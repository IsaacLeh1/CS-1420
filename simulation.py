import sys

def growth_equation(current_population, growth_rate):
    return growth_rate * current_population * (1 - current_population)

def main():
    if len(sys.argv) != 4:
        print("Use the following format: python simulation.py <value1> <value2> <value3>")
        return

    try:
        values = [float(arg) for arg in sys.argv[1:]]
    except ValueError:
        print("Invalid input. Please provide numeric values.")
        return

    current_population = None
    growth_rate = None
    iterations = None

    for value in values:
        if 0 < value < 1:
            current_population = value
        elif 0 < value < 4:
            growth_rate = value
        elif value > 4:
            iterations = int(value)

    if current_population is None or growth_rate is None or iterations is None:
        print("Invalid input ranges. Ensure current population is between 0 and 1, population growth is between 0 and 4, and iterations value is greater than 4.")
        return

    iteration_count = 1
    while iteration_count <= iterations:
        print(f"{iteration_count}    {current_population:.3f}")
        current_population = growth_equation(current_population, growth_rate)
        iteration_count += 1

if __name__ == "__main__":
    main()