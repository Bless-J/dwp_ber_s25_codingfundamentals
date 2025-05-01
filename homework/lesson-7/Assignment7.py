shopping_list = [] 

while True:
    item = input("Enter an item ('done' to finish): ").strip()
    
    if item.lower() == 'done':
        break

    if not item:
        continue
    
    if item not in shopping_list:
        shopping_list.append(item)
    else:
        print(f"'{item}' is already in your list.")
shopping_list.sort()

print("\nYour shopping list:")

for i, item in enumerate(shopping_list, start=1):
    print(f"{i}. {item}")

print(f"\nTotal items: {len(shopping_list)}")
