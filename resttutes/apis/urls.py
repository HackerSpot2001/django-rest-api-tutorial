from django.urls import path,include
from .views import ProductViewSet,index
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'get',viewset=ProductViewSet)

urlpatterns = [
    # path('',include(router.urls)),
    path('hello/',view=index,name="Index")
]