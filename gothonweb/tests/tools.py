from nose.tools import *
import re


def assert_response(res, contains=None, matches=None, headers=None, status="200"):

    assert status in res.status, "Expected response %r not in %r" % (status, res.status)

    if status == "200":
        assert res.data, "Response data is empty."

    if contains:
        assert contains in res.data, "Response does not contain %r" % contains

    if matches:
        reg = re.compile(matches)
        assert reg.matches(res.data), "Response does not match %r" % matches

    if headers:
        assert_equals(res.headers, headers)
