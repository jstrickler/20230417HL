import pytest
from subjectlib import Spam
import hamlib

HAM_VALUE = 42

def test_spam_calls_ham(mocker):
    mocker.patch('hamlib.ham', return_value=HAM_VALUE * 10)
    s = Spam(HAM_VALUE)  # Create instance of Spam, which calls ham()
    assert s.value == HAM_VALUE * 10

if __name__ == '__main__':
    pytest.main([__file__, '-s'])   # Start the test runner
