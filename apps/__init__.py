from flask import render_template
from flask_admin import Admin


def create_admin(app):
    from apps.auth.admin import add_to_admin
    from apps.auth.controllers import MyAdminIndexView

    admin = Admin(
        app, name='Admin', index_view=MyAdminIndexView(),
        template_mode='bootstrap3', base_template='admin_master.html',
    )

    add_to_admin(app, admin)
    return admin


def create_errorhandler(app):
    # HTTP error handling
    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    # HTTP error handling
    @app.errorhandler(500)
    def not_found(error):
        return render_template('500.html'), 500
