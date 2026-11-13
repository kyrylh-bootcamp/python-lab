# 1. algorithm
# 2. write the business logic
# 3. check if this is a functional candidate. If yes, define a function just above the logic.
# 4. Make the logic part of the function.
# 5. Check if there are any external factors in the code.
# 6. If yes, replace them with a variable and pass it as a function parameter.
# 7. Return a value if there is one; otherwise, return None explicitly.
# 8. Annotate the function.
# 9. Run the function.

"""Rule 1: If the amount is greater than 10,000, flag it as FLAGGED.
Rule 2: If the current location is NOT in the user's history list, flag it as
REVIEW_REQUIRED.
Rule 3: If both Rule 1 and Rule 2 are met, set the status to BLOCKED.
Add a new key fraud_metrics to each dictionary containing the results of these checks."""

from collections.abc import Callable

txns = [
    {"txn_id": "T101", "user_id": "U1", "amount": 600, "location": "NY", "history": ["NY", "NY"]},
    {"txn_id": "T102", "user_id": "U2", "amount": 12000, "location": "NY", "history": ["NY"]},
    {"txn_id": "T103", "user_id": "U1", "amount": 100, "location": "London", "history": ["NY", "NY"]},
]


def flag_the_user(txn_data: list[dict], criteria: int) -> list[str]:
    flagged_users = []
    for txn in txn_data:
        amount = txn["amount"]
        user_id = txn["user_id"]
        amount_flagged = amount > 10000
        location_review_required = txn["location"] not in txn["history"]
        both_rules_met = amount_flagged and location_review_required

        txn["fraud_metrics"] = {
            "amount_flag": "FLAGGED" if amount_flagged else None,
            "location_flag": "REVIEW_REQUIRED" if location_review_required else None,
            "status": "BLOCKED" if both_rules_met else None,
        }

        if amount > criteria:
            txn["flag"] = "flagged"
            flagged_users.append(user_id)
    return flagged_users


def validation_by_manager(
    func: Callable[[list[dict], int], list[str]],
    user_id: str,
    data: list[dict],
    criteria: int,
) -> None:
    for user in func(data, criteria):
        if user == user_id:
            print("skip the user")
        else:
            print("validate the user")


print(flag_the_user(txns, 500))
print(flag_the_user(txns, 10000))
validation_by_manager(flag_the_user, "U1", txns, 500)


print("\nNew task=====\n")


# Sample E-commerce Inventory Database
inventory = {
    "SKU_101": {"name": "Wireless Mouse", "price": 25.00, "stock_count": 50, "category": "Electronics"},
    "SKU_102": {"name": "Gaming Keyboard", "price": 80.00, "stock_count": 0, "category": "Electronics"},
    "SKU_103": {"name": "Yoga Mat", "price": 30.00, "stock_count": 15, "category": "Fitness"},
    "SKU_104": {"name": "Bluetooth Speaker", "price": 120.00, "stock_count": 5, "category": "Electronics"},
    "SKU_105": {"name": "Protein Shaker", "price": 15.00, "stock_count": 0, "category": "Fitness"},
}

#rule 1: UPDATE (Flash Sale):  #    Apply a 15% discount to the 'price' of every item in the "Electronics" category.

def update(inventory_data: dict[str, dict]) -> None:
    for sku, item in inventory_data.items():
        if item["category"] == "Electronics":
            original_price = item["price"]
            discounted_price = original_price * (1 - 0.15)
            item["price"] = round(discounted_price, 2)  # Round to 2 decimal places



update(inventory)

#rule 2: LOGIC (Restock Alert):  #    Loop through the inventory. If 'stock_count' is 0, add a new key  #    called 'restock_urgent' with the value True.

def check_restock_alerts(inventory_data: dict[str, dict]) -> None:
    for sku, item in inventory_data.items():
        if item["stock_count"] == 0:
            item["restock_urgent"] = True
            print(f"Restock Alert for {sku}: {item['name']} is out of stock!")

check_restock_alerts(inventory)

print("\n")
#rule 3: SAFE ACCESS (Data Integrity):  #    Check for a 'last_sold' key. If it doesn't exist, use .setdefault()  #    to set it to "Never".

def last_sold_check(inventory_data: dict[str, dict]) -> None:
    for sku, item in inventory_data.items():
        item.setdefault("last_sold", "Never")
        print(f"{sku}: Last Sold: {item['last_sold']}")


last_sold_check(inventory)

#rule 4: VIEW: Print the final updated inventory.

def print_inventory(inventory_data: dict[str, dict]) -> None:
    print("\nFinal Updated Inventory:")
    for sku, item in inventory_data.items():
        print(f"{sku}: {item}")


print_inventory(inventory)
