from django.db import models

# Car
class Car(models.Model):
    Serial_Number = models.CharField(max_length=100, unique=True)
    model_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    engine_capacity = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.model_name} ({self.year})"

# Customer 
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Salesperson 
class Salesperson(models.Model):
    salesperson_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# SalesInvoice 
class SalesInvoice(models.Model):
    Invoice_ID = models.CharField(max_length=10, unique=True)
    invoice_Number = models.PositiveIntegerField()
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Sale of {self.car} to {self.customer} on {self.date}"

# ServiceTicket
class ServiceTicket(models.Model):
    Service_Ticket_ID = models.CharField(max_length=10, unique=True)
    ticket_number = models.PositiveIntegerField()
    car_ID = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Date_Recieved = models.DateField()
    Comments = models.TextField()
    Date_Returned_to_Customer = models.DateField()
    
    def __str__(self):
        return f"Service Ticket for {self.car_ID} by {self.customer_ID} on {self.Date_Recieved}"

class Mechanic(models.Model):
    mechanic_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# Service 
class Service(models.Model):
    Service_ID = models.CharField(max_length=10, unique=True)
    Service_Name = models.CharField(max_length=100)
    Hourly_Rate = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.Service_Name
    
# Service_Mechanic 
class Service_Mechanic(models.Model):
    Service_Ticket_ID = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    Service_ID  = models.ForeignKey(Service, on_delete=models.CASCADE)
    Mechanic_ID = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    Hours = models.DecimalField(max_digits=5, decimal_places=2)
    Comment = models.TextField()
    Rate = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.Mechanic_ID} assigned to {self.Service_Ticket_ID}"

## Parts
class Parts(models.Model):
    Part_ID = models.CharField(max_length=10, unique=True)
    Part_Name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.Part_Name

# Parts_Used 
class Parts_Used(models.Model):
    Part_ID = models.ForeignKey(Parts, on_delete=models.CASCADE)
    Service_Ticket_ID = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    Number_Used = models.PositiveIntegerField()
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.Part_ID.Part_Name
