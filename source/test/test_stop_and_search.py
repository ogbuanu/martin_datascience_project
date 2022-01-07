import pandas as pd
from .setup_test import search_df
search_df.get_request()
search_df.get_request()
def test_stop_and_search_request():
    assert search_df.get_request() == 200

def test_stop_and_search_result():
    assert type(search_df.result_df) is  pd.DataFrame