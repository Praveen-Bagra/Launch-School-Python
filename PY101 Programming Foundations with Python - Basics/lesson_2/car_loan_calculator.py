# Ask for loan amount.
# Ask for the Anuual Percentage Rate
# Ask for the loan duration in months.
# Calculate monthly payment
# Print the monthly payment.

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

while True:
    while True:
        prompt("Please enter the loan amount:")
        loan_amount = input()

        if not invalid_number(loan_amount):
            break

        prompt("Hmm...doesn't look like a valid amount.")

    while True:
        prompt("Please enter the Annual Percentage Rate:")
        yearly_rate = input()

        if not invalid_number(yearly_rate):
            break

        prompt("Hmm...doesn't look like a valid rate.")

    while True:
        prompt("Please enter the loan duration in months.")
        duration_in_months = input()

        if not invalid_number(duration_in_months):
            break

        prompt("Hmm...doesn't look like valid duration in months.")

    monthly_rate = float(yearly_rate) / (12 * 100)

    monthly_payment = (float(loan_amount) * (monthly_rate / (1 - (1
                    + monthly_rate) ** (-float(duration_in_months)))))

    prompt(f'The monthly payment is ${monthly_payment:.2f}')

    print()
    prompt("Thank you for using the Calculator.")
    prompt("Do you want to do another loan calculation?")
    answer = input()

    if answer and answer[0].lower() != 'y':
        break
