from unittest import skip

from FT.helpers import MyTestCase

#@skip
class HumanResourceWebPageTests(MyTestCase):
    """ """
    def visit_human_res_employee_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        self.driver.find_element_by_link_text("Human Resources").click()
        self.driver.find_element_by_link_text("Personnel").click()

    def test_display_index_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        self.driver.find_element_by_link_text("Human Resources").click()
        self.driver.find_element_by_link_text("What's New").click()
        self.assertEqual(self.driver.current_url, self.live_server_url + '/hr/')
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Human Resource news', body.text)

    def test_display_employee_list(self):
        self.visit_human_res_employee_page()
        self.assertEqual(self.driver.current_url, self.live_server_url + '/hr/employee/')
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Current employees', body.text)

    def test_employee_list_detail_page(self):
        self.visit_human_res_employee_page()
        self.driver.find_element_by_xpath("(//a[contains(text(),'View')])[3]").click()
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Employee detail', body.text)

    def test_display_employee_update_form(self):
        self.visit_human_res_employee_page()
        self.driver.find_element_by_xpath("(//a[contains(text(),'Edit')])[3]").click()
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Update employee', body.text)

    def test_display_create_new_employee_form(self):
        self.visit_human_res_employee_page()
        self.driver.find_element_by_link_text("Add New Employee").click()
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Add a new employee', body.text)

    def test_delete_employee_form(self):
        self.visit_human_res_employee_page()
        self.driver.find_element_by_link_text("Edit").click()
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Are you sure ', body.text)
