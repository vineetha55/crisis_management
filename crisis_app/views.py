from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from.models import *
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request,'index.html')

def Admin_login(request):
    return render(request,'Admin_login.html')


def Admin_login_check(request):
        if request.method == "POST":
            User_name = request.POST.get("User_name")
            password = request.POST.get("password")
            user = authenticate(request, username=User_name, password=password)
            if user is not None:
                login(request, user)
                return redirect("/Admin_home/")
            else:
                return redirect("/loginform/")

def Admin_home(request):
   return render(request,'Admin_home.html')

def add_volunteer(request):
    return render(request,'add_volunteer.html')
def save_volunteer(request):
    a=tbl_volunteer()
    a.fullname=request.POST.get('name')
    a.gender=request.POST.get('gender')
    a.fields=request.POST.get('fields')
    a.availability=request.POST.get('availability')
    a.blood_group = request.POST.get('blood')
    a.emergency_contect = request.POST.get('phone')
    a.address=request.POST.get('address')
    a.district=request.POST.get('district')
    a.email=request.POST.get('email')
    a.phone_number=request.POST.get('phone')
    a.pincode=request.POST.get('pin')
    a.password=request.POST.get('password')
    a.save()
    return redirect('/add_volunteer/')
def view_volunteer(request):
    b=tbl_volunteer.objects.all()
    return render(request,'view_volunteer.html',{"b":b})


def add_disaster_manage(request):
    return render(request,'add_disaster_manage.html')

def save_disaster_manage(request):
    d=tbl_disaster_manage()
    d.disaster_name=request.POST.get('dname')
    d.year=request.POST.get('year')
    d.city=request.POST.get('city')
    d.country=request.POST.get('country')
    d.death_count=request.POST.get('death_count')
    d.hospitalized_count=request.POST.get('hospital_count')
    d.save()
    return redirect('/add_disaster_manage/')

def view_disaster_manage(request):
    e=tbl_disaster_manage.objects.all()
    return render(request,'view_disaster_manage.html',{"e":e})

def add_earthquake(request):
    return render(request,'add_earthquake.html')



def save_earthquake(request):
    q=tbl_earthquake()
    q.earthquake_name=request.POST.get('earth_name')
    q.date=request.POST.get('date')
    q.location=request.POST.get('location')
    q.country=request.POST.get('country')
    q.magnitude_depth=request.POST.get('depth')
    q.epicenter_cordinate=request.POST.get('epicenter')
    q.affected_area=request.POST.get('area')
    q.injuries=request.POST.get('injuries')
    q.structural_damage=request.POST.get('damage')
    q.aftershocks=request.POST.get('shocks')
    q.relief_effort=request.POST.get('relief')
    q.source_reference=request.POST.get('source')
    q.save()
    return redirect('/add_earthquake/')


def view_earthquake(request):
    g=tbl_earthquake.objects.all()
    return render(request,'view_earthquake.html',{"g":g})


def add_hurricane(request):
    return render(request,'add_hurricane.html')

def save_hurricane(request):
    h=tbl_hurricane()
    h.hurricane_name=request.POST.get('hurricane')
    h.date=request.POST.get('date')
    h.location=request.POST.get('location')
    h.country=request.POST.get('country')
    h.wind_speed_category=request.POST.get('wind_speed')
    h.storm_surge_rainfall=request.POST.get('surge')
    h.affected_area=request.POST.get('area')
    h.injuries=request.POST.get('injuries')
    h.structural_damage=request.POST.get('damage')
    h.shelter_information=request.POST.get('shelter')
    h.relief_effort=request.POST.get('relief')
    h.update_change= request.POST.get('update')
    h.source_reference=request.POST.get('source')
    h.save()
    return redirect('/add_hurricane/')

def view_hurricane(request):
    i=tbl_hurricane.objects.all()
    return render(request,'view_hurricane.html',{"i":i})

def add_flood(request):
    return render(request,'add_flood.html')



def save_flood(request):
    f=tbl_flood()
    f.name=request.POST.get('name')
    f.date=request.POST.get('date')
    f.location=request.POST.get('location')
    f.country=request.POST.get('country')
    f.severity_level=request.POST.get('severity')
    f.river_level_rainfall=request.POST.get('river')
    f.affected_area=request.POST.get('area')
    f.injuries=request.POST.get('injuries')
    f.infrastructural_damage=request.POST.get('infra')
    f.evacuations_rescues=request.POST.get('rescue')
    f.relief_effort=request.POST.get('relief')
    f.update_change= request.POST.get('update')
    f.source_reference=request.POST.get('source')
    f.save()
    return redirect('/add_flood/')


def view_flood(request):
    l=tbl_flood.objects.all()
    return render(request,'view_flood.html',{"l":l})



def user_login(request):
    return render(request,'user_login.html')



def user_login_check(request):
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            if tbl_user_registration.objects.filter(email=email, password=password).exists():
                d=tbl_user_registration.objects.get(email=email, password=password)
                request.session["uid"]=d.id
                return redirect("/user_home/")
            else:
                return redirect("/user_login/")



def user_registration(request):
    return render(request,'user_registration.html')




def save_user_registration(request):
    m=tbl_user_registration()
    m.name=request.POST.get('name')
    m.gender=request.POST.get('gender')
    m.mobile=request.POST.get('mobile')
    m.email=request.POST.get('email')
    m.address = request.POST.get('address')
    m.state= request.POST.get('phone')
    m.password = request.POST.get('password')
    m.save()
    return redirect('/user_login/')



def view_user_registration(request):
    n=tbl_user_registration.objects.all()
    return render(request,'view_user_registration.html',{"n":n})



def user_home(request):
    return render(request,'user_home.html')



