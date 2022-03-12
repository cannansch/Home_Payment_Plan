input_1 = input ("What is the cost of the property?.. $")
input_2 = input ("What is the interest?.. %")
input_3 = input ("Within how many years would you like to pay this property off?.. ")
input_4 = input ("How many people will be paying for this property.. ")

#principle
p = float(input_1)

#interest rate
r = (float(input_2)/100)/12

#number of  payments
n = float(input_3)*12

#number of people making payments
d = float(input_4)

#formula p*r*(r+1)**n/1+r**n-1

a = p * r
b = (r+1)**n
c = (1+r)**n-1

simp_formula = str(round(a*b/c, 2))
total_cost = (a*b/c)*360
monthly_interest = (a*b/c) - (p/n)
goal_total = (monthly_interest*n) + p
per_person = ((goal_total/float(input_3))/12)/d

print("Total monthly payments will be $" + simp_formula)
print("Total amount paid will be $" + str(round(goal_total, 2)))
print("Monthly cost per person will be $" + str(round(per_person, 2)))