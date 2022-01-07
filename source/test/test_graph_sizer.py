import matplotlib.pyplot as plt
from .setup_test import covid
def test_graph_ploter():
    f = covid.graph_sizer(plt,20,10)
    width = f.get_figwidth()
    height = f.get_figheight()
    assert height == 10
    assert width == 20