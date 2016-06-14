from app import db, admin
from apps.main import models
from apps.utils import ModelViewSecurity

admin.add_view(ModelViewSecurity(models.User, db.session))
