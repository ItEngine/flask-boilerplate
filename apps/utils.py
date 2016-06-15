from flask import redirect, render_template, request, url_for
from flask_admin.contrib.sqla import ModelView
from flask_admin import expose, helpers
from flask_admin.base import AdminIndexView
import flask_login as login

from apps.main.forms import LoginForm


class ModelViewSecurity(ModelView):
    """
    ModelView admin login required
    """
    def is_accessible(self):
        return login.current_user.is_authenticated


# Create customized index view class that handles login & registration
class MyAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)

        if request.method == 'POST':
            if helpers.validate_form_on_submit(form) and form.validate_login():
                user = form.get_user()
                login.login_user(user)
                return redirect(url_for('admin.index'))

        self._template_args['form'] = form
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))
