from django.shortcuts import render
from rest_framework import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse

from myapp.models import City,Airport,Airline_code,Airlines,Connecting,Flights,Job_type,Employees,Passengers,State_zipcode,Employee_phone
from myapp.models import Passenger_details,Employee_details,Passenger_phone,Passenger_employee,Tickets,Airport_City,Flight_airport

from myapp.serializers import City_Serializer,Airport_Serializer,Airline_code_Serializer,Airlines_Serializer,Connecting_Serializer
from myapp.serializers import Flights_Serializer,Job_type_Serializer,Employees_Serializer,Passengers_Serializer,State_zipcode_Serializer
from myapp.serializers import Passenger_details_Serializer,Employee_details_Serializer,Passenger_phone_Serializer,Passenger_employee_Serializer
from myapp.serializers import Tickets_Serializer,Airport_City_Serializer,Flight_airport_Serializer,Employee_phone_Serializer
# Create your views here.

# @csrf_exempt
# def homeApi(request):
# 		return render(request, 'index.html')

@csrf_exempt
def CityApi(request,id=0):
	if request.method=='GET':
		city=City.objects.all()
		city_serializer=City_Serializer(city,many=True)
		return JsonResponse(city_serializer.data,safe=False)

	elif request.method=='POST':
		city_data=JSONParser().parse(request)
		city_serializer=City_Serializer(data=city_data)
		if city_serializer.is_valid():
			city_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		city_data=JSONParser().parse(request)
		city=City.objects.get(city_name=city_data['city_name'])
		city_serializer=City_Serializer(city,data=city_data)
		if city_serializer.is_valid():
			city_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		city=City.objects.get(city_name=id)
		city.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def AirportApi(request,id=0):
	if request.method=='GET':
		airport=Airport.objects.all()
		airport_serializer=Airport_Serializer(airport,many=True)
		return JsonResponse(airport_serializer.data,safe=False)

	elif request.method=='POST':
		airport_data=JSONParser().parse(request)
		airport_serializer=Airport_Serializer(data=airport_data)
		if airport_serializer.is_valid():
			airport_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		airport_data=JSONParser().parse(request)
		airport=Airport.objects.get(airport_ID=airport_data['airport_ID'])
		airport_serializer=Airport_Serializer(airport,data=airport_data)
		if airport_serializer.is_valid():
			airport_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		airport=Airport.objects.get(airport_ID=id)
		airport.delete()
		return JsonResponse("Deleted Successfully",safe=False)
	

