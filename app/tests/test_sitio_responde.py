# Executes all functions with text prefix.
import pytest  # noqa: module-not-used
import requests


# All functions with test_ prefix will run in testing.
def test_site_localhost():
    # assert verifies if the test was successful or not.
    port = 5050
    assert 200 == requests.get(f"http://localhost:{port}", timeout=1).status_code
