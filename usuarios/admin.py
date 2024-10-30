from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Empleado

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'role')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

class EmpleadoAdmin(admin.ModelAdmin):
    model = Empleado
    list_display = ('nombre', 'cuit', 'email', 'telefono', 'fecha_alta', 'fecha_baja')
    search_fields = ('nombre', 'cuit', 'email')
    list_filter = ('fecha_alta', 'fecha_baja')
    ordering = ('nombre',)

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