def add_incident(request):
    return render(request,'add_incident.html')


def save_incident(request):
    i=tbl_incident()
    i.incident_type=request.POST.get('type')
    i.incident_time=request.POST.get('time')
    i.district=request.POST.get('district')
    i.state=request.POST.get('state')
    i.injuries=request.POST.get('injuries')
    i.incident_description=request.POST.get('description')
    i.save()
    return redirect('/add_incident/')



def add_shelter(request):
    return render(request,'add_shelter.html')


def save_shelter(request):
    s=tbl_shelter()
    s.shelter_name=request.POST.get('shelter')
    s.address=request.POST.get('address')
    s.contect_detail=request.POST.get('contect')
    s.capacity=request.POST.get('capacity')
    s.fecility=request.POST.get('fecility')
    s.volunteer_available=request.POST.get('volunteer')
    s.save()
    return redirect('/add_shelter/')



def view_shelter(request):
    t=tbl_shelter.objects.all()
    return render(request,'view_shelter.html',{"t":t})


def shelter_view(request):
    t=tbl_shelter.objects.all()
    return render(request,'shelter_view.html',{"t":t})




def incident_view(request):
    r=tbl_incident.objects.all()
    return render(request,'incident_view.html',{"r":r})


def volunteer_view(request):
    b=tbl_volunteer.objects.all()
    return render(request,'volunteer_view.html',{"b":b})



def add_feedback(request):
    return render(request, "add_feedback.html")

def save_feedback(request):
    if request.method == "POST":
        obj =tbl_feedback_view()
        obj.user_id = request.session["uid"]
        obj.feedback = request.POST.get("feedback")
        obj.status=True
        obj.save()
        return redirect("/add_feedback/")





def feedback_view(request):
      data = tbl_feedback_view.objects.filter(status=True)
      return render(request, "feedback_view.html", {"data": data})


def hide_feedback(request,id):
    d=tbl_feedback_view.objects.get(id=id)
    d.status=False
    d.save()
    return redirect("/feedback_view/")


def delete_volunteer(request,id):
       data = tbl_volunteer.objects.get(id=id)
       return redirect('/view_volunteer/')


def edit_volunteer(request, id):
    data = tbl_volunteer.objects.get(id=id)
    return redirect('/view_volunteer/')


def delete_flood(request, id):
    data = tbl_flood.objects.get(id=id)
    return redirect('/view_flood/')


def edit_flood(request, id):
    data = tbl_flood.objects.get(id=id)
    return redirect('/view_flood/')


def delete_hurricane(request, id):
    data = tbl_hurricane.objects.get(id=id)
    return redirect('/view_hurricane/')


def edit_hurricane(request, id):
    data = tbl_hurricane.objects.get(id=id)
    return redirect('/view_hurricane/')


def delete_earthquake(request, id):
    data = tbl_earthquake.objects.get(id=id)
    return redirect('/view_earthquake/')


def edit_earthquake(request, id):
    data = tbl_earthquake.objects.get(id=id)
    return redirect('/view_earthquake/')


def delete_shelter(request, id):
    data = tbl_shelter.objects.get(id=id)
    return redirect('/view_shelter/')


def edit_shelter(request, id):
    data = tbl_shelter.objects.get(id=id)
    return redirect('/view_shelter/')


def delete_incident(request, id):
    data = tbl_incident.objects.get(id=id)
    return redirect('/incident_view/')


def edit_incident(request, id):
    data = tbl_incident.objects.get(id=id)
    return redirect('/incident_view/')



def contact(request):
   return render(request,'contact.html')



def portfolio(request):
   return render(request,'portfolio.html')


def safety(request):
   return render(request,'safety.html')


def chat(request):
    return render(request,"chat.html")

def get_messages(request):
    messages = list(Message.objects.values('text', 'from_me'))
    return JsonResponse({'messages': messages})

def send_message(request):


        print("post")
        data = request.GET
        text = data.get('text')
        if text:
            # Save message to database
            Message.objects.create(text=text, from_me=True,user_id=request.session['uid'])
            # Retrieve all messages from database
            messages = list(Message.objects.values('text', 'from_me'))
            return JsonResponse({'messages': messages})
        return JsonResponse({}, status=400)


from django.http import JsonResponse


def save_message(request):
    if request.method == 'GET':
        message = request.GET.get('msg', '')  # Get the message from GET parameter
        if message:
            d=Message.objects.create(user_id=request.session['uid'],text=message)
            print("Received message:", message)
            return JsonResponse({'success': True})  # Return success response
        else:
            return JsonResponse({'success': False, 'error': 'Message is empty'},
                                status=400)  # Return error response if message is empty
    else:
        return JsonResponse({'success': False, 'error': 'Only GET requests are allowed'},
                            status=405)  # Return error response for other request methods

def save_message1(request):
    if request.method == 'GET':
        g=request.GET.get("g")
        print(g)
        message = request.GET.get('msg', '')  # Get the message from GET parameter
        if message:
            for i in g:
                d=Message.objects.get(id=i.id)
                d.reply=message
                d.save()
                print("Received message:", message)
                return JsonResponse({'success': True})  # Return success response
        else:
            return JsonResponse({'success': False, 'error': 'Message is empty'},
                                status=400)  # Return error response if message is empty
    else:
        return JsonResponse({'success': False, 'error': 'Only GET requests are allowed'},
                            status=405)  # Return error response for other request methods


def admin_chats(request):
    distinct_users = Message.objects.values('user__name','user_id').distinct()
    return render(request, "admin_chats.html", {"distinct_users": distinct_users})


def view_user_chat(request,id):
    g=Message.objects.filter(user=id)
    return render(request,"admin_chats.html",{"g":g})