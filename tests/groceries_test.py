
from app.groceries import calculate_avg_price

def test_calculate_avg_price():
    list0 = [0,0,0,0]
    list1 = [1,2,3,4]
    list2 = [6, 12, 18]
    assert calculate_avg_price(list0) == 0
    assert calculate_avg_price(list1) == 2.5
    assert calculate_avg_price(list2) == 12

