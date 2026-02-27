previous_val = int(input())
current_val = int(input())
print(f"Sequence starts at {previous_val}.")

while current_val < previous_val:
    print(f"{current_val} is less than {previous_val}. Sequence is decreasing.")
    previous_val = current_val
    current_val = int(input())
