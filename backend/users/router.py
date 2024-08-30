from rest_framework import routers

from .viewsets import UserView

app_name ="users"

router = routers.DefaultRouter()
router.register('users',UserView)
