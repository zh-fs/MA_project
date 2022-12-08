from allmodule.basepage import BasePage
from allmodule.common_module.old_form_one.old_form_ele import *


class Old_Edit(BasePage):
    def save_form(self):
        self.locator_with_wait(*save_form).click()
