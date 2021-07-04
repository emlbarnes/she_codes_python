from datetime import datetime

import (2019_2020_turtle_data_raw.csv)
def convert_mmddyyyy_date(mmddyyyy): 
    '''Takes a date in the format mm/dd/yyyy and converts it to a datetime object.

    Args:
        date: string of a date in the mm/dd/yyyy format.

    Returns: a datetime object.
    '''

    return datetime.strptime(date, '%m/%d/%Y')

    import {csv}
    

def get_month_name(date):
    '''Gets the month name from a datetime object.

    Args:
        date: a datetime object.

    Returns: the month name from the given date
        (e.g. "January", "February", etc).
    '''
    return date.strftime('%B')
    import {datetime}
    print (file= (2019_2020_turtle_data_raw)
19/12/19,3,14,,7
20/12/19,,4,,5
21/12/19,9,3,,9
22/12/19,8,3,1,10
23/12/19,6,5,1,8
24/12/19,8,5,2,11
25/12/19,5,12,1,16
26/12/19,4,25,3,4
27/12/19,10,11,4,12
28/12/19,12,13,4,10
29/12/19,9,4,1,8
30/12/19,5,6,2,8
31/1/19,7,3,,10
1/1/20,4,2,,5
2/1/20,1,0,,8
3/1/20,1,1,,7
4/1/20,0,0,,11
5/1/20,1,0,,8
6/1/20,1,0,,6
7/1/20,2,0,,2
8/1/20,2,0,,5
9/1/20,4,1,1,4
10/1/20,5,1,,4
11/1/20,0,1,1,9
12/1/20,1,1,,6
13/1/20,1,0,,8
14/1/20,1,0,,1
15/1/20,1,0,,1
16/1/20,0,0,,0
17/1/20,0,3,1,0
18/1/20,1,1,,0
19/1/20,0,0,,0
20/1/20,0,0,,0
21/1/20,0,1,,9
22/1/20,3,0,,0
23/1/20,3,1,,0
24/1/20,0,0,,0
25/1/20,0,0,,0
26/1/20,1,1,,0
27/1/20,0,0,,0
28/1/20,0,0,,0
29/1/20,1,0,,0
30/1/20,0,0,,0
31/1/20,0,0,,0
1/2/20,0,0,0,0
2/2/20,0,0,0,0
3/2/20,0,0,0,0
4/2/20,0,0,0,0
5/2/20,0,0,0,0
6/2/20,0,0,0,0
7/2/20,0,0,0,0
8/2/20,0,0,0,0
9/2/20,0,0,0,0
10/2/20,0,0,0,0
11/2/20,0,0,0,0
12/2/20,0,0,0,0
13/2/20,0,0,0,0
14/2/20,0,0,0,0
15/2/20,0,0,0,0
16/2/20,0,0,0,0
17/2/20,0,0,0,0
18/2/20,0,0,0,0
19/2/20,0,0,0,0
20/2/20,0,0,0,0
21/2/20,0,0,0,0
22/2/20,0,0,0,0
23/2/20,0,0,0,0
24/2/20,0,0,0,0
25/2/20,0,0,0,0
26/2/20,0,0,0,0
27/2/20,0,0,0,0
28/2/20,0,0,0,0
29/2/20,0,0,0,0
def format_text(text, spaces):
    '''Formats a string to be left aligned and take up a certain number of
        characters.

    Args:
        text: a string.
        spaces: the number of spaces the string should take up.
 
    Returns: the formatted string.
    '''
    return f"{tt:<{spaces}}"


def read_csv_file(file_name):{2019_2020_turtle_data_raw.csv}
    '''Reads a csv file and returns the data as a list.

    Args:
        file_name: a string representing the path and name of a csv file.

    Returns: a list.
    '''
    pass


def output_overall_statistics(monthly_data):
    '''Prints a summary of the total number of nests, hatched nests, false
        crawls, hit rocks and nest predation.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
        name and total values for that month.
    '''
    pass


def output_monthly_statistics(monthly_data):
    '''Prints a summary of the total number of nests, hatched nests, false crawls,
       hit rocks and nest predation per month.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
            name and total values for that month.
    '''
    pass


def output_nests_per_month_graph(monthly_data):
    '''Prints a graph of the total number of nests found per month.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
            name and total values for that month.
    '''
    pass


def transform_daily_to_monthly(data):
    '''Transform the data from daily to monthly format.

    Args:
        data: a list of lists, where each sublist represents data
            for a specific day.

    Returns: a list of lists, where each sublist represents data
        for a whole month.
    '''
    pass


if __name__ == "__main__":
    all_data = read_csv_file('data/2020_2021_turtle_data.csv')
    print(all_data)
    monthly_data = transform_daily_to_monthly(all_data)

    print('2020/2021 Flatback Turtle Migration at Cemetery Beach')
    print()
    output_nests_per_month_graph(monthly_data)
    print()
    output_monthly_statistics(monthly_data)
    print()
    output_overall_statistics(monthly_data)
    print()
