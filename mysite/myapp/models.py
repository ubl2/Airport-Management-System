from django.db import models

# Create your models here.

class City(models.Model):
	city_name=models.CharField(primary_key=True,max_length=40)
	state=models.CharField(max_length=50)
	country=models.CharField(max_length=50)

class Airport(models.Model):
	airport_ID=models.CharField(max_length=15,primary_key=True,unique=True)
	city_name=models.ForeignKey(City,on_delete=models.CASCADE)

class Airline_code(models.Model):
	airline_name=models.CharField(max_length=100,primary_key=True,unique=True)
	code=models.CharField(max_length=5)

#Airline id=first letter of airline+incremental integer
class Airlines(models.Model):
	airline_ID=models.CharField(max_length=10,primary_key=True,unique=True)
	airline_name=models.ForeignKey(Airline_code,on_delete=models.CASCADE)

#Only one connection
class Connecting(models.Model):
	connection_ID=models.AutoField(primary_key=True)
	layover_time=models.PositiveIntegerField()
	airport_ID=models.ForeignKey(Airport,on_delete=models.CASCADE)

#Every flight has connection
#flight_ID is first letter of airline+'_'+incrementing number
class Flights(models.Model):
	flight_ID=models.CharField(max_length=30,primary_key=True,unique=True)
	status=models.CharField(max_length=20)
	time_at_source=models.DateTimeField()
	time_at_destination=models.DateTimeField()
	duration=models.PositiveIntegerField()
	source=models.CharField(max_length=100)
	destination=models.CharField(max_length=100)
	source_airport_ID=models.ForeignKey(Airport,on_delete=models.CASCADE)
	airline_ID=models.ForeignKey(Airlines,on_delete=models.CASCADE)
	connection_ID=models.ForeignKey(Connecting,on_delete=models.CASCADE)

#Salaries Per hour
class Job_type(models.Model):
	job_name=models.CharField(max_length=100,primary_key=True,unique=True)
	salary=models.PositiveIntegerField()

class Employees(models.Model):
	SSN=models.PositiveIntegerField(primary_key=True,unique=True)
	employee_ID=models.PositiveIntegerField(unique=True)
	joining_date=models.DateTimeField()
	airport_ID=models.ForeignKey(Airport,on_delete=models.CASCADE)
	job_name=models.ForeignKey(Job_type,on_delete=models.CASCADE)
	
class Passengers(models.Model):
	passenger_ID=models.PositiveIntegerField(unique=True)
	passport_number=models.CharField(max_length=30,primary_key=True,unique=True)
	flight_ID=models.ForeignKey(Flights,on_delete=models.CASCADE)
	SSN=models.ForeignKey(Employees,on_delete=models.CASCADE)
	

class State_zipcode(models.Model):
	zip_code=models.PositiveIntegerField(primary_key=True,unique=True)
	State=models.CharField(max_length=50)


class Passenger_details(models.Model):
	passport_number=models.CharField(max_length=30,primary_key=True)
	first_name=models.CharField(max_length=100)
	middle_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	gender=models.CharField(max_length=10)
	age=models.PositiveIntegerField()
	zip_code=models.PositiveIntegerField()
	city=models.CharField(max_length=100)
	country=models.CharField(max_length=100)
	street_name=models.CharField(max_length=100)


class Employee_details(models.Model):
	SSN=models.PositiveIntegerField(primary_key=True,unique=True)
	first_name=models.CharField(max_length=100)
	middle_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	gender=models.CharField(max_length=10)
	age=models.PositiveIntegerField()
	zip_code=models.PositiveIntegerField()
	city=models.CharField(max_length=100)
	country=models.CharField(max_length=100)
	street_name=models.CharField(max_length=100)

class Passenger_phone(models.Model):
	passport_number=models.ForeignKey(Passenger_details,on_delete=models.CASCADE)
	phone_number=models.PositiveIntegerField(unique=True)
	class Meta:
		unique_together=["passport_number","phone_number"]


class Passenger_employee(models.Model):
	passport_number=models.ForeignKey(Passenger_details,on_delete=models.CASCADE)
	SSN=models.ForeignKey(Employees,on_delete=models.CASCADE)
	class Meta:
		unique_together=["passport_number","SSN"]

#Insert cancellation fee as 0, dat as 12/12/12 00:00:00 if not existing
class Tickets(models.Model):
	ticket_ID=models.CharField(max_length=30,primary_key=True)
	classes=models.CharField(max_length=20)
	price=models.PositiveIntegerField()
	date_of_travel=models.DateTimeField()
	source=models.CharField(max_length=100)
	destination=models.CharField(max_length=100)
	seat_number=models.PositiveIntegerField()
	booking_date=models.DateTimeField()
	passport_number=models.ForeignKey(Passenger_details,on_delete=models.CASCADE)
	airline_ID=models.ForeignKey(Airlines,on_delete=models.CASCADE)
	cancellation_fee=models.PositiveIntegerField()
	cancel_date=models.DateTimeField(null=True)
	flight_ID=models.ForeignKey(Flights,on_delete=models.CASCADE)

	class Meta:
		unique_together=["passport_number","airline_ID","ticket_ID"]

class Airport_City(models.Model):
	city_name=models.ForeignKey(City,on_delete=models.CASCADE)
	airport_name=models.CharField(max_length=30)


class Flight_airport(models.Model):
	flight_iD=models.ForeignKey(Flights,on_delete=models.CASCADE)
	airport_iD=models.ForeignKey(Airport,on_delete=models.CASCADE,unique=True)

	class Meta:
		unique_together=["flight_iD","airport_iD"]

class Employee_phone(models.Model):
	SSN=models.ForeignKey(Employees,on_delete=models.CASCADE)
	phone_number=models.PositiveIntegerField(unique=True)
	class Meta:
		unique_together=["SSN","phone_number"]


