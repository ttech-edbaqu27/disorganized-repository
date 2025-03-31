age = int(input("Enter age: "))
income = int(input("Enter income: $"))
creditScore = int(input("Enter credit score: "))
eligibility = ""
risk = ""

# if (age >= 18) and (income >= 25000) and (creditScore >= 650):
#     if (age >= 30) and (income >= 50000) and (creditScore >= 700):
#         print("Low Risk")
#     elif (age >= 25) and (income <= 35000) and (creditScore >= 650):
#         print("Medium Risk")
#     else:
#         print("High risk")

if age >= 18:
    if income >= 25000:
        if creditScore >= 650:
            if age >= 30 and income >= 50000 and creditScore >= 700:
                risk = "Low Risk"
            elif age >= 25 and income >= 35000 and creditScore >= 650:
                risk = "Medium Risk"
            else:
                risk = "High Risk"
            eligibility = "Eligible"
        else:
            eligibility = "Not Eligible!"
            risk = "N/A"  
    else:
        eligibility = "Not Eligible!"
        risk = "N/A"
else:
    eligibility = "Not Eligible!"
    risk = "N/A"

print(f"Loan Eligibility: {eligibility}")
if eligibility == "Eligible":
    print(f"Risk Category: {risk}")
