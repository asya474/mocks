from unittest.mock import patch
from nose.tools import assert_is_not_none
from services import get_todos
def test_getting_todos():
    mock_get_patcher=patch('services.requests.get')
    mock_get=mock_get_patcher.start()
    mock_get.return_value.ok=True
    response=get_todos()
    assert_is_not_none(response)
    mock_get_patcher.stop()
    mock_get.return_value.ok=True
    response=get_todos()
    mock_get_patcher.stop()
    assert_is_not_none(response)
    #Используйте патчер в тех случаях, когда нужно явно запустить и остановить мокинг функции
    # в нескольких тестах (например, функции setUp() и tearDown() в тестовом классе).
