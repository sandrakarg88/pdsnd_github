import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Nice to see you. Let\'s explore some US bikeshare data!')

    #set filter_criteria standard to all
    month = 'all'
    day = 'all'

    # To get user input for city (chicago, new york city, washington).
    while True:
        try:
            city = str(input('\nWould you like to see data for Chicago, New York or Washington?\n').lower())
            if city == 'washington' or city == 'chicago' or city == 'new york':
                if city == 'new york':
                    city = 'new york city'
                break
            else:
                print('\nYou\'re input is not valid. Please close the program if you want to stop.\n')
        except:
            print('\ninvalid value\n')

    print('\n{} is your choosen filter.\n'.format(city.title()))

    # To get user input for filter criteria month, day or no filter.
    while True:
        try:
            filter_criteria = str(input('Would you like to filter the data by month (type: month), day (type: day), both (type: both) or not at all (type: all)?\n').lower())
            if filter_criteria == 'month' or filter_criteria == 'day' or filter_criteria == 'both' or filter_criteria == 'all':
                break
            else:
                print('\n You\'re input is not valid. Please close the program if you want to stop.\n')
        except:
            print('\ninvalid value\n')

    print('\n{} is your choosen filter.\n'.format(filter_criteria).title())

    # to get user input for month + day of the week
    if filter_criteria == 'both':
        # To get user input for month (all, january, february, ... , june)
        while True:
            try:
                month = str(input('Which month do you like to filter. Please type: January, February, March, April, Mai, June or all?\n').lower())
                if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':
                    break
                else:
                    print('\nYou\'re input is not valid. Please close the program if you want to stop.\n')
            except:
                print('\nThat\'s not a valid number!\n')

        print('\n{} is your choosen filter.\n'.format(month.title()))

        # To get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            try:
                day = str(input('\nWhich day? Please type \'monday\', \'tuesday\', \'wednesday\', \'thursday\', \'friday\', \'saturday\' or \'sunday\'. If you don\'t want to filter at all please type \'all\'.\n').lower())
                if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all':
                    break
                else:
                    print('\nYou\'re input is not valid. Please close the program if you want to stop.\n')
            except:
                print('\nThat\'s not a valid value!\n')

        print('\n{} is your choosen filter.\n'.format(day.title()))

    # To get user input for month (all, january, february, ... , june)
    if filter_criteria == 'month':
        while True:
            try:
                month = str(input('Which month do you like to filter. Please type: January, February, March, April, Mai, June or all?\n').lower())
                if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':
                    break
                else:
                    print('\nYou\'re input is not valid. Please close the program if you want to stop.\n')
            except:
                print('\nThat\'s not a valid number!\n')

        print('\n{} is your choosen filter.\n'.format(month.title()))

    # To get user input for day of week (all, monday, tuesday, ... sunday)
    if filter_criteria == 'day':
        while True:
            try:
                day = str(input('\nWhich day? Please type \'monday\', \'tuesday\', \'wednesday\', \'thursday\', \'friday\', \'saturday\' or \'sunday\'. If you don\'t want to filter at all please type \'all\'.\n').lower())
                if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all':
                    break
                else:
                    print('\nYou\'re input is not valid. Please close the program if you want to stop.\n')
            except:
                print('\nThat\'s not a valid value!\n')

        print('\n{} is your choosen filter.\n'.format(day.title()))

    print('You\'re chosen filters are: \ncity = {} \nmonth = {} \nday = {}'.format(city, month, day))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from Start Time to create new month column
    df['month'] = df['Start Time'].dt.month
    # extract day of week from Start Time column to create new day column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
               main()
