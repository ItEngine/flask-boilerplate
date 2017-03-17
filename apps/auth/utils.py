from flask_admin.contrib.sqla import ModelView
import flask_login as login


class ModelViewSecurity(ModelView):
    """
    ModelView admin login required
    """
    def is_accessible(self):
        return login.current_user.is_authenticated
