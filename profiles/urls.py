from django.urls import path, include
from profiles import views

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profile', views.UserProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),

    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
