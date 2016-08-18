cost_in_cents = int(input("Enter cents per kWh: "))
daily_use = float(input("Enter daily use in kWh: "))
number_billing_days = int(input("Enter number of billing days: "))
estimated_bill = (cost_in_cents*daily_use*number_billing_days)/100
print("Estimated bill:$", str(estimated_bill))
