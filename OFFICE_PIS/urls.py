from django.conf.urls import url,include
from django.urls import  path
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

# views as auth_views
# app_name = 'office_pis'


urlpatterns =[

	path(r'staff/', views.StaffCreateView.as_view(), name ='staff-add'),
	path(r'staff/update/<pk>', views.StaffUpdateView.as_view(), name ='staff-update'), 
	path(r'darbandi/view', views.DarbandiListView.as_view(), name ='darbandi-view'), 

	path(r'staff', views.StaffListView.as_view(), name ='staff-list'),
	path(r'post/create', views.PostCreateView.as_view(), name ='post-add'),
	path(r'service/<pk>/create', views.ServiceCreateView.as_view(), name ='service-add'),
	path(r'leave/<pk>/create', views.LeaveCreateView.as_view(), name ='leave-add'),
	path(r'punishment/<pk>/create', views.PunishmentCreateView.as_view(), name ='punishment-add'),
	path(r'treatment/<pk>/create', views.TreatmentCreateView.as_view(), name ='treatment-add'),
	
	path(r'staff/<pk>', views.StaffDetailView.as_view(), name ='staff-detail'),
	path(r'darbandi/create', views.DarbandiCreateView.as_view(), name ='darbandi-add'),
	path(r'darbandi/update/<pk>', views.DarbandiUpdateView.as_view(), name ='darbandi-update'),

	path(r'staff/document/<pk>', views.pdfView, name ='staff-document-view'),
	path(r'staff/search/', views.SearchResultView.as_view(), name ='search-results'),


	# #user authentication
	
	path ('login/', auth_views.LoginView.as_view(),  name = 'login' ),
    path (r'pis', auth_views.LogoutView.as_view(), {'next_page' : '/'}, name = 'logout' ), 	
    path ('', TemplateView.as_view (template_name = 'home.html'), name ='home'),	
    

	# # yesma url matching garda staff ra delete rakheni hunxa narakhe ni hunxa
	# url(r'^del/(?P<pk>\d+)$', views.StaffDeleteView.as_view(), name ='staff-del'),
	
	
	# url(r'^staff/permanent$', views.permanentStaff, name ='staff-permanent'),
	# url(r'^staff/non-permanent$', views.non_permanentStaff, name ='staff-non-permanent'),
	

	
]