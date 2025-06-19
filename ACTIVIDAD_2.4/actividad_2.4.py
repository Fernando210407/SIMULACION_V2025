import pandas as pd
from pulp import LpProblem, LpVariable, LpMaximize, lpSum, LpBinary, value

df = pd.read_csv("mochila_almno_.csv")


for i in range(len(df)):
    row = df.iloc[i]
    weights = [int(x) for x in row['Weights'].strip('[]').split()]
    prices = [int(x) for x in row['Prices'].strip('[]').split()]


    capacity = int(row['Capacity'])
    n_items = len(weights)

    
    prob = LpProblem("Knapsack", LpMaximize)
    x = [LpVariable(f"x_{j}", cat=LpBinary) for j in range(n_items)]

    
    prob += lpSum(prices[j] * x[j] for j in range(n_items)), "Total Price"
    prob += lpSum(weights[j] * x[j] for j in range(n_items)) <= capacity, "Capacity Constraint"

    
    prob.solve()

   
    best_picks = [int(x[j].varValue) for j in range(n_items)]
    best_price = value(prob.objective)
    avg_weights = sum(weights) / n_items
    avg_prices = sum(prices) / n_items
    cost_function = " + ".join([f"{prices[j]}*x_{j}" for j in range(n_items)])
    constraint = " + ".join([f"{weights[j]}*x_{j}" for j in range(n_items)]) + f" <= {capacity}"

    
    df.at[i, 'Best picks'] = str(best_picks)
    df.at[i, 'Best price'] = best_price
    df.at[i, 'Average Weights'] = avg_weights
    df.at[i, 'Average Prices'] = avg_prices
    df.at[i, 'Cost function'] = cost_function
    df.at[i, 'Constraint'] = constraint


df.to_csv("mochila_almno_resultado.csv", index=False)