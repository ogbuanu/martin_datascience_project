from numpy import cov
from covid_19_cases import *
import matplotlib.pyplot as plt
import pandas as pd
from stop_and_search import *

def mainloop():
        
    covid = Covid()
    search = Search(parameter="avon-and-somerset", year='2021',month='06')
    switch = False
    user = ''
    level=1
    while switch is False:
        if level == 1:
            print(
                "well come to this application.\n"
                "press 1 to go to covid-19 main-menu \n"
                
                "press 2 to go to stop and search main-menu \n"

                "press 0 to exit."
            )
            
            user = input("")
            if user == '1':
                level = '2a'
                continue
            if user == '2':
                level = '2b'
                continue
                
            if user == '0':
                switch = True
        if level == '2a':
            print(
                "Welcome to the covid-19 main-menu. \n"

                "press 1 to plot the areas with the largest positive change of cases for a given 7 day period. \n \n"

                "Press 2 to plot the comparison of two or more areas concerning their daily change over a give ndate range \n \n"

                "Press 3 to plot the areas with the highest number of cases on a given day \n\n"

                "Press 4 to plot the total number of cases reported each day over a given date range. \n\n"

                "Press 5 to plot the total number of cases reported each week over a given date range. \n\n"

                "Press 6 to plot the total number of cases reported each month over from the start of reporting to end.\n \n"

                "Press 7 to plot the comparison of two or more areas concerning their cumulative cases tota lover a given date range.\n \n"

                "Press 8 to go back to application main-menu \n"
                "Press 0 to exit"
        
                
            )
            user = input("")
            if user == '0':
                switch=True

            if user == '8':
                level =1
            if user == '1':
                covid.plot_positive_changes()
                level = '2a'
                continue
            if user == '2':
                covid.plot_compare_changes()
                level = '2a'
                continue

            if user == '3':
                covid.plot_highest_cases()
                level = '2a'    
                continue

            if user == '4':
                covid.plot_total_daily_cases()
                level = '2a'
                continue
            
            if user =='5':
                covid.plot_total_weekly_cases()
                level = '2a'
                continue
            if user == '6':
                covid.plot_total_monthly_cases()
                level= '2a'
                continue
            
            if user == '7':
                covid.plot_cumulative_cases()
                level = '2a'
                continue
        
        if level == '2b':
            print(
                "Welcome to the stop and search main-menu \n"
                "Press 1 to plot the age-range\n"
                "Press 2 to group the stop and search data with respect to age-range column\n"
                "Press 3  to show the number of searches in a particular date using area plot \n"
                "Press 4 to plot the Search outcome buy age range\n"
                "Press 5 to Plot the gender by age range \n"
                "Press 6 to plot the ethnicity by age range\n"
                "Press 7 to plot the gender by ethnicity\n"

            )
            user = input("")
            if user == '1':
                search.get_request()
                search.get_result()
                search.plot_result()
                level = '2b'
            if user == '2':
                search.get_request()
                search.get_result()
                search.age_grouping()
                level = '2b'
            if user == '3':
                search.get_request()
                search.get_result()
                search.area_plot()
                level = '2b'
            if user == '4':
                search.get_request()
                search.get_result()
                search.outcome_by_age()
                level = '2b'
            
            if user == '5':
                search.get_request()
                search.get_result()
                search.age_by_gender()
                level = '2b'
            
            if user == '6':
                search.get_request()
                search.get_request()
                search.age_by_ethnicity()

            if user == '7':
                search.get_request()
                search.get_result()
                search.gender_by_ethnicity()

if __name__ == '__main__':
    mainloop()