from django.urls import path
from . import views as v
urlpatterns = [
    path('',v.index,name="index"),
    path('register/',v.register,name='register'),
    path('login/',v.login,name='login'),
    path('login/checklogin/',v.checklogin,name="checklogin"),
    path('register/checkregister',v.checkregister,name='checkregister'),
    path('logout',v.logout,name="logout"),
    path('addrecord/',v.addrecord,name="addrecord"),
    path('addrecord/checkentry/',v.checkentry,name="checkentry"),
    path('update/<int:id>',v.update,name="update"),
    path('delete/<int:id>',v.delete,name="delete"),
    path('update/updaterecord/<int:id>',v.updaterecord,name="updaterecord"),
]
