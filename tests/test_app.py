from flask_todo import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hello(client):
    response = client.get('/')
    assert b'<p>This is HTML<p>' in response.data == True
