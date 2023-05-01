from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import mail_admins

def index(request):

    all_roles = Roles.objects.all()
    context = {
        'all_roles':all_roles,
    }   
    return render(request, 'index.html', context)


def about(request):
    all_personal_info = Personal_Info.objects.all()
    all_facts_info = Facts_Info.objects.all()
    all_skills_info = Skills_Info.objects.all()
    about_me_info = About_Me.objects.all()

    personal_info_dtls1 = {obj.info_name : obj.info_value for obj in all_personal_info[0:4] }
    personal_info_dtls2 = {obj.info_name : obj.info_value for obj in all_personal_info[4:8] }
    all_facts_dtls = {obj.facts_name : (obj.facts_value,obj.facts_description) for obj in all_facts_info}
    
    context = {
        'personal_info_dtls1' : personal_info_dtls1,
        'personal_info_dtls2' : personal_info_dtls2,
        'all_facts_dtls' : all_facts_dtls,
        'all_skills_info' : all_skills_info,
        'about_me_info' : about_me_info,

    }
    return render(request, 'about.html', context)

def resume(request):
    all_edu_info = Education_Info.objects.order_by('id') #use -id to sort in descending order
    resume_summary_info = Resume_Summary.objects.all()
    project_dtls_info = Project_Details.objects.order_by('-id')
    project_desc_info = create_work_desc_dict(project_dtls_info)
    
    context = {
        'all_edu_info': all_edu_info,
        'resume_summary_info' : resume_summary_info,
        'project_dtls_info' : project_dtls_info,
        'project_desc_info' : project_desc_info,
    }

    return render(request, 'resume.html', context)

def create_work_desc_dict(work_exp_obj):
    work_desc_dict = {}
    
    for project_item in work_exp_obj:
        work_desc_list = [project_desc.description for project_desc in Project_Details.objects.get(project_name=project_item.project_name).project_desc_set.all()]
        work_desc_dict.update({project_item.project_name:work_desc_list})
    
    return work_desc_dict

def contact(request):
    if request.method == "POST":
        
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent Successfully!")
        return redirect('contact')
        # form = ContactForm(request.POST or None)
        # if form.is_valid():
        #     name = form.cleaned_data['name']
        #     sender = form.cleaned_data['email']
        #     subject = "You have a new Feedback from {}:{}".format(name, sender)
        #     message = "Subject: {}\n\nMessage: {}".format(form.cleaned_data['subject'], form.cleaned_data['message'])
        #     mail_admins(subject, message)
        #     form.save()
        #     messages.success(request, "Message sent Successfully!")
        # return redirect('contact')

    else:
        my_contact_info = My_Contact_Details.objects.all()
        context = {
            'my_contact_info' : {obj.contact_info : obj.contact_value for obj in My_Contact_Details.objects.all()},
        }
        
        return render(request, 'contact.html', context)