from django.db import models

# Create your models here.
class tbl_volunteer(models.Model):
    fullname=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=100,null=True)
    fields=models.CharField(max_length=100,null=True)
    availability=models.CharField(max_length=100,null=True)
    blood_group=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100, null=True)
    district=models.CharField(max_length=100, null=True)
    email=models.EmailField(max_length=100, null=True)
    phone_number=models.IntegerField(max_length=100, null=True)
    emergency_contect=models.IntegerField(max_length=100,null=True)
    pincode=models.IntegerField(max_length=100, null=True)
    password=models.CharField(max_length=100, null=True)







class tbl_earthquake(models.Model):
    earthquake_name=models.CharField(max_length=100,null=True)
    date=models.IntegerField(max_length=100,null=True)
    location=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    magnitude_depth=models.CharField(max_length=100,null=True)
    epicenter_cordinate=models.CharField(max_length=100, null=True)
    affected_area=models.CharField(max_length=100, null=True)
    injuries=models.IntegerField(max_length=100, null=True)
    structural_damage=models.IntegerField(max_length=100, null=True)
    aftershocks=models.IntegerField(max_length=100,null=True)
    relief_effort=models.IntegerField(max_length=100, null=True)
    source_reference=models.CharField(max_length=100, null=True)




class tbl_hurricane(models.Model):
    hurricane_name=models.CharField(max_length=100,null=True)
    date=models.IntegerField(max_length=100,null=True)
    location=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    wind_speed_category=models.CharField(max_length=100,null=True)
    storm_surge_rainfall=models.IntegerField(max_length=100, null=True)
    affected_area=models.CharField(max_length=100, null=True)
    injuries=models.IntegerField(max_length=100, null=True)
    structural_damage=models.IntegerField(max_length=100, null=True)
    shelter_information=models.IntegerField(max_length=100,null=True)
    relief_effort=models.IntegerField(max_length=100, null=True)
    update_change=models.IntegerField(max_length=100, null=True)
    source_reference=models.CharField(max_length=100, null=True)


class tbl_flood(models.Model):
    name=models.CharField(max_length=100,null=True)
    date=models.IntegerField(max_length=100,null=True)
    location=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    severity_level=models.CharField(max_length=100,null=True)
    river_level_rainfall=models.IntegerField(max_length=100, null=True)
    affected_area=models.CharField(max_length=100, null=True)
    injuries=models.IntegerField(max_length=100, null=True)
    infrastructure_damage=models.IntegerField(max_length=100, null=True)
    evacuations_rescues=models.CharField(max_length=100,null=True)
    relief_effort=models.IntegerField(max_length=100, null=True)
    update_change=models.CharField(max_length=100, null=True)
    source_reference=models.CharField(max_length=100, null=True)




class tbl_user_registration(models.Model):
    name=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=100,null=True)
    mobile=models.IntegerField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100, null=True)
    state=models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)


class tbl_incident(models.Model):
    incident_type=models.CharField(max_length=100,null=True)
    incident_time=models.CharField(max_length=100,null=True)
    district=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    injuries=models.CharField(max_length=100,null=True)
    incident_description= models.CharField(max_length=100, null=True)







class tbl_shelter(models.Model):
    shelter_name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    contect_detail=models.IntegerField(max_length=100,null=True)
    capacity=models.IntegerField(max_length=100,null=True)
    fecility=models.CharField(max_length=100,null=True)
    volunteer_available=models.IntegerField(max_length=100, null=True)



class tbl_feedback_view(models.Model):
    user=models.ForeignKey(tbl_user_registration,models.CASCADE,null=True)
    feedback=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)
   
class Message(models.Model):
    text = models.TextField(null=True)
    user=models.ForeignKey(tbl_user_registration,on_delete=models.CASCADE,null=True)
    reply=models.TextField(null=True)



