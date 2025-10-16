import json
from web.app import app

def test_root():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert b"Hello" in r.data

def test_plus_one():
    client = app.test_client()
    r = client.get("/plus_one?x=5")
    data = json.loads(r.data.decode())
    assert data["x"] == 6

def test_plus_two():
    client = app.test_client()
    r = client.get("/plus_two?x=3")
    data = json.loads(r.data.decode())
    assert data["x"] == 5

def test_square():
    client = app.test_client()
    r = client.get("/square?x=4")
    data = json.loads(r.data.decode())
    assert data["x"] == 16

