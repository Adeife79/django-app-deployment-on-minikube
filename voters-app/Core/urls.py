from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('unit', UnitView.as_view()),
    path('unit/<int:pk>', UnitIDView.as_view()),
    path('ward', WardView.as_view()),
    path('ward/<int:pk>', WardIDView.as_view()),
    path('state', StateView.as_view()),
    path('state/<int:pk>', StateIDView.as_view()),
    path('VoterRegister', Voter_RegisterView.as_view()),
    path('VoterRegister/<int:pk>', Voter_RegisterIDView.as_view()),
    path('Localgovernment', Local_governmentView.as_view()),
    path('Localgovernment/<int:pk>', Local_governmentIDView.as_view()),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
