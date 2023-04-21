import pytest  # Needed for test runner
import re  # Needed for test (but will be mocked)
from subjectlib import SpamSearch   # subject under test


def test_spam_search_calls_re_search(mocker):   # Unit test
    mocker.patch('re.search')  # Patch re.search (i.e., replace re.search with a Mock object that records calls to it)
    s = SpamSearch('bug', 'lightning bug')  # Create instance of SpamSearch
    _ = s.findit()   # Call the method under test
    re.search.assert_called_once_with('bug', 'lightning bug')  # Check that method was called just once with the expected parameters

if __name__ == '__main__':
    pytest.main([__file__, '-s'])   # Start the test runner
