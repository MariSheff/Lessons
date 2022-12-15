import pytest

def inc(x):
    return x + 1

@pytest.mark.skip(reason = 'no time to test') #пропускаем тест
def test_answer1():
    assert inc(3) == 5

@pytest.mark.xfail #(reason = 'known parser issue')
def test_answer2():
    assert inc(3) == 7

@pytest.mark.xfail
def test_answer2():
    assert inc(3) == 4

# def test_true():
#     assert True
#
# def test_false():
#     assert False