from unittest.mock import Mock, patch
from nose.tools import assert_is_not_none, assert_list_equal
from services import get_todos

@patch('services.requests.get')
def test_getting_todos_when_response_is_ok(mock_get):
    todos = [{
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }]
    mock_get.return_value=Mock(ok=True)
    mock_get.return_value.json.return_value=todos
    response=get_todos()
    assert_list_equal(response.json(), todos)

@patch('services.requests.get')
def test_getting_todos_when_response_is_not_ok(mock_get):
    mock_get.return_value.ok=False
    response=get_todos()
    assert_is_not_none(response)
