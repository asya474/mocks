from unittest.mock import Mock, patch
from nose.tools import assert_list_equal, assert_true
from services import get_uncompleted_todos

@patch
def test_getting_uncompleted_todos_when_todos_is_not_none(mock_get_todos):
    todo1 = {
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }
    todo2={
        'userId': 1,
        'id': 2,
        'title': 'Walk the dog',
        'completed': True
    }
    mock_get_todos.return_value = Mock()
    mock_get_todos.return_value.json.return_value=[todo1, todo2]
    uncompleted_todos=get_uncompleted_todos()
    assert_true(mock_get_todos.called)
    assert_list_equal(uncompleted_todos, [todo1])

@patch('mock_server.get_todos')
def test_getting_uncompleted_todos_when_todos_is_none(mock_get_todos):
    mock_get_todos.return_value = None
    uncompleted_todos = get_uncompleted_todos()
    assert_true(mock_get_todos.called)
    assert_list_equal(uncompleted_todos, [])

