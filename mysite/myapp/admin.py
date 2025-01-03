from django.contrib import admin
from myapp.models import City,Airport,Airline_code,Airlines,Connecting,Flights,Job_type,Employees,Passengers,State_zipcode,Employee_phone
from myapp.models import Passenger_details,Employee_details,Passenger_phone,Passenger_employee,Tickets,Airport_City,Flight_airport

admin.site.site_header='Airport Management System'

class CityAdmin(admin.ModelAdmin):
	list_display=('city_name','state','country')
	list_filter=("state","country")

admin.site.register(City,CityAdmin)

class AirportAdmin(admin.ModelAdmin):
	list_display=('airport_ID','city_name')
admin.site.register(Airport,AirportAdmin)

class Airline_codeAdmin(admin.ModelAdmin):
	list_display=('airline_name','code')
	list_filter=("airline_name",)
admin.site.register(Airline_code,Airline_codeAdmin)

class AirlinesAdmin(admin.ModelAdmin):
	list_display=('airline_ID','airline_name')
	list_filter=("airline_name",)
admin.site.register(Airlines,AirlinesAdmin)

class ConnectingAdmin(admin.ModelAdmin):
	list_display=('connection_ID','layover_time','airport_ID')
admin.site.register(Connecting, ConnectingAdmin)

class FlightsAdmin(admin.ModelAdmin):
	list_display=('flight_ID','status','time_at_source','time_at_destination','duration','source','destination','source_airport_ID','airline_ID','connection_ID')
	list_filter=("source","destination","airline_ID")
admin.site.register(Flights,FlightsAdmin)

class Job_typeAdmin(admin.ModelAdmin):
	list_display=('job_name','salary')
	list_filter=("salary",)
admin.site.register(Job_type, Job_typeAdmin)

class EmployeesAdmin(admin.ModelAdmin):
	list_display=('SSN','employee_ID','joining_date','airport_ID','job_name')
	list_filter=("job_name",)
admin.site.register(Employees,EmployeesAdmin)

class PassengersAdmin(admin.ModelAdmin):
	list_display=('passenger_ID','passport_number','flight_ID','SSN')
admin.site.register(Passengers,PassengersAdmin)

class SZAdmin(admin.ModelAdmin):
	list_display=('zip_code','State')
	list_filter=("State",)
admin.site.register(State_zipcode,SZAdmin)

class EPAdmin(admin.ModelAdmin):
	list_display=('SSN','phone_number')
admin.site.register(Employee_phone,EPAdmin)

class PassDetAdmin(admin.ModelAdmin):
	list_display=('passport_number','first_name','middle_name','last_name','gender','age','zip_code','city','country','street_name')
admin.site.register(Passenger_details,PassDetAdmin)

class EmpdetAdmin(admin.ModelAdmin):
	list_display=('SSN','first_name','middle_name','last_name','gender','age','zip_code','city','country','street_name')
admin.site.register(Employee_details,EmpdetAdmin)

class PassphoneAdmin(admin.ModelAdmin):
	list_display=('passport_number','phone_number')
admin.site.register(Passenger_phone,PassphoneAdmin)

class PassempAdmin(admin.ModelAdmin):
	list_display=('passport_number','SSN')
admin.site.register(Passenger_employee,PassempAdmin)

class TicketsAdmin(admin.ModelAdmin):
	list_display=('ticket_ID','classes','price','date_of_travel','source','destination','seat_number','booking_date','passport_number','airline_ID','cancellation_fee','cancel_date','flight_ID')
	list_filter=("classes","price")
admin.site.register(Tickets,TicketsAdmin)

class ACAdmin(admin.ModelAdmin):
	list_display=('city_name','airport_name')
admin.site.register(Airport_City,ACAdmin)

class FAAdmin(admin.ModelAdmin):
	list_display=('flight_iD','airport_iD')
admin.site.register(Flight_airport,FAAdmin)

# Register your models here.
