months = int(input(" Enter the number of months the servers will run: "))

server_costs = [3200, 5000, 1790, 8900, 2300]
monthly_cost = 100

total_cost = 0

print ("Server costs and average monthly costs:")

for server_cost in server_costs:
    total_server_cost = server_cost + monthly_cost * months
    average_monthly_cost = total_server_cost / months
    total_cost += total_server_cost
    print(f"The server costing {server_cost} costs on average {average_monthly_cost} each month.")
print(f"Total cost: {total_cost}")
