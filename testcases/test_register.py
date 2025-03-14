import pytest
import time
from Pages.base import datetime
from Pages.register import loginclass
from Pages.checkin import checkinclass
from sheetutilities import sheet
@pytest.mark.usefixtures("setup")
class Test_login:
    def test_login(self):
        registerobj=loginclass(self.driver)
        checkinobj = checkinclass(self.driver)
        datetimeobject = datetime()
        sheet.selectsheet("logins")
        max_rowcount = int(sheet.rowcount())
        for i in range(2, max_rowcount + 1):
            status = sheet.readdata(f"F{i}")
            if status != "Done":
                registerobj.login()
                mobile = sheet.readdata(f"B{i}")
                password = sheet.readdata(f"C{i}")
                registerobj.login(mobile,password)
                checkinobj.checkin()
            x = datetimeobject.curentdatetime()
            li = list(x)
            sheet.writedata(i, 4, li[0])
            sheet.writedata(i, 5, li[1])
            sheet.writedata(i, 6, "Done")







