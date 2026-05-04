names = ["Alex", "Neeraj", "Lexus","Kim","Samantha","John","Emily","Michael","Sarah","David"]
message = f"Hello, {names[0].title()}! We invite you to our party tonight."
print(message)  # Output: Hello, Alex! We invite you to our party tonight.
message = f"Hello, {names[3].title()}! We invite you to our party tonight."
print(message)  # Output: Hello, Kim! We invite you to our party tonight.
message = f"Hello, {names[-1].title()}! We invite you to our party tonight."
print(message)  # Output: Hello, David
message = f"Hello, {names[2:5]}! We invite you to our party tonight."
print(message)  # Output: Hello, ['Lexus', 'Kim', 'Samantha']! We invite you to our party tonight.

