from datetime import datetime
from random import randint, sample


"Excesize 1"

def get_days_from_today(date):
    date_format="%Y-%m-%d"
    try:
        specified_date = datetime.strptime(date, date_format).date()
        current_date = datetime.now().date()
        difference = (current_date - specified_date).days
        return difference

    except ValueError:
        return "Invalid date format. Try again..."
    
if __name__ == "__main__":
    date_input = "2022-02-24"
    days_difference = get_days_from_today(date_input)
    print(f"Days from {date_input} to today: {days_difference}")



"Excesize 2"

def get_numbers_ticket (min_value, max_value, quantity):
    if not (1<=min_value<max_value<=1000):
        return []

    if not (1<=quantity<=max_value-min_value+1):
        return []


    lottery_numbers = set ()
    while len (lottery_numbers) != quantity:
        lottery_numbers.add(randint(min_value, max_value+1))
    return(sorted(sample(list(lottery_numbers), k=quantity)))


lottery_numbers = get_numbers_ticket(1, 43, 20)
print("Ваші лотерейні числа:", lottery_numbers)
    

