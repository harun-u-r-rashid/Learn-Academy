from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()

router.register('list', views.UserViewSet)
router.register('contact/list', views.ContactView)
router.register('course/list', views.CourseView)
router.register('module/list', views.ModuleView)


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

    path('course_create/', views.CourseCreateView.as_view(), name='course_create'),
    path('<int:pk>/course_update/', views.CourseUpdateView.as_view(), name='course_update'),
    path('<int:pk>/course_delete/', views.CourseDestroyView.as_view(), name='course_delete'),

    # Module
    path('module_create/', views.ModuleCreateView.as_view(), name='module_create'),
    path('<int:pk>/module_update/', views.ModuleUpdateView.as_view(), name='module_update'),
    path('<int:pk>/module_delete/', views.ModuleDestroyView.as_view(), name='module_delete'),

]


