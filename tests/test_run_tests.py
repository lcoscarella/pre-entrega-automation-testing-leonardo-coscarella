from def_tests import login
import pytest
from utils import vars

### python -m pytest -v
@pytest.mark.logueo
def test_login():
    assert login(vars.userLogin,vars.pwdLogin) == True

