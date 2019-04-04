import pytest
from cars.fleet import Fleet

@pytest.fixture(scope="module")
def build_fleet():
    return Fleet(queue_id='test')
