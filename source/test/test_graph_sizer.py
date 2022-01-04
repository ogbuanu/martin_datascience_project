import matplotlib.pyplot as plt
from source import helper_func

def test_graph_ploter():
    f = helper_func.graph_sizer(plt,20,10)
    width = f.get_figwidth()
    height = f.get_figheight()
    assert height == 10
    assert width == 20