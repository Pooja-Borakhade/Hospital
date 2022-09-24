
from HSPTL.models import *
from django.shortcuts import redirect, render, HttpResponse

# Create your views here.


def homepage(request):
   
    if request.method=='POST':
      
        id = request.POST.get('Hid')
        Name = request.POST.get('H_Name')
        Phone_num = request.POST.get('H_Phone_num')
        esta_year = request.POST.get('H_esta_year')    
        if not id:

            a = Hospital( Name=Name, Phone_num=Phone_num, esta_year=esta_year)
            a.save()
            return redirect("get_data")
        else :
            b = Hospital.objects.get(id = id)
            b.Name = Name
            b.Phone_num = Phone_num
            b.esta_year = esta_year
            b.save()
            return redirect("get_data")    
        
            
    else:
        return render(request, "home1.html")


def get_data(request):
    data = Hospital.objects.all()
    # print(data)
    return render(request,'get_data.html',{'data':data}) 

def edit_data(request,pk):
    obj = Hospital.objects.get(id = pk)
    return render(request,'home1.html',{'ob1':obj})
# --------------------------------------------------------------------------------------------------------------------#

def get_owner(request):
    O_data1 = Owner.objects.all()
    return render(request,'get_owner.html',{'O_data': O_data1})

# ----------------------------------------------------------------------------------------------------------------------#
def homepage1(request):
   
    if request.method=='POST':

        id = request.POST.get('Dept_id')
        Name = request.POST.get('Dept_Name')
        Total_staff = request.POST.get('Dept_total_staff')
        hospi_id = request.POST.get('Dept_Hospi_id')
          
        if not id:

            a = Department( Name=Name, Total_Staff=Total_staff, hospi_id=hospi_id)         
            a.save()
            return redirect("get_dept")
        else :
            b = Department.objects.get(id = id)
            b.Name = Name
            b.Total_Staff = Total_staff
            b.hospi_id = hospi_id
           
            b.save()
            return redirect("get_dept")    
        
            
    else:
        return render(request, "dept.html")
    



def get_dept(request):
    D_data1 = Department.objects.all()
    print(D_data1)
    return render(request,'get_dept.html',{'D_data': D_data1})

def edit_dept(request,pk):
    dept1 = Department.objects.get(id = pk)
    return render(request,'dept.html',{'dept':dept1})
# ========================================================================================#

def homepage2(request):
   
    if request.method=='POST':

        id = request.POST.get('Doc_id')
        Name = request.POST.get('Doc_Name')
        No_Of_Doctor = request.POST.get('Doc_No_of_Doctor')
        speciality = request.POST.get('Doc_Hospi_id')

        hospi_id = request.POST.get('Doc_speciality')
          
        if not id:

            a = Department( Name=Name, No_Of_Doctor=No_Of_Doctor, speciality=speciality ,hospi_id=hospi_id)         
            a.save()
            return redirect("get_doctor")
        else :
            b = Department.objects.get(id = id)
            b.Name = Name
            b.No_of_Doctor = No_Of_Doctor
            b.speciality = speciality
            b.hospi_id = hospi_id
            b.save()
            return redirect("get_doctor")     
        
            
    else:
        return render(request, "doctor.html")
    



def get_doctor(request):
    O_doctor1 = Doctor.objects.all()
    return render(request,'get_doctor.html',{'O_doctor': O_doctor1})

def edit_doctor(request,pk):
    doctor1 = Doctor.objects.get(id = pk)
    print(pk)
    return redirect("doctorUpdate")
    # return render(request,'HSPTL/doctor_form.html',{'doctor':doctor1})

from django.views.generic import ListView, CreateView, DetailView, UpdateView

class CreateDoctor(CreateView):
    model = Doctor
    fields = "__all__"
    # print("abc")
    success_url = "http://127.0.0.1:8000/doctorList/"

class DoctorList(ListView):
    model = Doctor
    template_name = 'doctorDetail.html'
    
    
class DetailDoctor(DetailView):
    model = Doctor
    

class DoctorUpdate(UpdateView):
    model = Doctor
    fields = '__all__'
    success_url = "http://127.0.0.1:8000/doctorList/"