import calendar

if __name__ == '__main__':
    print('Input year:')
    year = int(input())
    print('Year', year, 'is a leap year' if calendar.isleap(year) is True else 'is low-altitude')
