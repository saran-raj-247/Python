def manage_shoe_inventory():
    x = int(input())
    shoe_sizes = list(map(int, input().split()))
    shoe_inventory = {}
    for size in shoe_sizes:
        if size in shoe_inventory:
            shoe_inventory[size] += 1
        else:
            shoe_inventory[size] = 1

    n = int(input())
    total_revenue = 0
    for _ in range(n):
        size, price = map(int, input().split())
        if size in shoe_inventory and shoe_inventory[size] > 0:
            total_revenue += price
            shoe_inventory[size] -= 1

    print(total_revenue)

manage_shoe_inventory()
