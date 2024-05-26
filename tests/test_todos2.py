from unittest.mock import patch
from nose.tools import assert_is_not_none
from services import get_todos

def test_getting_todos():
    with patch('services.requests.get') as mock_get:
        mock_get.return_value.ok=True
        response=get_todos()
    assert_is_not_none(response)
    #Используйте менеджер контекста, когда часть кода в тестовой функции использует мок,
    # а другая часть кода ссылается на настоящую функцию.