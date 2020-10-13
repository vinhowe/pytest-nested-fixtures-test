import pytest
from random import random

s_env = None

@pytest.fixture(scope="module")
def boss_env(request):
    global s_env

    if s_env is None:
        s_env = random()

    saved_s_env = s_env

    print(s_env)

    yield s_env

    s_env = None

    raise Exception(f"cleaning up {saved_s_env}")


@pytest.fixture
def env(request, boss_env):
    yield boss_env + 5

