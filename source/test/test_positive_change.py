from .setup_test import covid
import pandas as pd


def test_compare_changes():
    df = pd.DataFrame()
    df['test1'] = [1,2,3,2,1,1,2,12,3,4,]
    df['test2'] = [1,1,2,2,1,1,2,12,3,2,]
    df['test3'] = [11,11,5,7,1,1,2,12,3,2,]
    df['test4'] = [1,10,3,2,1,1,2,12,3,2,]
    column_list = df.columns
    item =  covid.positive_change(df)
    assert item == 'test1'
  


