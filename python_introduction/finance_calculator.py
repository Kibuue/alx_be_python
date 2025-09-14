Monthly_Income = int(input("Enter your monthly income: "))
Total_Monthly_Expenses = int(input("Enter your total monthly expenses: "))

Monthly_Savings = float(Monthly_Income) - float(Total_Monthly_Expenses)

Annual_interest_Rate = 0.05
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * Annual_interest_Rate)

print("Your monthly savings is: ", Monthly_Savings)
print("Your projected savings for one year, with interest, is: ", Projected_Savings)
