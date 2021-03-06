from wtforms import PasswordField

from apps.auth import models
from apps.auth.utils import ModelViewSecurity


class UserAdmin(ModelViewSecurity):
    form_columns = (
        'username', 'password', 'email',
        'first_name', 'last_name', 'is_active',
        'is_admin',
    )
    column_list = (
        'username', 'email', 'first_name',
        'last_name', 'is_active', 'date_join',
        'is_admin',
    )

    def scaffold_form(self):
        form_class = super(UserAdmin, self).scaffold_form()
        form_class.password = PasswordField()
        return form_class


def add_to_admin(app, admin):
    admin.add_view(UserAdmin(models.User, app.db.session))
