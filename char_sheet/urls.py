from django.urls import path

from . import views

app_name = 'char_sheet'
urlpatterns = [
	# ex: /char_sheet/
	path('', views.index, name='index'),
	# ex: /char_sheet/3/
	path('<int:player_id>/', views.detail, name='detail'),
	#path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# ex: /char_sheet/3/2/
	path('<int:player_id>/character', views.char_detail, name='char_detail')

]