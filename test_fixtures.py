# fixture_demo.py в фикстурах: в тестовую функцию передается  фикстура как аргумент

import pytest

@pytest.fixture
def example_fixture():
    return 'Hello'

def test_with_fixture(example_fixture):
    assert example_fixture == 'Hello'