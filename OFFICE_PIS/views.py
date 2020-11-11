from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from .models import Staff, Office,Darbandi, Post, Address, Family, Appointment,  DesiredPerson, Service, EducationalInfo, LeaveInfo, PunishmentInfo, Treatment, Document

# from .models import Question, Answer
from django.shortcuts import get_object_or_404
from django.db.models import Q
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory, InlineFormSetView

class AddressInline(InlineFormSetFactory):
	model = Address
	fields = ['country', 'province', 'district', 'municipal']
	factory_kwargs = {'can_delete': False}
	

class FamilyInline(InlineFormSetFactory):
	model = Family
	fields = '__all__'
	factory_kwargs = {'can_delete': False}
	# fields = ['country'

class AppointmentInline(InlineFormSetFactory):
	model = Appointment
	fields = '__all__'
	factory_kwargs = {'can_delete': False}

class DesiredPersonInline(InlineFormSetFactory):
	model = DesiredPerson
	fields = '__all__'
	factory_kwargs = {'can_delete': False}
	
class ServiceInline(InlineFormSetFactory):
	model = Service
	fields = '__all__'
	factory_kwargs = {'can_delete': False}


class EducationalInfoInline(InlineFormSetFactory):
	model = EducationalInfo
	fields = '__all__'
	factory_kwargs = {'can_delete': False, 'max_num': 3}

class DocumentInline(InlineFormSetFactory):
	model = Document
	fields = '__all__'
	factory_kwargs = {'can_delete': False}



class StaffCreateView(SuccessMessageMixin, CreateWithInlinesView):
	model = Staff
	inlines = [AddressInline, FamilyInline,DesiredPersonInline, AppointmentInline,  EducationalInfoInline, DocumentInline ]
	fields = ['name', 'post', 'photo', 'ph_num', 'dob', 'office' ]
	template_name = 'OFFICE_PIS/staff_form.html'

	success_url = reverse_lazy('staff-add')
	success_message = "%(name)s is added  successfully......"


class StaffUpdateView(UpdateWithInlinesView):
	model = Staff
	inlines = [AddressInline, FamilyInline,DesiredPersonInline, AppointmentInline,  EducationalInfoInline, DocumentInline ]
	fields = ['name', 'post', 'photo', 'ph_num', 'dob', 'office' ]
	template_name = 'OFFICE_PIS/staff_form.html'

	success_url = reverse_lazy('staff-list')
	success_message = "%(name)s is updated  successfully......"


	
class StaffListView(ListView):

	model = Staff
	


	





class OfficeDetailView(ListView):

	model = Office

class DarbandiCreateView(CreateView):
	model= Darbandi
	fields = '__all__'
	success_url = reverse_lazy('darbandi-view')

	

class DarbandiUpdateView(UpdateView):
	model= Darbandi
	fields = '__all__'
	success_url = reverse_lazy('darbandi-view')



# there is only one darbandi so for detail view we use Listview of darbandi
class DarbandiListView(ListView):

	model = Darbandi





class SearchResultView(ListView):
	model = Staff
	
	def get_queryset(self):
		query = self.request.GET.get('q')

		"""Q if you need to execute more complex queries
		(for example, queries with OR statements), you can use Q objects(djnago.db.models.Q)
		eg. Q ((name__icontains=query) | (post__icontains = query))
		"""
		
		object_list= Staff.objects.filter(
			Q(name__icontains = query) |
				Q(post__icontains = query)
			)
		return object_list


class PostCreateView(CreateView):
	model= Post
	fields = '__all__'
	template_name = 'OFFICE_PIS/post_form.html'

	success_url = reverse_lazy('post-add')




"""----------Staff Details View------------"""

class StaffDetailView(DetailView):
	model= Staff
	fields = '__all__'

	def get_context_data(self, **kwargs):
		context = super(StaffDetailView, self).get_context_data(**kwargs)

		context['services'] = Service.objects.filter(staff=self.kwargs.get('pk'))
		context['educations'] = EducationalInfo.objects.filter(staff=self.kwargs.get('pk'))
		context['leaveinfos'] = LeaveInfo.objects.filter(staff=self.kwargs.get('pk'))
		
		context['punishments'] = PunishmentInfo.objects.filter(staff=self.kwargs.get('pk'))
		context['treatments'] = Treatment.objects.filter(staff=self.kwargs.get('pk'))
		context['documents'] = Document.objects.filter(staff=self.kwargs.get('pk'))

		return context


class ServiceCreateView(CreateView):
	model= Service
	fields =  ['start_date', 'end_date', 'appointment_type', 'office', 'post']
	

	# to automatic select the related staff object while creating service form
	def form_valid(self, form):
		form.instance.staff_id = self.kwargs.get('pk')
		return super(ServiceCreateView, self).form_valid(form)


	# to forward to related staff detail view / return to details of related staff field
	def get_success_url(self):
		staff_id= self.kwargs['pk']
		return reverse_lazy ('staff-detail', kwargs = {'pk': staff_id})
		



