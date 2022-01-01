
def new_table(df,pd):
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
def positive_change(data_frame):
    count = 0
    new_item = ''

    for item in data_frame.pct_change().tail(7):
        if data_frame.pct_change().tail(7)[item].values.mean() > count:
            new_item = item
            count = data_frame.pct_change().tail(7)[item].values.mean()

    return new_item


def graph_sizer(plt,width,height):
    f = plt.figure()
    f.set_figwidth(width)
    f.set_figheight(height)
    return f

def clean_data(pd):
    '''pass in the dataframe: pf=dataframe and pd=pandas '''
    pf = pd.read_csv("../files/specimenDate_ageDemographic-unstacked.csv")
    df = pf.drop(columns=['areaType', 'areaCode','areaName'])
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
    newdata,specimen = new_table(df,pd)
    column_list = list(specimen)
    return s,column_list,newdata,specimen,t


def compare_change(s):
    count = 0
    new_item1 = ''
    for item in s.pct_change().tail(7):
        if s.pct_change().tail(7)[item].values.mean() > count:
            new_item1 = item
            count = s.pct_change().tail(7)[item].values.mean()
            
    count2 = 0
    new_item2 = ''
    for item in s.pct_change().tail(7):
        if s.pct_change().tail(7)[item].values.mean() < count2:
            new_item2 = item
            count2 = s.pct_change().tail(7)[item].values.mean()
    return new_item1,new_item2


def cumulative_cases(data,columnlist,):
    specimen_wnd = data.drop(columns=['new_date',]).copy()
    last_seven_cumsum = specimen_wnd.tail(7).cumsum()
    last_seven_cumsum = last_seven_cumsum[columnlist].sum()
    last_seven_cumsum.values
    count = 0
    value = 0
    for item in last_seven_cumsum.values:
        if item > value:
            value = item
        count+=1
    return count,value,last_seven_cumsum