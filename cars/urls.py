from django.urls import path
from . import views

urlpatterns = [
    path('branch/', views.branch),
    # path('postfilter/', views.customfilter),
    path('branch/<int:pk>', views.branchDetail),
]