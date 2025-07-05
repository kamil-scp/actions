# test_my_script.py

import pytest
from unittest.mock import patch
import my_script

# Przykładowe dane do testów
fake_data = [
    {
        "name": "John Doe",
        "address": {"city": "New York"}
    },
    {
        "name": "Jane Smith",
        "address": {"city": "Los Angeles"}
    }
]

def test_process_users():
    df = my_script.process_users(fake_data)
    assert list(df.columns) == ['name', 'city']
    assert df.loc[0, 'name'] == 'John Doe'
    assert df.loc[0, 'city'] == 'New York'
    assert df.loc[1, 'name'] == 'Jane Smith'
    assert df.loc[1, 'city'] == 'Los Angeles'

@patch('my_script.requests.get')
def test_fetch_users(mock_kamil):
    mock_kamil.return_value.status_code = 200
    mock_kamil.return_value.json.return_value = fake_data
    data = my_script.fetch_users()
    assert data == fake_data
    mock_kamil.assert_called_once_with('https://jsonplaceholder.typicode.com/users')

print("x")