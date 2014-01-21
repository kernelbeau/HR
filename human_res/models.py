from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from localflavor.us.models import USStateField


class Employee(models.Model):
    """ """
    name_first = models.CharField(_('first name'), max_length=24)
    name_last = models.CharField(_('last name'), max_length=24)

    class Meta:
        db_table = 'employee'
        ordering = ['name_last', 'name_first']
        verbose_name = _('employee')
        verbose_name_plural = _('employee')

    def __unicode__(self):
        return u'%s, %s'% (self.name_last, self.name_first)

    def get_absolute_url(self):
        return reverse('human_res:employee-detail', kwargs={'pk': self.pk,})


class Address(models.Model):
    """ """
    address = models.CharField(_('address'), max_length=72)
    TYPE = (('Alternate', 'Alternate'), ('Mailing', 'Mailing'), ('Physical', 'Physical'),)
    address_type = models.CharField(_('address type'), max_length=10, choices=TYPE)
    city = models.CharField(_('city'), max_length=36)
    employee = models.ForeignKey(Employee)
    state = USStateField(_('state'),)
    zip_code = models.CharField(_('zip code'), max_length=10)

    class Meta:
        db_table = 'employee_address'
        unique_together = ('employee', 'address_type')
        verbose_name_plural = _('Address')

    def __unicode__(self):
        return u'%s, %s, %s  %s'% (self.address, self.city, self.state, self.zip_code)


class Email(models.Model):
    """ """
    email = models.EmailField(_('email address'), max_length=64)
    employee = models.ForeignKey(Employee)


    class Meta:
        db_table = 'employee_email'
        verbose_name_plural = _('Email')

    def __unicode__(self):
        return u'%s'% (self.email)


#class Phone(models.Model):