@csrf_exempt
def Airline_codeApi(request,id=0):
	if request.method=='GET':
		airline_code=Airline_code.objects.all()
		airline_code_serializer=Airline_code_Serializer(airline_code,many=True)
		return JsonResponse(airline_code_serializer.data,safe=False)

	elif request.method=='POST':
		airline_code_data=JSONParser().parse(request)
		airline_code_serializer=Airline_code_Serializer(data=airline_code_data)
		if airline_code_serializer.is_valid():
			airline_code_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		airline_code_data=JSONParser().parse(request)
		airline_code=Airline_code.objects.get(airline_name=airline_code_data['airline_name'])
		airline_code_serializer=Airline_code_Serializer(airline_code,data=airline_code_data)
		if airline_code_serializer.is_valid():
			airline_code_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		airline_code=Airline_code.objects.get(airline_name=id)
		airline_code.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def AirlineApi(request,id=0):
	if request.method=='GET':
		airline=Airlines.objects.all()
		airline_serializer=Airlines_Serializer(airline,many=True)
		return JsonResponse(airline_serializer.data,safe=False)

	elif request.method=='POST':
		airline_data=JSONParser().parse(request)
		airline_serializer=Airlines_Serializer(data=airline_data)
		if airline_serializer.is_valid():
			airline_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		airline_data=JSONParser().parse(request)
		airline=Airlines.objects.get(airline_ID=airline_data['airline_ID'])
		airline_serializer=Airlines_Serializer(airline,data=airline_data)
		if airline_serializer.is_valid():
			airline_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		airline=Airlines.objects.get(airline_ID=id)
		airline.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def FlightsApi(request,id=0):
	if request.method=='GET':
		flights=Flights.objects.all()
		fights_serializer=Flights_Serializer(flights,many=True)
		return JsonResponse(fights_serializer.data,safe=False)

	elif request.method=='POST':
		flights_data=JSONParser().parse(request)
		flights_serializer=Flights_Serializer(data=flights_data)
		if flights_serializer.is_valid():
			flights_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		flights_data=JSONParser().parse(request)
		flights=Flights.objects.get(flight_ID=connecting_data['flight_ID'])
		flights_serializer=Flights_Serializer(flights,data=flights_data)
		if flights_serializer.is_valid():
			flights_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		flights=Flights.objects.get(flight_ID=id)
		flights.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def ConnectingApi(request,id=0):
	if request.method=='GET':
		connecting=Connecting.objects.all()
		connecting_serializer=Connecting_Serializer(connecting,many=True)
		return JsonResponse(connecting_serializer.data,safe=False)

	elif request.method=='POST':
		connecting_data=JSONParser().parse(request)
		connecting_serializer=Connecting_Serializer(data=connecting_data)
		if connecting_serializer.is_valid():
			connecting_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		connecting_data=JSONParser().parse(request)
		connecting=Connecting.objects.get(connection_ID=connecting_data['connection_ID'])
		connecting_serializer=Connecting_Serializer(connecting,data=connecting_data)
		if connecting_serializer.is_valid():
			connecting_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		connecting=Connecting.objects.get(connection_ID=id)
		connecting.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def Job_typeApi(request,id=0):
	if request.method=='GET':
		job=Job_type.objects.all()
		job_serializer=Job_type_Serializer(job,many=True)
		return JsonResponse(job_serializer.data,safe=False)

	elif request.method=='POST':
		job_data=JSONParser().parse(request)
		job_serializer=Job_type_Serializer(data=job_data)
		if job_serializer.is_valid():
			job_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		job_data=JSONParser().parse(request)
		job=Job_type.objects.get(job_name=job_data['job_name'])
		job_serializer=Job_type_Serializer(job,data=job_data)
		if job_serializer.is_valid():
			job_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		job=Job_type.objects.get(job_name=id)
		job.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def EmployeeApi(request,id=0):
	if request.method=='GET':
		emp=Employees.objects.all()
		emp_serializer=Employees_Serializer(emp,many=True)
		return JsonResponse(emp_serializer.data,safe=False)

	elif request.method=='POST':
		emp_data=JSONParser().parse(request)
		emp_serializer=Employees_Serializer(data=emp_data)
		if emp_serializer.is_valid():
			emp_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		emp_data=JSONParser().parse(request)
		emp=Employees.objects.get(SSN=emp_data['SSN'])
		emp_serializer=Employees_Serializer(emp,data=emp_data)
		if emp_serializer.is_valid():
			emp_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		emp=Employees.objects.get(SSN=id)
		emp.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def PassengerApi(request,id=0):
	if request.method=='GET':
		pas=Passengers.objects.all()
		pas_serializer=Passengers_Serializer(pas,many=True)
		return JsonResponse(pas_serializer.data,safe=False)

	elif request.method=='POST':
		pas_data=JSONParser().parse(request)
		pas_serializer=Passengers_Serializer(data=pas_data)
		if pas_serializer.is_valid():
			pas_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		pas_data=JSONParser().parse(request)
		pas=Passengers.objects.get(passport_number=pas_data['passport_number'])
		pas_serializer=Passengers_Serializer(pas,data=pas_data)
		if pas_serializer.is_valid():
			pas_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		pas=Passengers.objects.get(passport_number=id)
		pas.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def State_zipApi(request,id=0):
	if request.method=='GET':
		sz=State_zipcode.objects.all()
		sz_serializer=State_zipcode_Serializer(sz,many=True)
		return JsonResponse(sz_serializer.data,safe=False)

	elif request.method=='POST':
		sz_data=JSONParser().parse(request)
		sz_serializer=State_zipcode_Serializer(data=sz_data)
		if sz_serializer.is_valid():
			sz_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		sz_data=JSONParser().parse(request)
		sz=State_zipcode.objects.get(zip_code=sz_data['zip_code'])
		sz_serializer=State_zipcode_Serializer(sz,data=sz_data)
		if sz_serializer.is_valid():
			sz_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		sz=State_zipcode.objects.get(zip_code=id)
		sz.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def Pass_detailsApi(request,id=0):
	if request.method=='GET':
		pd=Passenger_details.objects.all()
		pd_serializer=Passenger_details_Serializer(pd,many=True)
		return JsonResponse(pd_serializer.data,safe=False)

	elif request.method=='POST':
		pd_data=JSONParser().parse(request)
		pd_serializer=Passenger_details_Serializer(data=pd_data)
		if pd_serializer.is_valid():
			pd_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		pd_data=JSONParser().parse(request)
		pd=Passenger_details.objects.get(passport_number=pd_data['passport_number'])
		pd_serializer=Passenger_details_Serializer(pd,data=pd_data)
		if pd_serializer.is_valid():
			pd_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		pd=Passenger_details.objects.get(passport_number=id)
		pd.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def Emp_detailsApi(request,id=0):
	if request.method=='GET':
		emp=Employee_details.objects.all()
		emp_serializer=Employee_details_Serializer(emp,many=True)
		return JsonResponse(emp_serializer.data,safe=False)

	elif request.method=='POST':
		emp_data=JSONParser().parse(request)
		emp_serializer=Employee_details_Serializer(data=emp_data)
		if emp_serializer.is_valid():
			emp_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		emp_data=JSONParser().parse(request)
		emp=Employee_details.objects.get(SSN=emp_data['SSN'])
		emp_serializer=Employee_details_Serializer(emp,data=emp_data)
		if emp_serializer.is_valid():
			emp_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		emp=Employee_details.objects.get(SSN=id)
		emp.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def Pass_phoneApi(request,id=0):
	if request.method=='GET':
		pp=Passenger_phone.objects.all()
		pp_serializer=Passenger_phone_Serializer(pp,many=True)
		return JsonResponse(pp_serializer.data,safe=False)

	elif request.method=='POST':
		pp_data=JSONParser().parse(request)
		pp_serializer=Passenger_phone_Serializer(data=pp_data)
		if pp_serializer.is_valid():
			pp_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		pp_data=JSONParser().parse(request)
		pp=Passenger_phone.objects.get(passport_number=pp_data['passport_number'])
		pp_serializer=Passenger_phone_Serializer(pp,data=pp_data)
		if pp_serializer.is_valid():
			pp_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		pp=Passenger_phone.objects.get(passport_number=id)
		pp.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def Pass_phoneApi(request,id=0):
	if request.method=='GET':
		pe=Passenger_employee.objects.all()
		pe_serializer=Passenger_employee_Serializer(pe,many=True)
		return JsonResponse(pe_serializer.data,safe=False)

	elif request.method=='POST':
		pe_data=JSONParser().parse(request)
		pe_serializer=Passenger_employee_Serializer(data=pe_data)
		if pe_serializer.is_valid():
			pe_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		pe_data=JSONParser().parse(request)
		pe=Passenger_phone.objects.get(passport_number=pe_data['passport_number'])
		pe_serializer=Passenger_employee_Serializer(pe,data=pe_data)
		if pe_serializer.is_valid():
			pe_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		pe=Passenger_employee.objects.get(passport_number=id)
		pe.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def TicketApi(request,id=0):
	if request.method=='GET':
		t=Tickets.objects.all()
		t_serializer=Tickets_Serializer(t,many=True)
		return JsonResponse(t_serializer.data,safe=False)

	elif request.method=='POST':
		t_data=JSONParser().parse(request)
		t_serializer=Tickets_Serializer(data=t_data)
		if t_serializer.is_valid():
			t_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		t_data=JSONParser().parse(request)
		t=Tickets.objects.get(ticket_ID=t_data['ticket_ID'])
		t_serializer=Tickets_Serializer(t,data=t_data)
		if t_serializer.is_valid():
			t_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		t=Tickets.objects.get(ticket_ID=id)
		t.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def Airport_cityApi(request,id=0):
	if request.method=='GET':
		t=Airport_City.objects.all()
		t_serializer=Airport_City_Serializer(t,many=True)
		return JsonResponse(t_serializer.data,safe=False)

	elif request.method=='POST':
		t_data=JSONParser().parse(request)
		t_serializer=Airport_City_Serializer(data=t_data)
		if t_serializer.is_valid():
			t_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		t_data=JSONParser().parse(request)
		t=Airport_City.objects.get(city_name=t_data['city_name'])
		t_serializer=Airport_City_Serializer(t,data=t_data)
		if t_serializer.is_valid():
			t_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		t=Airport_City.objects.get(city_name=id)
		t.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def Flight_airApi(request,id=0):
	if request.method=='GET':
		t=Flight_airport.objects.all()
		t_serializer=Flight_airport_Serializer(t,many=True)
		return JsonResponse(t_serializer.data,safe=False)

	elif request.method=='POST':
		t_data=JSONParser().parse(request)
		t_serializer=Flight_airport_Serializer(data=t_data)
		if t_serializer.is_valid():
			t_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		t_data=JSONParser().parse(request)
		t=Flight_airport.objects.get(airport_iD=t_data['airport_iD'])
		t_serializer=Flight_airport_Serializer(t,data=t_data)
		if t_serializer.is_valid():
			t_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		t=Flight_airport.objects.get(airport_iD=id)
		t.delete()
		return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def Emp_phoneApi(request,id=0):
	if request.method=='GET':
		t=Employee_phone.objects.all()
		t_serializer=Employee_phone_Serializer(t,many=True)
		return JsonResponse(t_serializer.data,safe=False)

	elif request.method=='POST':
		t_data=JSONParser().parse(request)
		t_serializer=Employee_phone_Serializer(data=t_data)
		if t_serializer.is_valid():
			t_serializer.save()
			return JsonResponse("Added Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='PUT':
		t_data=JSONParser().parse(request)
		t=Employee_phone.objects.get(phone_number=t_data['phone_number'])
		t_serializer=Employee_phone_Serializer(t,data=t_data)
		if t_serializer.is_valid():
			t_serializer.save()
			return JsonResponse("Updated Successfully",safe=False)
		return JsonResponse("Failed to Add",safe=False)

	elif request.method=='DELETE':
		t=Employee_phone.objects.get(phone_number=id)
		t.delete()
		return JsonResponse("Deleted Successfully",safe=False)