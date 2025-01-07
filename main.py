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