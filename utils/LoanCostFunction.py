revenue = 0  
profit_percentage_last_year = 0 
inflation=0

simple_interest = 0 
interest_rate = 0 
amount_of_loan = 0 
time_to_repay = 0 
past_debt_to_repay = 0 

sustainability = 0 
competition_scale = 0 
management_effectivity = 0 
startup = 0 
cibil_score = 0 

#balance the decrease in amount of money
interest_rate -= inflation

# substract from the net revenue
external_cost = (len(str(amount_of_loan))-1)*(
    5*(1-sustainability) + 
    3*(1-management_effectivity) +
    2*(startup) + 
    10*(900 - cibil_score)/100
)   

loan_interest_cost = amount_of_loan*(1+interest_rate*time_to_repay) if simple_interest else amount_of_loan*(pow((1 + interest_rate/100),time_to_repay))

#the net profit conceded over the period of time
net_revenue = revenue*profit_percentage_last_year*time_to_repay

residue_left_after_time = net_revenue - external_cost - loan_interest_cost

if residue_left_after_time < 0:
    if abs(residue_left_after_time) > 0.1*net_revenue:
        print("Very High Risk involved")
    else:
        print("Moderate risk involved")
else:
    if (residue_left_after_time) < 0.1*net_revenue:
        print("It is fine to grant the loan")
    else:
        print("There is a huge scope of expansion in the business")