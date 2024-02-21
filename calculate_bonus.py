def calculate_earnings(workers):
    total_earnings = 0
    for worker in workers:
        worker["Earning"] = worker["Worked Hours"] * worker["Hourly Rate"]
        total_earnings += worker["Earning"]
    return total_earnings

def calculate_bonus_and_average_rate(workers, budget, total_earnings):
    available_bonus = budget - total_earnings
    average_rate = available_bonus / total_earnings if total_earnings > 0 else 0
    for worker in workers:
        worker["Bonus"] = worker["Earning"] * average_rate
    return average_rate

def print_project_view(workers, average_rate):
    print("\nWorkers\tEarning\tAverage Rate\tBonus")
    for worker in workers:
        print(f"{worker['Name']}\t${worker['Earning']:.2f}\t{average_rate:.10f}\t${worker['Bonus']:.2f}")
    total_earnings = sum(worker["Earning"] for worker in workers)
    total_bonus = sum(worker["Bonus"] for worker in workers)
    print(f"Total\t${total_earnings:.2f}\t{average_rate:.10f}\t${total_bonus:.2f}")

def input_workers():
    workers = []
    while True:
        name = input("Enter worker name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        hourly_rate = float(input(f"Enter hourly rate for {name}: "))
        worked_hours = float(input(f"Enter worked hours for {name} (in hours): "))
        workers.append({"Name": name, "Hourly Rate": hourly_rate, "Worked Hours": worked_hours, "Earning": 0, "Bonus": 0})
    return workers

def main():
    workers = input_workers()
    budget = float(input("Enter project budget: "))
    status = input("Enter project status (approve/pending): ").lower()

    total_earnings = calculate_earnings(workers)

    if status == "approve":
        average_rate = calculate_bonus_and_average_rate(workers, budget, total_earnings)
    elif status == "pending":
        average_rate = 0
        for worker in workers:
            worker["Bonus"] = 0 

    print_project_view(workers, average_rate)
    print(workers)

if __name__ == "__main__":
    main()
