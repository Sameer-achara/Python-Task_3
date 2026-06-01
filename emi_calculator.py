def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / (12 * 100)

    emi = (
        principal
        * monthly_rate
        * (1 + monthly_rate) ** tenure_months
    ) / (
        (1 + monthly_rate) ** tenure_months - 1
    )

    return emi


p = float(input("Enter Loan Amount: "))
r = float(input("Enter Annual Interest Rate (%): "))
t = int(input("Enter Tenure (months): "))

emi = calculate_emi(p, r, t)

print("Monthly EMI =", round(emi, 2))