class LeaveCreateView(CreateView):
	model= LeaveInfo
	fields =  ['leave_type', 'Leave_days']

	#automatic selects ta staff field
	def form_valid(self, form):
		form.instance.staff_id = self.kwargs.get('pk')
		return super(LeaveCreateView, self).form_valid(form)


	# to forward to related staff detail view / return to details of related staff field
	def get_success_url(self):
		staff_id= self.kwargs['pk']
		return reverse_lazy ('staff-detail', kwargs = {'pk': staff_id})



class PunishmentCreateView(CreateView):
	model= PunishmentInfo
	fields =  ['punishment_type', 'order_date']

	#automatic selects ta staff field
	def form_valid(self, form):
		form.instance.staff_id = self.kwargs.get('pk')
		return super(PunishmentCreateView, self).form_valid(form)


	# to forward to related staff detail view / return to details of related staff field
	def get_success_url(self):
		staff_id= self.kwargs['pk']
		return reverse_lazy ('staff-detail', kwargs = {'pk': staff_id})


class TreatmentCreateView(CreateView):
	model= Treatment
	fields =  ['amount', 'date']

	#automatic selects ta staff field
	def form_valid(self, form):
		form.instance.staff_id = self.kwargs.get('pk')
		return super(TreatmentCreateView, self).form_valid(form)


	# to forward to related staff detail view / return to details of related staff field
	def get_success_url(self):
		staff_id= self.kwargs['pk']
		return reverse_lazy ('staff-detail', kwargs = {'pk': staff_id})

		

def pdfView(request, pk):
	"""pk id bata data filter gareko, 
	for getting only one object use method :get_object_or_404(Staff, pk=pk) ,
	for getting more than one object use filter i.e. : Staff.objects.filter(per_nonper='permanent')
	"""
	
	document = get_object_or_404(Document, pk=pk)					 
	pdf_data= open (document.doc_file.path, 'rb').read()
	return HttpResponse(pdf_data, content_type='application/pdf')




















# 	model = Staff
# class AnswerInline(InlineFormSet):
# 	model = Answer
# 	fields = ['answer', 'ques']
	
# class CreateQuestionView(CreateWithInlinesView):
# 	model = Question
# 	inlines = [AnswerInline]
# 	fields = ['name', 'subject']
# 	template_name = 'OFFICE_PIS/staff_form.html'

# 	success_url = reverse_lazy('staff-list')

# class OfficeInline(InlineFormSetFactory):
# 	model = Post
# 	# fields = ['name']

# class StaffCreateView(CreateView):
# 	model= Staff, Address
# 	fields = '__all__'

	# fields = [
	# 	'name',
	# 	'position',
	# 	'post',
	# 	'address',
	# 	'per_nonper',
	# 	'ph_num',
	# 	'photo',
	# 	'document',
	# 	'dob',
	# 	# 'district_name',
	# 	# 'district_code',
	# 	# 'municipal_name',
	# 	# 'municipal_code'
	# ]

	# success_url = reverse_lazy('staff-list')




# class StaffDetailView(DetailView):

# 	model = Staff
	

# class StaffDeleteView(DeleteView):

# 		model = Staff
# 		success_url = reverse_lazy('staff-list')


# class StaffUpdateView(UpdateView):
# 	model= Staff
# 	fields = [
# 		'name',
# 		'position',
# 		'post',
# 		'address',
# 		'per_nonper',
# 		'ph_num',
# 		'photo',
# 		'document',
# 		'dob'
# 	]
# 	success_url = reverse_lazy('staff-list')






# def pdfView(request, pk):
# 	"""pk id bata data filter gareko, 
# 	for getting only one object use method :get_object_or_404(Staff, pk=pk) ,
# 	for getting more than one object use filter i.e. : Staff.objects.filter(per_nonper='permanent')
# 	"""
	
# 	staff = get_object_or_404(Staff, pk=pk)					 
# 	pdf_data= open (staff.document.path, 'rb').read()
# 	return HttpResponse(pdf_data, content_type='application/pdf')


# def permanentStaff(request):

# 	staff = Staff.objects.filter(per_nonper='permanent') #permament data filter gareko 
# 	context = {'staff_list': staff}	
# 	return render(request, 'OFFICE_PIS/permanent.html', context)

# def non_permanentStaff(request):

# 	staff = Staff.objects.filter(per_nonper='non_permanent') #non-permament data filter gareko 
# 	context = {'staff_list': staff}	
# 	return render(request, 'OFFICE_PIS/non_permanent.html', context)


# if staff.familys.all