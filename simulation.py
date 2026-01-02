# Simulation model

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    gini_values = []

    # Simulation loop
    for run in range(10):
        population = np.full(20, 10)
        for day in range(1000):
            # select two random individuals
            i, j = np.random.choice(len(population), 2, replace=False)
            # i gives a random amount of resources to j
            amount = np.random.randint(1, population[i] + 1) if population[i] > 0 else 0
            population[i] -= amount
            population[j] += amount

        # get a measure of inequality
        gini_coefficient = (np.sum(np.abs(np.subtract.outer(population, population))) /
                            (2 * len(population) * np.mean(population)))
        gini_values.append(gini_coefficient)
    print("Gini coefficients over 10 runs:", gini_values)
    # plot histogram of gini values
    plt.hist(gini_values, bins=10, range=(0, 1), rwidth=0.8)
    plt.xlabel('Gini Coefficient')
    plt.ylabel('Frequency')
    plt.title('Distribution of Gini Coefficients over 10 Runs')
    plt.show()
