import csv
from datetime import datetime

def read_csv_file(file_name): 
    output=[] 
    with open(file_name) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            # print(', '.join(row))
            output.append(row)
    return output

def convert_mmddyyyy_date(date): 
    return datetime.strptime(date, '%m/%d/%Y')

def get_month_name(date):
    return date.strftime('%B')

def transform_daily_to_monthly(data):
    '''Transform the data from daily to monthly format.

    Args:
        data: a list of lists, where each sublist represents data
            for a specific day.

    Returns: a list of lists, where each sublist represents data
        for a whole month.
    '''
    output=[]
    current_month = None
    month_data=[]
    for row in data: 
        # print (row[0])
        print()
        date = row[0]
        print(date)  
        month = get_month_name(convert_mmddyyyy_date(date))
        print(month)
        if current_month != month:
            print('New month!')
            current_month = month
            if month_data:
                output.append(month_data)
            month_data = []
        
        month_data.append(row)
    return output       
    

if __name__ == "__main__":
    all_data = read_csv_file('data/2020_2021_turtle_data.csv')[1:]
    monthly_data = transform_daily_to_monthly(all_data)

    for item in monthly_data:
        print()     
        print (item) 

    # date = convert_mmddyyyy_date("6/7/2021")
    # print(get_month_name(date))   




































   

