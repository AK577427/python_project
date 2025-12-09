import csv
# import pandas as pd
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C" #u - Unicode string literal, does nothing in python3 but is necessary in python 2


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
   
    dt_iso_string = datetime.fromisoformat(iso_string)
    formatted_date = dt_iso_string.strftime ("%A %d %B %Y") #.replace(" 0"," ")

    return formatted_date


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    float_temp_in_fahrenheit = float(temp_in_fahrenheit)

    temp = (5/9*(float_temp_in_fahrenheit-32))
    temp_in_degree = round(temp,1)

    return temp_in_degree


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum = 0
    count = 0
    for i in weather_data:
        i = float(i)
        sum = sum + i
        count+=1
    mean = sum/count
    return mean


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    list_of_lists = []

    with open(csv_file,encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            # if not any(cell.strip() for cell in row):
            if not row:
                continue
            processed_row=[]
            for item in row:
                try:
                    processed_row.append(int(item))
                except ValueError:
                    try:
                        processed_row.append(float(item))
                    except ValueError:
                        processed_row.append(item)
            list_of_lists.append(processed_row)
    return list_of_lists

    #using pandas
    # df = pd.read_excel(csv_file)
    # df_empty_rows = df.dropna(how=all)
    # list_of_lists = df.values.tolist()
    # return list_of_lists


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    else:
        min_value = min(weather_data)
        value_index = 0
        min_value_index = 0
        for value in weather_data:
            if(value == min_value):
                value_index = min_value_index
            min_value_index=min_value_index + 1
        return float(min_value) , value_index


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    else:
        max_value = max(weather_data)
        value_index = 0
        min_value_index = 0
        for value in weather_data:
            if(value == max_value):
                value_index = min_value_index
            min_value_index=min_value_index + 1
        return (float(max_value) , value_index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
