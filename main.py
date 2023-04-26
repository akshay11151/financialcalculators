def compound_interest(principal, rate, time):
    # Calculate compound interest
    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal

    # Round to 2 decimal places
    amount = round(amount, 2)
    interest = round(interest, 2)

    return amount, interest


def loan_calculator(principal, rate, time):
    # Calculate loan payments
    r = rate / 1200  # monthly interest rate
    n = time * 12  # total number of payments
    payment = principal * r / (1 - (1 + r) ** -n)

    # Round to 2 decimal places
    payment = round(payment, 2)

    return payment


def mortgage_calculator(principal, rate, time):
    # Calculate mortgage payments
    r = rate / 1200  # monthly interest rate
    n = time * 12  # total number of payments
    payment = principal * r / (1 - (1 + r) ** -n)

    # Round to 2 decimal places
    payment = round(payment, 2)

    return payment


def retirement_calculator(principal, rate, time, monthly_savings):
    # Calculate retirement savings
    r = rate / 1200  # monthly interest rate
    n = time * 12  # total number of payments
    future_value = principal * (1 + r) ** n + monthly_savings * ((1 + r) ** n - 1) / r

    # Round to 2 decimal places
    future_value = round(future_value, 2)

    return future_value


# Collect input from user
print("Select a financial calculator to use:")
print("1. Compound Interest Calculator")
print("2. Loan Calculator")
print("3. Mortgage Calculator")
print("4. Retirement Calculator")
choice = int(input("Enter your choice: "))

if choice == 1:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate: "))
    time = int(input("Enter the time period (in years): "))
    amount, interest = compound_interest(principal, rate, time)
    print("Compound interest after", time, "years is", amount)
    print("Interest earned is", interest)

elif choice == 2:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate: "))
    time = int(input("Enter the time period (in years): "))
    payment = loan_calculator(principal, rate, time)
    print("Monthly payment is", payment)

elif choice == 3:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate: "))
    time = int(input("Enter the time period (in years): "))
    payment = mortgage_calculator(principal, rate, time)
    print("Monthly payment is", payment)

elif choice == 4:
    principal = float(input("Enter the current retirement savings: "))
    rate = float(input("Enter the annual interest rate: "))
    time = int(input("Enter the time until retirement (in years): "))
    monthly_savings = float(input("Enter the monthly savings: "))
    future_value = retirement_calculator(principal, rate, time, monthly_savings)
    print("Future retirement savings is", future_value)

else:
    print("Invalid choice. Please enter a number from 1 to 4.")
