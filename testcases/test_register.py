import pytest
import time
from Pages.base import datetime
from Pages.register import loginclass
from Pages.checkin import checkinclass
from sheetutilities import sheet

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login(self):
        register_obj = loginclass(self.driver)
        checkin_obj = checkinclass(self.driver)
        datetime_obj = datetime()

        # Select the "logins" sheet
        sheet.selectsheet("Sheet1")
        max_row_count = int(sheet.rowcount())

        for i in range(6, max_row_count + 1):
            try:
                status = sheet.readdata(f"F{i}")

                if status != "Done":  # Process only if status is not "Done"
                    mobile = sheet.readdata(f"B{i}")
                    password = sheet.readdata(f"C{i}")

                    print(f"Attempting login for user: {mobile}")

                    register_obj.login(mobile, password)
                    checkin_obj.checkin()

                    # Fetch current date & time
                    current_date, current_time = datetime_obj.curentdatetime()

                    # Write back results
                    sheet.writedata(i, 4, current_date)
                    sheet.writedata(i, 5, current_time)
                    sheet.writedata(i, 6, "Done")

                    print(f"Login & check-in completed for user: {mobile}")
                else:
                    print(f"Skipping row {i}, already processed.")

            except Exception as e:
                print(f"Error processing row {i}: {e}")

