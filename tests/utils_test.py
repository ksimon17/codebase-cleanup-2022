
from app.utils import to_usd

def test_to_usd():
    
    # if large number, should use thousands separator:  
    assert to_usd(123456789.98) == "$123,456,789.98"
    
    # it rounds to two decimal places (and have a dollar sign):
    assert to_usd(0.45555) == "$0.46"