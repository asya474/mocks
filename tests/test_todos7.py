from unittest import skipIf
from constants import SKIP_REAL
from nose.tools import  assert_list_equal

@skipIf(SKIP_REAL, "Skipping tests that hit the real API server")
def test_integration_contract():
    actual = get_todos()
    actual_keys = actual.json().pop().keys()

    with patch('services.requests.get') as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = [{
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }]

        mocked = get_todos()
        mocked_keys = mocked.json().pop().keys()

    assert_list_equal(list(actual_keys), list(mocked_keys))