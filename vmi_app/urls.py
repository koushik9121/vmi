from django.urls import path

from . import views


urlpatterns=[
	path('',views.index,name='index'),
	path('shop/',views.shop,name='shop'),
	path('contact/',views.contact,name='contact'),
	path('login_register/',views.login_register,name='login_register'),
	path('blog_details/',views.blog_details,name='blog_details'),
	path('single_portfolio/',views.single_portfolio,name='single_portfolio'),
	#path('vmi/',views.vmi,name='vmi')
	
]