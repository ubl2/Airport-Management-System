from rest_framework import serializers
from myapp.models import City,Airport,Airline_code,Airlines,Connecting,Flights,Job_type,Employees,Passengers,State_zipcode,Employee_phone
from myapp.models import Passenger_details,Employee_details,Passenger_phone,Passenger_employee,Tickets,Airport_City,Flight_airport
class City_Serializer(serializers.ModelSerializer):
	class Meta:
		model=City
		fields=('city_name','state','country')

class Airport_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Airport
		fields=('airport_ID','city_name')

class Airline_code_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Airline_code
		fields=('airline_name','code')

class Airlines_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Airlines
		fields=('airline_ID','airline_name')

class Connecting_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Connecting
		fields=('connection_ID','layover_time','airport_ID')

class Flights_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Flights
		fields=('flight_ID','status','time_at_source','time_at_destination','duration','source','destination','source_airport_ID','airline_ID','connection_ID')

class Job_type_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Job_type
		fields=('job_name','salary')

class Employees_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Employees
		fields=('SSN','employee_ID','joining_date','airport_ID','job_name')

class Passengers_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Passengers
		fields=('passenger_ID','passport_number','flight_ID','SSN')

class State_zipcode_Serializer(serializers.ModelSerializer):
	class Meta:
		model=State_zipcode
		fields=('zip_code','State')

class Passenger_details_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Passenger_details
		fields=('passport_number','first_name','middle_name','last_name','gender','age','zip_code','city','country','street_name')

class Employee_details_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Employee_details
		fields=('SSN','first_name','middle_name','last_name','gender','age','zip_code','city','country','street_name')

class Passenger_phone_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Passenger_phone
		fields=('passport_number','phone_number')

class Passenger_employee_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Passenger_employee
		fields=('passport_number','SSN')

class Tickets_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Tickets
		fields=('ticket_ID','classes','price','date_of_travel','source','destination','seat_number','booking_date','passport_number','airline_ID','cancellation_fee','cancel_date','flight_ID')

class Airport_City_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Airport_City
		fields=('city_name','airport_name')

class Flight_airport_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Flight_airport
		fields=('flight_iD','airport_iD')

class Employee_phone_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Employee_phone
		fields=('SSN','phone_number')