import pytest
from Pages.register import applyloanclass

@pytest.mark.usefixtures("setup")
class Test_login:
    def test_login(self):
        registerobj=applyloanclass(self.driver)
        registerobj.applyloan()


