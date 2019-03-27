import pytest

from flask_todo  import create_app


@pytest.fixture
def app():
    app = create_app({
        'Testing': True,
        })

    yield app



@pytest.fixture
def client(app):
    return app.test_client()
