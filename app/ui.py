import six
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from m3_ext.ui.fields import ExtDictSelectField

from objectpack.ui import BaseEditWindow, TabbedEditWindow, ObjectTab
from m3_ext.ui import all_components as ext
from . import actions


class UserAddWindow(BaseEditWindow):

    def _init_components(self, *args, **kwargs):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserAddWindow, self)._init_components(*args, **kwargs)

        self.field__password = ext.ExtStringField(
            label=u'Password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__lastlogin = ext.ExtStringField(
            label=u'last login',
            name='last login',
            anchor='100%')

        self.field__superuserstatus = ext.ExtCheckBox(
            label=u'superuser status',
            name='superuser status',
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__firstname = ext.ExtStringField(
            label=u'first name',
            name='first name',
            anchor='100%')

        self.field__lastname = ext.ExtStringField(
            label=u'last name',
            name='lastname',
            anchor='100%',
            data=ContentType)

        self.field__emailaddress = ext.ExtStringField(
            label=u'email address',
            name='email address',
            anchor='100%')

        self.field__staffstatus = ext.ExtCheckBox(
            label=u'staff status',
            name='staff status',
            anchor='100%')

        self.field__active = ext.ExtCheckBox(
            label=u'active',
            name='active',
            anchor='100%')

        self.field__datajoined = ext.ExtDateField(
            label=u'data joined',
            name='data joined',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__lastlogin,
            self.field__superuserstatus,
            self.field__username,
            self.field__firstname,
            self.field__lastname,
            self.field__emailaddress,
            self.field__staffstatus,
            self.field__active,
            self.field__datajoined
        ))

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class PermissionTab(ObjectTab.fabricate(
    model=Permission, field_list=('name', 'content_type', 'codename',))):

    def init_components(self, *args, **kwargs):
        super(PermissionTab, self).init_components(*args, **kwargs)

        self._content_type_field = ExtDictSelectField(
            label='Content Type')
        self._controls.append(self._content_type_field)

    def set_params(self, *args, **kwargs):
        super(PermissionTab, self).set_params(*args, **kwargs)

        self._content_type_field.pack = actions.ContentTypePak
        self._content_type_field.display_field = (
            '__unicode__' if six.PY2 else '__str__'
        )


class PermissionEditWindow(TabbedEditWindow):
    tabs = [
        PermissionTab,

    ]
