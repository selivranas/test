import pytest

@pytest.mark.parametrize("num, rezult",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, result):
   assert 11*num == result
    
def test_set_comparison():
    num1 = set("206")
    num2 = set("510")
    assert num1 == num2
    
def test_div_two_numbers_float():
    calc = SimpleCalc()
    result = calc.div(27, 6)
    assert result == 4.5
