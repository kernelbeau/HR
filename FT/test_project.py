from unittest import skip

from selenium.webdriver.common.keys import Keys

from FT.helpers import MyTestCase

#@skip
class DjangoAdminTests(MyTestCase):
    """ """
    def test_admin_site_login_app_links_and_logout(self):
        # go to admin site
        self.driver.get('%s%s'% (self.live_server_url, '/admin/'))
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('My Project', body.text)
        # log in
        username_field = self.driver.find_element_by_name('username')
        username_field.send_keys("kb")
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys("kb")
        password_field.send_keys(Keys.RETURN)
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)
        # find admin links to current apps
        content = self.driver.find_element_by_id('content-main')
        self.assertIn('Human_Res', content.text)
        self.assertIn('Employee', content.text)
        # log out
        self.driver.find_element_by_link_text('Log out').click()
        self.assertEqual(self.driver.current_url, self.live_server_url + '/admin/logout/')

#@skip
class DjangoProjectTests(MyTestCase):
    """ """
    def test_django_project_index_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('My Company', body.text)

    def test_visit_human_res_home_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        # click link to human_res
        self.driver.find_element_by_link_text('Human Resources').click()
        self.driver.find_element_by_link_text("What's New").click()
        self.assertEqual(self.driver.current_url, self.live_server_url + '/hr/')
        # view human_res home page
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Human Resource news...', body.text)

    def test_visit_human_res_personnel_page(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        # click link to personnel
        self.driver.find_element_by_link_text('Human Resources').click()
        self.driver.find_element_by_link_text("Personnel").click()
        self.assertEqual(self.driver.current_url, self.live_server_url + '/hr/employee/')
        # view human_res personnel page
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Current employees...', body.text)
