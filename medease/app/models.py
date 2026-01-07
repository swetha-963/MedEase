from django.db import models
from django.contrib.auth.models import User

# Address model
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.full_name} - {self.address}"

# Medicine model
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

# Cart model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.medicine.name} x {self.quantity}"

    # Optional: calculate total for this cart item
    @property
    def total_price(self):
        return self.medicine.price * self.quantity


# class LabTest(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.FloatField()
#     description = models.TextField()
#     overview = models.TextField(blank=True)
#     result_interpretation = models.TextField(blank=True)

#     def __str__(self):
#         return self.name


class LabTest(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name