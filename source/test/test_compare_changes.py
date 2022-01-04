import pytest
import pandas as pd
from source import helper_func

def test_compare_changes():
    df = pd.DataFrame()
    df['test1'] = [1,2,3,2,1,1,2,12,3,4,]
    df['test2'] = [1,1,2,2,1,1,2,12,3,2,]
    df['test3'] = [11,11,5,7,1,1,2,12,3,2,]
    df['test4'] = [1,10,3,2,1,1,2,12,3,2,]
    column_list = df.columns
    item1,item2 =  helper_func.compare_change(df)
    assert item1 == 'test1'
    assert item2 == 'test4'


def test_compare_changes2():
    df = pd.DataFrame()
    df['test1'] = [1,2,3,2,1,1,2,12,3,4,]
    df['test2'] = [1,1,2,2,1,1,2,12,3,2,]
    df['test3'] = [11,11,5,7,1,1,2,12,3,2,]
    df['test4'] = [1,10,3,2,1,1,2,12,3,2,]
    column_list = df.columns
    item1,item2 =  helper_func.compare_change(df)
    assert item2 == 'test4'
