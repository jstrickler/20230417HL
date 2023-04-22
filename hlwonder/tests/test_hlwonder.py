import pytest
from hlwonder import Hlwonder, sample_function

@pytest.fixture
def Hlwonder_object():
    obj = Hlwonder()
    return obj

def test_Hlwonder_instance_has_sample_method(Hlwonder_object):
    assert hasattr(Hlwonder_object, "sample_method")

def test_hlwonder_has_sample_function():
    assert sample_function() is None  # no return value
