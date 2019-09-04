from app import app
import pytest

def test_home():
    test_client = app.test_client()
    response = test_client.get('/')
    print(response.data)
    assert b'error' not in response.data