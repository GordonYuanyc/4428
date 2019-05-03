import math
import random

# a function that can generate a series of time in poisson process... I hope so...
def nextTime(rateParameter):
    return -math.log(1.0 - random.random()) / rateParameter

def calculate_remaining_customer(cust_num,rate,time):
    return int(cust_num * (1 - math.exp(-rate*time)))

def check_bankrupt(capital_lst,counter):
    if counter :
        return counter
    else:
        for cap in capital_lst:
            if cap < 0:
                return True
        return False


# this will generate time in floating point number form
# although the question says that policyholder pays every unit time, but the
# claim, I think, is not necessarily needs to be unit time
lambda_value = float(input("enter the lambda for all claims time: "))
# I'm assuming the poisson process is the time that new customer appears
# for example, a new customer appear at time 8 and time 12, each time a new one come
new_customer_rate = float(input("enter the rate for new customers: "))
customer_number_init = int(input("enter the number of initial customer: "))
customer_remain_rate = float(input("the rate that the customers remain: "))
capital_init = float(input("enter the initial capital: "))
payment = float(input("enter the payment: "))
time_period = int(input("enter time period we care (note*: this may be prior to the last time of claim): "))

# it should be distribution F but I'm just trying to say it's 20 everytime... just to make it easy
claim_every_time = 20

#claim_list = [nextTime(1/lambda_value) for i in range(10)]
#claim_list.sort()

#new_customer_list = [nextTime(1/new_customer_rate) for i in range(10)]
#new_customer_list.sort()
# uncomment the following 2 lines to see sorted time_list and new_customer_list
#print(time_list)
#print(new_customer_list)
#print(max(time_list))

#remaining_customer = calculate_remaining_customer(customer_number,customer_remain_rate,5)
#print(remaining_customer)
for rotate in range(100):
    claim_list = [nextTime(1 / lambda_value) for i in range(10)]
    claim_list.sort()
    new_customer_list = [nextTime(1 / new_customer_rate) for i in range(10)]
    new_customer_list.sort()
    customer_number = customer_number_init
    capital = capital_init
    bankrupt = False
    current_capital = []
    for time in range (time_period):
        if (len(claim_list) > 0):
            while (claim_list[0] < time):
                claim_list.pop(0)
                capital = capital - claim_every_time
                if (len(claim_list) == 0):
                    break

        if (len(new_customer_list) > 0):
            while (new_customer_list[0] < time):
                new_customer_list.pop(0)
                customer_number = customer_number + 1
                if (len(new_customer_list) == 0):
                    break
        if time > 0:
            capital = capital + customer_number * payment
        current_capital.append(capital)
        customer_number = calculate_remaining_customer(customer_number, customer_remain_rate, time)
        if (customer_number < 0):
            bankrupt = True

    bankrupt = check_bankrupt(current_capital,bankrupt)
    print(bankrupt)
    print (current_capital)