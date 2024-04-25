import pytest

pytest_plugins = [
    "core.tests.fixtures",
]


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):  # noqa
    pass
