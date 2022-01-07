import pytest
import pandas as pd
from .setup_test import covid
def test_cumulative():
    df = pd.DataFrame()
    df['test1'] = [1,2,3,2,1,1,2,12,3,4,]
    df['test2'] = [1,1,2,2,1,1,2,12,3,2,]
    df['test3'] = [11,11,5,7,1,1,2,12,3,2,]
    df['test4'] = [1,10,3,2,1,1,2,12,3,2,]
    column_list = df.columns
    value,data_cumsum =  covid.cumulative_cases(df,column_list)
    assert value == 112

