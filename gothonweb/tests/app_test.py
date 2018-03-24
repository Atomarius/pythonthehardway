from bin.app import app
from tests.tools import assert_response


def test_index():
    res = app.request("/")
    assert_response(res, status="303")
