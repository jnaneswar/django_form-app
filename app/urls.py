from django.urls import path
from . import views










urlpatterns = [
    
    path('', views.HomePageView.as_view(),name="home"),
    path('create',views.ContactCreateView.as_view(),name="submit"),
    path('success',views.ContactSuccessView.as_view(),name="success"),
    path('retrieval',views.ContactRetrievalView.as_view(),name="retrieval"),

]



