from unittest.mock import Mock,patch
from nose.tools import assert_is_none, assert_list_equal, assert_true
from services import get_todos, get_uncompleted_todos

class TestTodos(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher=patch('services.requests.get')
        cls.mock_get=cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_getting_todos_when_response_is_ok(self):
        self.mock_get.return_value.ok=True
        todos=[{
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }]

        self.mock_get.return_value=Mock()
        self.mock_get.return_value.json.return_value=todos

        response=get_todos()

        assert_list_equal(response.json(),todos)

    def test_getting_todos_when_response_is_not_ok(self):
        self.mock_get.return_value.ok=False
        response=get_todos()

        assert_is_none(response)

class TestUncompletedTodos(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_todos_patcher=patch('services.get_todos')
        cls.mock_get_todos=cls.mock_get_todos_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_todos_patcher.stop()

    def test_getting_uncompleted_todos_when_todos_is_not_none(self):
        todo1 = {
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }
        todo2 = {
            'userId': 2,
            'id': 2,
            'title': 'Walk the dog',
            'completed': True
        }
        self.mock_get_todos.return_value = Mock()
        self.mock_get_todos.return_value.json.return_value = [todo1, todo2]
        uncompleted_todos = get_uncompleted_todos()

        assert_true(self.mock_get_todos.called)
        assert_list_equal(uncompleted_todos, [todo1])

    def test_getting_uncompleted_todos_when_todos_is_none(self):
        self.mock_get_todos.return_value = None
        uncompleted_todos = get_uncompleted_todos()

        assert_true(self.mock_get_todos.called)
        assert_list_equal(uncompleted_todos, [])

    def test_integration_contract(self):
        # Вызов службы, чтобы обратиться к реальному API.
        actual = get_todos()
        actual_keys = actual.json().pop().keys()

        # Вызов службы, чтобы вызвать подменный API.
        with patch('project.services.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = [{
                'userId': 1,
                'id': 1,
                'title': 'Make the bed',
                'completed': False
            }]

            mocked = get_todos()
            mocked_keys = mocked.json().pop().keys()

        # Объект из реального API и объект из подменного API должны иметь
        # одинаковую структуру данных.
        assert_list_equal(list(actual_keys), list(mocked_keys))