from django.contrib import admin
from .models import Address, Medicine, Cart

# Register Address model
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone', 'district', 'state', 'pincode')
    search_fields = ('user__username', 'full_name', 'district', 'state')

# Register Medicine model
@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('stock',)

# Register Cart model
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'medicine', 'quantity', 'total_price')
    search_fields = ('user__username', 'medicine__name')
