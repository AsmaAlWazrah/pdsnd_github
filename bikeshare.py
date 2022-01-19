
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA =[ 'all', 'january', 'february','march','april','may','june']
DAY_DATA =[ 'all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
#update first bikeshare message
    print('Hello there! Let\'s explore some US bikeshare data!')
    
    while True:
        try:
            city= str(input('Enter a city (chicago, new york city, washington):')).lower()
            if city in CITY_DATA.keys():
                break
            else:
                print('choose from specified list') 
        except (ValueError, KeyboardInterrupt):
            print('INVALID') 

    while True:
        try:
            month= str(input('Enter a month (all, january, february, .., june):')).lower()
            if month in MONTH_DATA:
                break
            else:
                print('choose from specified list') 
        except (ValueError, KeyboardInterrupt):
            print('INVALID') 
    while True:
        try:
            day= str(input('Enter a day (all, monday, tuesday, ... sunday):')).lower()
            if day in DAY_DATA:
                break
            else:
                print('choose from specified list') 
        except (ValueError, KeyboardInterrupt):
            print('INVALID') 

    return city, month, day   


def load_data(city, month, day):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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

    view_data = str(input("Would you like to view 5 rows of individual trip data? Enter yes or no?")).lower()
    start_loc = 0
    
    while (view_data=='yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = str(input("Do you wish to continue?: ")).lower()
        if view_display=='yes':
            continue
        elif view_display=='no':
            break
        
        
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mcm= df['month'].mode()
    print('The most common month:', mcm.values)
    # TO DO: display the most common day of week
    mcd= df['day_of_week'].mode()
    print('The most common day of week:', mcd.values)

    # TO DO: display the most common start hour
    mch= (df['Start Time'].dt.hour).mode()
    print('The most common start hour:', mch.values)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mcss= df['Start Station'].mode()
    print('The most common start station:', mcss.values)

    # TO DO: display most commonly used end station
    mces= df['End Station'].mode()
    print('The most common end station:', mces.values)

    # TO DO: display most frequent combination of start station and end station trip
    mcses= df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most common start and end station:', mcses)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    ttt= df['Trip Duration'].sum()
    print('The total travel time:', ttt)
    

    # TO DO: display mean travel time

    mtt= df['Trip Duration'].mean()
    print('The mean travel time:', mtt)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    ut= df['User Type'].value_counts()
    print('User type counts:', ut)
    
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gen= df['Gender'].value_counts()
        print('Gender counts:', gen)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('Earliest year of birth:', df['Birth Year'].min().astype(int))
        print('Most recent year of birth:', df['Birth Year'].max().astype(int))
        print('Most common year of birth:', df['Birth Year'].mode().astype(int).values)   
    else:
        print('This dataset does not include birth year')
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print('you choose city {} month {} day {}'.format(city, month, day))

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

