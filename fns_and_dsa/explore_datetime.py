import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted = current_date.strftime("%d-%m-%y , %I:%M:%S ")
    print(f"Current date and time: {formatted}")
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date.date() + datetime.timedelta(days= number_of_days)
    print(f"Future date: {future_date}")



def main():
    display_current_datetime()
    
    
    
if __name__ == "__main__":
    main()
