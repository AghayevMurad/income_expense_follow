
def income_expense_follow():
     income = float(input("Enter your monthly income: "))
     expense = float(input("Enter your monthly expense: "))

     residual = income - expense

     if residual > 0:
         print("Congratulations! You're keeping your spending under control.")
     elif residual < 0:
         print("Attention! Your spending exceeds your income.")
         print("Some saving tips:")
         print("- Cook at home instead of eating out for less meals.")
         print("- Review your subscriptions and cancel any unnecessary ones.")
         print("- Search for ways to lower your bills such as electricity and water.")

     else:
         print("Your spending is exactly equal to your income.")
         print("Watch out, you may need to save.")




income_expense_follow()
