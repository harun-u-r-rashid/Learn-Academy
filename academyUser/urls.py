from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()

router.register('list', views.UserViewSet)
router.register('contact/list', views.ContactView)
router.register('course/list', views.CourseView)


urlpatterns = [
    path('', include(router.urls)),

    # user
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),

    # password reset
     path("reset/",views.RequestPasswordReset.as_view(), name="request-password-reset"),
     path("password-reset/<uidb64>/<token>/", views.ResetPassword.as_view(), name="reset-password"),

    #  contact
    path('contact/', views.ContactAddView.as_view(), name='contact'),

    # Course

    path('create/', views.CourseCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.CourseUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.CourseDestroyView.as_view(), name='delete'),

]


