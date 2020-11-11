from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, UpdateView

from xamine.models import Patient, Order, Invoice

from .forms import RegisterForm, PatientModelForm


# Create your views here.
def patient_home_view(request):
    """ get patient user and patient user oder set """
    p_user=Patient.objects.get(patient_user=request.user)
    p_orders=Order.objects.filter(patient=p_user)

    # Set up empty context to pass to template
    context = {}

    """ upcoming appointments """
    upcoming_orders = Order.objects.filter(level_id=1, appointment__isnull=False).order_by('appointment')

    """ orders """
    complete_orders = p_orders.filter(level_id=4).order_by('completed_time')
    active_orders = p_orders.filter(level_id__lt=4)

    # context['active_orders'] = active_orders
    context['complete_orders'] = complete_orders
    context['upcoming_orders'] = upcoming_orders

    return render(request, "patient_home_template.html", context)
    
class PatientDetailView(DetailView):
    template_name = 'patient_detail.html'
    queryset = Patient.objects.all()

    def get_object(self):
        id_ = Patient.objects.get(patient_user=self.request.user).id
        return get_object_or_404(Patient, id=id_)

class PatientUpdateView(UpdateView):
    template_name = 'patient_update.html'
    form_class = PatientModelForm
    success_url = '/patient_portal/detail'

    def get_object(self):
        id_ = Patient.objects.get(patient_user=self.request.user).id
        return get_object_or_404(Patient, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

def patient_insurance_view(request):
    return render(request, "insurance_template.html", {})

def patient_visits_view(request):
    return render(request, "visits_template.html", {})

def patient_billing_view(request):

    context = {}
    """
    p_user=Patient.objects.get(patient_user=request.user)
    P_invoice=Invoice.objects.filter(patient=p_user)
    print('P_invoice = ', Invoice.objects.filter(patient=p_user))

    current_invoices = P_invoice.filter(isPaid=False).order_by('order_id')
    print('current invoices = ', P_invoice.filter(isPaid=False).order_by('order_id'))
    context['invoices'] = current_invoices
    """
    return render(request, "billing_template.html", context)

def cancel_order(request, order_id):
    try:
        cur_order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        raise Http404

    context = {}
    context['this_order'] = cur_order

    if request.method == 'POST':
	    cur_order.delete()
	    return redirect('/..')

    return render(request, 'cancel_order.html', context)

#Register User as Patient
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)

        # extra validation to check email across xamine.models.Patient
        if form.is_valid():
            user = form.save()
            user_group = Group.objects.get(name='Patient')     
            user.groups.add(user_group)

            # find associated email in xamine.models.Patient and add user to Patient model
            xamine_patient = Patient.objects.get(email_info=response.POST.get('email'))
            xamine_patient.patient_user = user
            xamine_patient.save(update_fields=['patient_user'])

            # TODO remove
            # get the patient user name from xamine Patient model
            user.first_name = xamine_patient.first_name
            user.last_name = xamine_patient.last_name
            user.save(update_fields=['first_name', 'last_name'])

            return HttpResponseRedirect("/login/?next=/")
    else:
        form = RegisterForm()    

    return render(response, "register/register.html", {'form':form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })