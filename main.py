import random

# ----------------------------
# Step 1: Define Problem Parameters
# ----------------------------
# Problem: Given a set of items with weights and values, find the subset that maximizes value without exceeding the weight limit.

def knapsack_fitness(individual, weights, values, weight_limit):
    total_weight = sum(individual[i] * weights[i] for i in range(len(individual)))
    total_value = sum(individual[i] * values[i] for i in range(len(individual)))
    return total_value if total_weight <= weight_limit else 0

# ----------------------------
# Step 2: Generate Random Individual
# ----------------------------
def random_individual(n):
    return [random.randint(0, 1) for _ in range(n)]

# ----------------------------
# Step 3: Initialize Population
# ----------------------------
def initialize_population(pop_size, n):
    return [random_individual(n) for _ in range(pop_size)]

# ----------------------------
# Step 4: Select Top Individuals
# ----------------------------
def select_top_individuals(population, fitness_func, k, weights, values, weight_limit):
    return sorted(population, key=lambda ind: fitness_func(ind, weights, values, weight_limit), reverse=True)[:k]

# ----------------------------
# Step 5: Learn Probability Distribution
# ----------------------------
def learn_distribution(top_individuals, n):
    probabilities = [0.0] * n
    for i in range(n):
        ones_count = sum(ind[i] for ind in top_individuals)
        probabilities[i] = ones_count / len(top_individuals)
    return probabilities

# ----------------------------
# Step 6: Sample New Individuals
# ----------------------------
def sample_new_individual(probabilities):
    return [1 if random.random() < p else 0 for p in probabilities]

# ----------------------------
# Step 7: Main EDA Loop
# ----------------------------
def eda_knapsack(weights, values, weight_limit, population_size, generations, top_k):
    n = len(weights)  # Number of items
    population = initialize_population(population_size, n)

    for generation in range(generations):
        top_individuals = select_top_individuals(
            population, knapsack_fitness, top_k, weights, values, weight_limit
        )
        probabilities = learn_distribution(top_individuals, n)
        population = [sample_new_individual(probabilities) for _ in range(population_size)]

        best = max(population, key=lambda ind: knapsack_fitness(ind, weights, values, weight_limit))
        best_fitness = knapsack_fitness(best, weights, values, weight_limit)

        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}, Best Individual = {best}")
        print(f"Probabilities = {probabilities}")
        print("-" * 50)

    return max(population, key=lambda ind: knapsack_fitness(ind, weights, values, weight_limit))