total_sum = 0
for _ in range(5):
    while True:
        user_input = input("Enter an integer: ")
        try:
            total_sum += int(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

print("Resulting sum:", total_sum)
