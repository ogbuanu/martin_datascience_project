import pandas as pd
import matplotlib.pyplot as plt





class Covid:

    def get_csv(self):
        self.csv = "../files/specimenDate_ageDemographic-unstacked.csv"
        self.pf = pd.read_csv(self.csv)
    
    
    def clean_data(self,pd):
        '''pass in the dataframe: pf=dataframe and pd=pandas 
        This is a custom function for this project.
        it cleans and process the dataframe, making it ready to work with.
        '''
        self.get_csv()
        df = self.pf.drop(columns=['areaType', 'areaCode','areaName'])
        df['new_date'] = pd.to_datetime(df['date'])

        t = df.drop(columns=['date',]).copy()


        df['newCasesBySpecimenDateByPctchange-0_4'] = df['newCasesBySpecimenDate-0_4'].pct_change()
        df['newCasesBySpecimenDateByPctchange-0_59'] = df['newCasesBySpecimenDate-0_59'].pct_change()
        df['newCasesBySpecimenDateByPctchange-10_14'] = df['newCasesBySpecimenDate-10_14'].pct_change()
        df['newCasesBySpecimenDateByPctchange-15_19'] = df['newCasesBySpecimenDate-15_19'].pct_change()
        df['newCasesBySpecimenDateByPctchange-20_24'] = df['newCasesBySpecimenDate-20_24'].pct_change()
        df['newCasesBySpecimenDateByPctchange-25_29'] = df['newCasesBySpecimenDate-25_29'].pct_change()
        df['newCasesBySpecimenDateByPctchange-30_34'] = df['newCasesBySpecimenDate-30_34'].pct_change()
        df['newCasesBySpecimenDateByPctchange-35_39'] = df['newCasesBySpecimenDate-35_39'].pct_change()
        df['newCasesBySpecimenDateByPctchange-40_44'] = df['newCasesBySpecimenDate-40_44'].pct_change()
        df['newCasesBySpecimenDateByPctchange-45_49'] = df['newCasesBySpecimenDate-45_49'].pct_change()
        df['newCasesBySpecimenDateByPctchange-50_54'] = df['newCasesBySpecimenDate-50_54'].pct_change()
        df['newCasesBySpecimenDateByPctchange-55_59'] = df['newCasesBySpecimenDate-55_59'].pct_change()
        df['newCasesBySpecimenDateByPctchange-5_9'] = df['newCasesBySpecimenDate-5_9'].pct_change()
        df['newCasesBySpecimenDateByPctchange-60_64'] = df['newCasesBySpecimenDate-60_64'].pct_change()
        df['newCasesBySpecimenDateByPctchange-65_69'] = df['newCasesBySpecimenDate-65_69'].pct_change()
        df['newCasesBySpecimenDateByPctchange-70_74'] = df['newCasesBySpecimenDate-70_74'].pct_change()
        df['newCasesBySpecimenDateByPctchange-75_79'] = df['newCasesBySpecimenDate-75_79'].pct_change()
        df['newCasesBySpecimenDateByPctchange-60+'] = df['newCasesBySpecimenDate-60+'].pct_change()
        df['newCasesBySpecimenDateByPctchange-80_84'] = df['newCasesBySpecimenDate-80_84'].pct_change()
        df['newCasesBySpecimenDateByPctchange-85_89'] = df['newCasesBySpecimenDate-85_89'].pct_change()
        df['newCasesBySpecimenDateByPctchange-90+'] = df['newCasesBySpecimenDate-90+'].pct_change()
        tcolumn = list(t)
        tcolumn.remove('new_date')
        t['total_cases'] = t[tcolumn].sum(axis=1)

        s = df.drop(columns=['date','new_date']).copy()
        newdata,specimen = self.new_table(df,pd)
        column_list = list(specimen)
        return s,column_list,newdata,specimen,t

    def graph_sizer(self,plt,width,height):
        """
        plt: matplotlib,
        width: width of the graph,
        height: Height of the graph,
        graph_sizer(plt,width,height)
        This function resizes the graph.
        """
        f = plt.figure()
        f.set_figwidth(width)
        f.set_figheight(height)
        return f

    def new_table(self,df,pd):
        """
        df: dataframe,
        pd: pandas,
        new_table(df,pd): process the data and creates multiple new tables 
        This function creates new columns that show the percentage change of
    infection rates between each day for each area.

            """
        newdata = pd.DataFrame()
        newdata['newCasesBySpecimenDate-0_4'] = df['newCasesBySpecimenDate-0_4']
        newdata['newCasesBySpecimenDate-0_59'] = df['newCasesBySpecimenDate-0_59']
        newdata['newCasesBySpecimenDate-10_14'] = df['newCasesBySpecimenDate-10_14']
        newdata['newCasesBySpecimenDate-15_19'] = df['newCasesBySpecimenDate-15_19']
        newdata['newCasesBySpecimenDate-20_24'] = df['newCasesBySpecimenDate-20_24']
        newdata['newCasesBySpecimenDate-25_29'] = df['newCasesBySpecimenDate-25_29']
        newdata['newCasesBySpecimenDate-30_34'] = df['newCasesBySpecimenDate-30_34']
        newdata['newCasesBySpecimenDate-35_39'] = df['newCasesBySpecimenDate-35_39']
        newdata['newCasesBySpecimenDate-40_44'] = df['newCasesBySpecimenDate-40_44']
        newdata['newCasesBySpecimenDate-45_49'] = df['newCasesBySpecimenDate-45_49']
        newdata['newCasesBySpecimenDate-50_54'] = df['newCasesBySpecimenDate-50_54']
        newdata['newCasesBySpecimenDate-55_59'] = df['newCasesBySpecimenDate-55_59']
        newdata['newCasesBySpecimenDate-5_9'] = df['newCasesBySpecimenDate-5_9']
        newdata['newCasesBySpecimenDate-60_64'] = df['newCasesBySpecimenDate-60_64']
        newdata['newCasesBySpecimenDate-65_69'] = df['newCasesBySpecimenDate-65_69']
        newdata['newCasesBySpecimenDate-70_74'] = df['newCasesBySpecimenDate-70_74']
        newdata['newCasesBySpecimenDate-75_79'] = df['newCasesBySpecimenDate-75_79']
        newdata['newCasesBySpecimenDate-60+'] = df['newCasesBySpecimenDate-60+']
        newdata['newCasesBySpecimenDate-80_84'] = df['newCasesBySpecimenDate-80_84']
        newdata['newCasesBySpecimenDate-85_89'] = df['newCasesBySpecimenDate-85_89']
        newdata['newCasesBySpecimenDate-90+'] = df['newCasesBySpecimenDate-90+']

        specimen = newdata.copy()


        newdata['newCasesBySpecimenDateByPctchange-0_4'] = df['newCasesBySpecimenDateByPctchange-0_4'] = df['newCasesBySpecimenDate-0_4'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-0_59'] = df['newCasesBySpecimenDateByPctchange-0_59'] = df['newCasesBySpecimenDate-0_59'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-10_4'] = df['newCasesBySpecimenDateByPctchange-10_14'] = df['newCasesBySpecimenDate-10_14'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-15_19'] = df['newCasesBySpecimenDateByPctchange-15_19'] = df['newCasesBySpecimenDate-15_19'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-20_24'] = df['newCasesBySpecimenDateByPctchange-20_24'] = df['newCasesBySpecimenDate-20_24'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-25_29'] = df['newCasesBySpecimenDateByPctchange-25_29'] = df['newCasesBySpecimenDate-25_29'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-30_34'] = df['newCasesBySpecimenDateByPctchange-30_34'] = df['newCasesBySpecimenDate-30_34'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-35_39'] = df['newCasesBySpecimenDateByPctchange-35_39'] = df['newCasesBySpecimenDate-35_39'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-40_44'] = df['newCasesBySpecimenDateByPctchange-40_44'] = df['newCasesBySpecimenDate-40_44'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-45_49'] = df['newCasesBySpecimenDateByPctchange-45_49'] = df['newCasesBySpecimenDate-45_49'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-50_54'] = df['newCasesBySpecimenDateByPctchange-50_54'] = df['newCasesBySpecimenDate-50_54'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-55_59'] = df['newCasesBySpecimenDateByPctchange-55_59'] = df['newCasesBySpecimenDate-55_59'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-5_9'] = df['newCasesBySpecimenDateByPctchange-5_9'] = df['newCasesBySpecimenDate-5_9'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-60_64'] = df['newCasesBySpecimenDateByPctchange-60_64'] = df['newCasesBySpecimenDate-60_64'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-65_69'] = df['newCasesBySpecimenDateByPctchange-65_69'] = df['newCasesBySpecimenDate-65_69'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-70_74'] = df['newCasesBySpecimenDateByPctchange-70_74'] = df['newCasesBySpecimenDate-70_74'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-75_79'] = df['newCasesBySpecimenDateByPctchange-75_79'] = df['newCasesBySpecimenDate-75_79'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-60+'] = df['newCasesBySpecimenDateByPctchange-60+'] = df['newCasesBySpecimenDate-60+'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-80_84'] = df['newCasesBySpecimenDateByPctchange-80_84'] = df['newCasesBySpecimenDate-80_84'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-85_89'] = df['newCasesBySpecimenDateByPctchange-85_89'] = df['newCasesBySpecimenDate-85_89'].pct_change()
        newdata['newCasesBySpecimenDateByPctchange-90+'] = df['newCasesBySpecimenDateByPctchange-90+'] = df['newCasesBySpecimenDate-90+'].pct_change()
        return newdata,specimen

    
    def positive_change(self,data_frame):
        """data_frame: Dataframe
            positive_change(data_frame)
            This function returns The column of a dataframe that has the highest positive change.
        """
        count = 0
        new_item = ''

        for item in data_frame.pct_change().tail(7):
            if data_frame.pct_change().tail(7)[item].values.mean() > count:
                new_item = item
                count = data_frame.pct_change().tail(7)[item].values.mean()

        return new_item

        
    def compare_change(self,s):
        """
        s: dataframe
        compare_changes(s):
        This function takes in a dataframe and returns two item
        item1 = item with the highest positive change by percentage
        item2 = item with the lowest positive change by percentage
        """
        count = 0
        new_item1 = ''
        for item in s.pct_change().tail(7):
            if s.pct_change().tail(7)[item].values.mean() > count:
                new_item1 = item
                count = s.pct_change().tail(7)[item].values.mean()
                
        count2 = 0
        new_item2 = ''
        for item in s.pct_change().tail(7):
            if s.pct_change().tail(7)[item].values.mean() < count:
                new_item2 = item
                count2 = s.pct_change().tail(7)[item].values.mean()
        return new_item1,new_item2

    def cumulative_cases(self,data,columnlist,):
        """
        data: pandas Dataframe
        columnlist: list of column in the dataframe.
        cumulative_cases(data,columnlist):\
            
        """
        if 'new_date' in data.columns:
            
            specimen_wnd = data.drop(columns=['new_date',]).copy()
        else:
            specimen_wnd = data.copy()
        last_seven_cumsum = specimen_wnd.tail(7).cumsum()
        last_seven_cumsum = last_seven_cumsum[columnlist].sum()
        # last_seven_cumsum.values
        count = 0
        value = 0
        for item in last_seven_cumsum.values:
            if item > value:
                value = item
            count+=1
        return value, last_seven_cumsum

    def plot_positive_changes(self):
        """
         section 1:  Areas with the largest positive change of cases for a given 7 day period. """

        s,column_list,newdata,specimen,t = self.clean_data(pd)
        item = self.positive_change(specimen)
        self.graph_sizer(plt,20,10)
        plt.plot(s.pct_change().tail(7)[item])
        plt.show()

    def plot_compare_changes(self):
        '''
    section 2: • Comparison of two or more areas concerning their daily change over a given
    date range

    '''
        s,column_list,newdata,specimen,t = self.clean_data(pd)

        item1,item2 = self.compare_change(newdata)
        self.graph_sizer(plt,20,10)
        plt.subplot(2, 1, 1)
        plt.plot(s.pct_change().tail(7)[item1])

        plt.subplot(2, 1, 2)
        plt.plot(s.pct_change().tail(7)[item2])
        plt.show()

    def plot_highest_cases(self):
        """
        section 3: Shows the areas with the highest number of cases on a given day
        """
        s,column_list,newdata,specimen,t = self.clean_data(pd)

        highest = specimen.idxmax(axis=1)
        self.graph_sizer(plt,20,10)
        plt.plot(self.pf.date.head(1), highest[:1])
        plt.show()

    def plot_total_daily_cases(self):
        """
        section 4: Total number of cases reported each day over a given date range.
        """
        s,column_list,newdata,specimen,t = self.clean_data(pd)

        specimen['total_cases'] = specimen[column_list].sum(axis=1)
        self.graph_sizer(plt,20,10)

        specimen.total_cases[:7].plot()
        plt.show()

    def plot_total_weekly_cases(self):
        """section5:  Total number of cases reported each week over a given date range."""
        s,column_list,newdata,specimen,t = self.clean_data(pd)
        specimen['new_date'] = t['new_date']
        specimen['total_cases'] = specimen[column_list].sum(axis=1)

        weekly_cases = specimen.resample('W',on='new_date').sum()
        self.graph_sizer(plt,20,10)
        weekly_cases.total_cases[:5].plot(kind='bar')
        plt.show()
    def plot_total_monthly_cases(self):
        """section 6: Total number of cases reported each month over from the start of reporting
        to end.
        """
        s,column_list,newdata,specimen,t = self.clean_data(pd)
        specimen['new_date'] = t['new_date']
        specimen['total_cases'] = specimen[column_list].sum(axis=1)


        monthly_cases = specimen.resample('M',on='new_date').sum()
        self.graph_sizer(plt,20,10)
        monthly_cases.total_cases.plot(kind='bar')
        plt.show()

    def plot_cumulative_cases(self):
        """ section 7: Comparison of two or more areas concerning their cumulative cases total
        over a given date range.
        """
        s,column_list,newdata,specimen,t = self.clean_data(pd)

        value,data_cumsum = self.cumulative_cases(specimen,column_list)
        self.graph_sizer(plt,20,10)
        data_cumsum.plot(kind='bar')
        plt.show()




