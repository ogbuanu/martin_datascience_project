#Eniola Rahman Olamide
#Teesside University ICA 12/2020

#Import the libraries needed.
import requests
import pandas as pd
import json
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import datetime

#Create the Class police
class Police():

    #Set the police class constructor
    def __init__ (self,):
        self.id = id
        self.police_url = "https://data.police.uk/api/forces"
        self.police_request = None
    #A function that checks if the request is Ok and returns a value if the condition is true
    def get_status(self,):
         self.police_request = requests.get(self.police_url)
         if (self.police_request.status_code == 200):
             return "Stop and Search data Visualization "

    #A function that returns the police force.
    def get_police(self,):
        self.police_id = []
        if self.police_request.status_code == requests.codes.ok:
            the_request = self.police_request.json()
            for i in the_request:
                police_id = i["id"]
                self.police_id.append(police_id)
        return(self.police_id)

#Create the Class Search that contains the stop and search dataset
class Search():
    parameter = ""

    #Define the Constructor with three parameters
    def __init__(self, parameter, year, month):
        self.parameter = parameter
        self.year = year
        self.month = month
        self.url = "https://data.police.uk/api/stops-force"
        self.request = None
        self.result_df = pd.DataFrame()

    #Create a get_request function that returns the request code    
    def get_request(self,):
        self.request = requests.get(self.url + "?force=" + self.parameter + "&date=" + self.year + "-" + self.month)
        #print(self.request.status_code)
        print(self.request.status_code)
        return self.request.status_code

    #Create a get request function that returns the request as Pandas data frame
    def get_result(self,):
        if self.request.status_code == requests.codes.ok:
            result = self.request.json()
            self.result_df = pd.DataFrame(result)
        return self.result_df

    #A function that plots the age-range 
    def plot_result(self,):
        self.get_result()
        fig1, ax1 = plt.subplots(1,2,figsize=(18,8))
        self.result_df['age_range'].value_counts().plot.pie(autopct='%1.1f%%',ax=ax1[0],shadow=True)
        ax1[0].set_title('The Age Range of the people stoped by ' +self.parameter +" police force in " + self.month + " - " +self.year)
        ax1[0].set_ylabel('Count')
        self.result_df['age_range'].value_counts().plot(kind = "bar")
        plt.show()
    
    #A function that group the stop and search data with respect to age-range column
    def age_grouping(self,):
        age_group = self.result_df["age_range"].value_counts()
        age_df = pd.DataFrame(age_group.items(), columns=["Age Group", "Total"])
        age_df
        headerColor = 'grey'
        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'
        fig = go.Figure(data=[go.Table(header=dict(
        values=['<b>Age _Group</b>','<b>Total</b>'],
        line_color='darkslategray',
        fill_color=headerColor,
        align=['left','center'],
        font=dict(color='white', size=12)),
        cells=dict(values=[
        age_df["Age Group"], age_df["Total"]],
        line_color='darkslategray',
        # 2-D list of colors for alternating rows
        fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*len(age_df)],
        align = ['left', 'center'],
        font = dict(color = 'darkslategray', size = 11)))])
        fig.update_layout(title='Police stop by area',)
        fig.show()
    
    #Compare the number of searches for two different data points
    def comparison_of_searches(self, df1, df2, police1, month1, year1, police2, month2, year2):
        first_number = df1.size
        second_number = df2.size
        if (second_number == first_number):
                print("The number of stop and search are equal, More likely the Options are the same")
        elif (second_number > first_number):
                print("The number of stop and search at " + police1+ " in " + month1 +" " +year1+\
                     " in contrast to the one for  " +police2+ "Police force in" +year2+ " " +month2+ " has increased")
        elif (second_number < first_number):
                print("The number of stop and search at " +police2+ "For" +month2+ "has not increased")
        print("difference :", self.result_df.size)
    
    """A function to plot the number of stop and seach for two different forces. 
    Note: The size of the data signifies the number of entries which implies the number of distict stop and search
    """
    def compare_searches(self, df1, df2, police1, police2, month1, month2, year1, year2):
        
        first_df = df1
        first_size = first_df.size
    
        second_df = df2
        second_size = second_df.size
        y = [first_size, second_size]
        mylabels = ['Number of people stoped by ' +police1+\
            " police in " + month1 + " - " +year1, 'The Age Range of the people stoped by ' +police2 +\
            " police in " + month2 + " - " +year2, ]

        plt.pie(y, labels = mylabels)
    
        plt.show()
      
        print(self.result_df.size)

    #A function using Area plot to show the number of searches in a particular date
    def area_plot(self,):
        df = self.result_df
        df["datetime"] = pd.to_datetime(df["datetime"]).dt.date
        df = df["datetime"].value_counts()
        df = pd.DataFrame(df.items(), columns=["datetime", "count"])
        fig=px.area(x=df["datetime"],y=df["count"])
        fig.update_layout(title='Count of the number of people stoped by ' +self.parameter +\
            " police force in " + self.month + " - " +self.year,
                  xaxis_title="Date",yaxis_title="Count",)
        fig.show()

    #Plot the Search outcome buy age range
    def outcome_by_age(self,):
        df = self.result_df
        ct = pd.crosstab(df['age_range'], df['outcome'])
        ct.plot.bar(stacked=True)
        plt.legend(title='mark')
        plt.show()
    #Plot the gender by age range
    def age_by_gender(self,):
        df = self.result_df
        ct = pd.crosstab(df['age_range'], df['gender'])
        ct.plot.bar(stacked=True)
        plt.legend(title='mark')
        plt.show()
    #Plot the ethnicity by age range
    def age_by_ethnicity(self,):
        df = self.result_df
        ct = pd.crosstab(df['self_defined_ethnicity'], df['age_range'])
        ct.plot.bar(stacked=True)
        plt.legend(title='mark')
        plt.show()  
    #Plot the gender by ethnicity
    def gender_by_ethnicity(self,):
        df = self.result_df
        ct = pd.crosstab(df['self_defined_ethnicity'], df['gender'])
        #ct = ct.drop(['All'], axis=1)
        ct.plot.bar(stacked=True)
        plt.legend(title='mark')
        plt.show()     
    def other_functions(self):
        pass #Add this function later

   


    
    
