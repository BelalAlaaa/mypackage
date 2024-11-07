from mypackage import mymodule

def test_top_n():
    """
    make sure that top_n returns the correct top n elements

    """
    assert mymodule.top_n([8,3,2,7,4],3) == [8,7,4], 'incorrect'
    assert mymodule.top_n([12,3,10,7,4],3) == [12,10,7], 'incorrect'
    assert mymodule.top_n([5,3,2,2,4],2) == [5,4], 'incorrect'