from django.core.urlresolvers import reverse
#from django.http import HttpRequest
from django.test import TestCase
from django.test.client import Client

from human_res.models import Employee, Email, Address


class TestEmployeeCreate(TestCase):
    """ """
    def test_display_new_employee_form(self):
        new_employee_form = self.client.get(reverse('human_res:employee-create'))
        self.assertEqual(new_employee_form.status_code, 200)

    def test_new_employee_form_can_save_post_request(self):
        employee = {'name_first': 'First_one', 'name_last': 'Last_one'}
        self.client.post(reverse('human_res:employee-create'), employee)
        self.assertEqual(Employee.objects.all().count(), 1)


class TestEmployeeDelete(TestCase):
    """ """
    def setUp(self):
        Employee.objects.create(name_first='First', name_last='Last')

    def test_can_remove_employee_with_comfirmation_form(self):
        self.assertEqual(Employee.objects.all().count(), 1)
        employee = Employee.objects.get(name_last='Last')
        remove_employee = self.client.post(reverse('human_res:employee-delete',
            kwargs={'pk': employee.id}))
        self.assertEqual(Employee.objects.all().count(), 0)


class EmployeeDetailTest(TestCase):
    """ """
    def setUp(self):
        Employee.objects.create(name_first='First_one', name_last='Last_one')
        Address.objects.create(address='111 One_address', city='One_city', state='TN', zip_code='12345', employee=Employee.objects.get(pk=1))
        Email.objects.create(email='one@example.com', employee=Employee.objects.get(pk=1))

    def test_display_employee_detail_page(self):
        employee = Employee.objects.get(name_last='Last_one')
        employee_detail = self.client.get(reverse('human_res:employee-detail',
            kwargs={'pk': employee.id}))
        self.assertEqual(employee_detail.status_code, 200)

    def test_employee_detail_displays_data(self):
        employee = Employee.objects.get(name_last='Last_one')
        employee_detail = self.client.get(reverse('human_res:employee-detail',
            kwargs={'pk': employee.id}))
        self.assertContains(employee_detail, 'Last_one')
        self.assertContains(employee_detail, '111 One_address')
        self.assertContains(employee_detail, 'one@example.com')


class EmployeeListTest(TestCase):
    """" """
    def test_display_human_res_personnel_page(self):
        employee_list = self.client.get(reverse('human_res:employee-list'))
        self.assertEqual(employee_list.status_code, 200)

    def test_empty_employee_list_displays_message(self):
        employee_list = self.client.get(reverse('human_res:employee-list'))
        self.assertContains(employee_list, 'No active employees')

    def test_employee_list_displays_names(self):
        Employee.objects.create(name_first='First_one', name_last='Last_one')
        employee_list = self.client.get(reverse('human_res:employee-list'))
        self.assertContains(employee_list, 'Last_one')


class EmployeeModelTest(TestCase):
    """ """
    def test_unicode(self):
        name = Employee(name_first='First', name_last='Last')
        self.assertEqual(str(name), 'Last, First')


class TestEmployeeUpdate(TestCase):
    """ """
    def setUp(self):
        Employee.objects.create(name_first='First_one', name_last='Last_one')

    def test_display_employee_edit_form(self):
        employee = Employee.objects.get(name_last='Last_one')
        edit_employee = self.client.get(reverse('human_res:employee-update',
            kwargs={'pk': employee.id}))
        self.assertEqual(edit_employee.status_code, 200)
        self.assertContains(edit_employee, "Last_one")

    def test_can_edit_employee_and_save_post_request(self):
        employee = Employee.objects.get(name_last='Last_one')
        edit_employee = self.client.post(reverse('human_res:employee-update',
            kwargs={'pk': employee.id}), {'name_first': 'Eno_tsrif', 'name_last': 'Last_one'})
        employee = Employee.objects.get(name_last='Last_one')
        self.assertEqual(employee.name_first, "Eno_tsrif")
        # check old name is gone
        employee_list = self.client.get(reverse('human_res:employee-list'))
        self.assertNotContains(employee_list, 'First_one')
