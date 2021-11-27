"""
Requirement : (file handling)
-------------
-->write a program to fetch the data using http get and point out number of holidays in england and wales, then group them based on the year. read the data from this link : https://www.gov.uk/bank-holidays.json
"""

# solution:
# ---------
import requests
from datetime import datetime

data = requests.get("https://www.gov.uk/bank-holidays.json")
main_dict = (data.json())
countries_list = [i for i in main_dict.keys()]
# print(countries_list)

dict1 = {}

dict1 = main_dict['england-and-wales']
# print(dict1)


# seperate events data, this data2 contains the list of dictionary.
list_data2 = dict1['events']
# print(list_data2[0]['date'])
# print(list_data2)


date_dict2 = {}
# create dictionary by making date at key
for i in range(len(list_data2)):
    date_dict2[list_data2[i]['date']] = list_data2[i]
# print(date_dict2)


# sorting the date
def func(n):
    return datetime.strptime(n, '%Y-%m-%d').date()


dates_list = sorted(date_dict2.keys(), key=func)
# print(dates_list)


# separate only year from date and use sets to avoid duplicates
dates_set = set()
for i in dates_list:
    dates_set.add(i[0: 4])
    # print(dates_set)

# sort the years in ascending order
years_list = sorted(list(dates_set))
# print(years_list)


# create a dictionary with year as key and year count as value
count_dict = {}

for year in years_list:
    count = 0
    for key in date_dict2:
        if key.startswith(year):
            count += 1
            count_dict[year] = count

    # print(count_dict)

# display the final output
print('\n========================', countries_list[0], ' Holidays data by year', '============================\n')
for year in years_list:
    print('\n------------------------In ', year, ' ', countries_list[0], ' has', count_dict[year],
          ' holidays------------------------ \n')
    for date in date_dict2:
        if date.startswith(year):
            print(date, date_dict2[date])

# full solution: this returns the all the holidays year wise for all the countries.
# ---------------
import requests
from datetime import datetime

data = requests.get("https://www.gov.uk/bank-holidays.json")
main_dict = data.json()

countries_list = [i for i in main_dict.keys()]
# print(countries_list)

for country in countries_list:
    # seperate england-and-wales data

    dict1 = main_dict[country]
    # print(dict1)

    # seperate events data, this data2 contains the list of dictionary.
    list_data2 = dict1['events']
    # print(list_data2[0]['date'])
    # print(list_data2)

    date_dict2 = {}
    # create dictionary by making date at key
    for i in range(len(list_data2)):
        date_dict2[list_data2[i]['date']] = list_data2[i]
    # print(date_dict2)

    # sorting the date
    def func(n):
        return datetime.strptime(n, '%Y-%m-%d').date()

    dates_list = sorted(date_dict2.keys(), key=func)
    # print(dates_list)

    # separate only year from date and use sets to avoid duplicates
    dates_set = set()
    for i in dates_list:
        dates_set.add(i[0: 4])
    # print(dates_set)

    # sort the years in ascending order
    years_list = sorted(list(dates_set))
    # print(years_list)

    # create a dictionary with year as key and year count as value
    count_dict = {}

    for year in years_list:
        count = 0
        for key in date_dict2:
            if key.startswith(year):
                count += 1
                count_dict[year] = count
    #
    print(count_dict)

    # display the final output
    print('\n========================', country, ' Holidays data by year', '============================\n')
    for year in years_list:
        print('\n------------------------In ', year, ' ', country, ' has', count_dict[year],
              ' holidays------------------------ \n')
        for date in date_dict2:
            if date.startswith(year):
                print(date, date_dict2[date])