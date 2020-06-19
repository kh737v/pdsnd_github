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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=''
    month=''
    day=''
    city_list = ['chicago', 'new york city', 'washington']
    while city.lower() not in city_list:
        city = input("Enter a city: ")   
        if city.lower() not in city_list:
            print('Sorry, Invalid city name. Please enter a city of Chicago, New York, or Washington.')

    # TO DO: get user input for month (all, january, february, ... , june)
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    while month.lower() not in months_dict.keys():            
        month = input("Enter a month: ")   
        if month.lower() not in months_dict.keys():
            print('Sorry, Invalid month name. Please enter a month between January and June') 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']      
    while day.lower() not in day_list:            
        day = input("Enter a weekday: ")   
        if day.lower() not in day_list:
            print('Sorry, Invalid weekday name. Please enter a weekday name')  

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
    #print(df.head())
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    #print(df['Start Time'].head())

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #print(df['month'].head())
    #print(df['day_of_week'].head())
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #print((months[month]))
        #print(month)
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        #print(df['month'].head())

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        #print(day.title())
        #print(df.head())

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = df['month'].mode()[0]
    index = int(df['Start Time'].dt.month.mode())
    index = df['Start Time'].dt.month.mode()[0]
    most_pop_month = months[index - 1]
    print('The most popular month is {} or {}.'.format(index, most_pop_month))

    # TO DO: display the most common day of week
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    index = int(df['Start Time'].dt.dayofweek.mode())
    index = df['Start Time'].dt.dayofweek.mode()[0]
    most_pop_day = days_of_week[index]
    print('The most popular day of week for start time is {} or {}.'.format(index+1, most_pop_day))

    # TO DO: display the most common start hour
    most_pop_hour = int(df['Start Time'].dt.hour.mode())
    most_pop_hour = df['Start Time'].dt.hour.mode()[0]
    if most_pop_hour == 0:
        am_pm = 'am'
        pop_hour_readable = 12
    elif 1 <= most_pop_hour < 13:
        am_pm = 'am'
        pop_hour_readable = most_pop_hour
    elif 13 <= most_pop_hour < 24:
        am_pm = 'pm'
        pop_hour_readable = most_pop_hour - 12
    print('The most popular hour of day for start time is {} or {}{}.'.format(most_pop_hour, pop_hour_readable, am_pm))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode().to_string(index = False)

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode().to_string(index = False)

    # TO DO: display most frequent combination of start station and end station trip
    print('The most commonly used start station is {}.'.format(most_common_start))
    print('The most commonly used end station is {}.'.format(most_common_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_time = df['Trip Duration'].sum()
    print('total trip time is {}.'.format(total_trip_time))

    # TO DO: display mean travel time
    mean_trip_time = df['Trip Duration'].mean()
    print('mean trip time is {}.'.format(mean_trip_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_type = df["User Type"].value_counts()
        #print(type(user_type))
        print('There are {} Subscribers and {} Customers.'.format(user_type['Subscriber'], user_type['Customer']))
    else:
        print('User Type is not in the data!')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_type = df["Gender"].value_counts()
        print('There are {} male users and {} female users.'.format(gender_type['Male'], gender_type['Female']))
    else:
        print('Gendar is not in the data!')

    # TO DO: Display earliest, most recent, and most common year of birth
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode())
        print('The earliest year of birth in {}.\n'
              'The most recent year of birth in {}.\n'
              'The most common year of birth in {}.'.format(earliest, most_recent, most_common))
    else:
        print('Birth Year is not in the data!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    '''
    Descriptive statistics are correctly computed and used to answer the questions posed about the data. 
    Raw data is displayed upon request by the user in this manner: Script should prompt the user 
    if they want to see 5 lines of raw data, display that data if the answer is 'yes', 
    and continue these prompts and displays until the user says 'no'.    
    '''       
    firstline = 0
    lastline  = 5
    valid_input = True
    while valid_input:
        select = input('Would you like to view trip data? Type yes or no: ')
        if select in ['yes', 'no']:
            break
        else:
            print('Invlid input, Please enter yes or no')
    if select.lower() == 'yes':
        # prints 5 lines of the trip data 
        print(df.iloc[:,0:].iloc[firstline:lastline])
        
        select_more = ''
        while select_more.lower() != 'no':
            valid_input_more = False
            while valid_input_more == False:
                select_more = input('Would you like to view more trip data? Type yes or no: ')
                if select_more in ['yes', 'no']:
                    break
                else:
                    print('Invalid input, Please enter yes or no')
            if select_more.lower() == 'yes':
                firstline += 5
                lastline += 5
                # prints another 5 lines of the trip data
                print(df.iloc[:,0:].iloc[firstline:lastline])
            elif select_more.lower() == 'no':
                break
def first_commit():
    print('This is the first change for step 4. Refactor Code')

def second_commit():
    print('This is the second change for step 4. Refactor Code')

def third_commit():
    print('This is the third change for step 4. Refactor code')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
