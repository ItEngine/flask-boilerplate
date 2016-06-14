from flask_admin.contrib.sqla import ModelView

from app import db, admin
from apps.main import models


admin.add_view(ModelView(models.User, db.session))
