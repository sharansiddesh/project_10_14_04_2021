from django.urls import path
from app1 import views

app_name='app1'



urlpatterns = [
    path('view1/',views.view1,name="view1"),
    path('view2/',views.view2,name="view2"),
    path('view3/<data>',views.view3,name="view3"),
    path('view4/<name>',views.view4,name="view4"),
    path('view5/',views.view5,name="view5"),
    path('view6/',views.view6,name="view6"),
    path('view7/',views.view7,name="view7"),
]