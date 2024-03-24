from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cliente, Staff, Usuario


class CustomCliente(UserAdmin):
    model = Cliente
    fieldsets = UserAdmin.fieldsets + (
        (
            "Campos adicionales",
            {
                "fields": (
                    "edad",
                    "direccion",
                    "telefono",
                )
            },
        ),
    )
    # Con esto te saldra al crear un nuevo usuario desde admin los campos
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Campos adicionales",
            {"fields": ("direccion", "edad", "telefono")},
        ),
    )


class CustomStaff(UserAdmin):
    model = Staff
    fieldsets = UserAdmin.fieldsets + (
        (
            "Campos adicionales",
            {"fields": ("funcion", "telefono")},
        ),
    )
    # Con esto te saldra al crear un nuevo usuario desde admin los campos
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Campos adicionales",
            {
                "fields": (
                    "funcion",
                    "telefono",
                )
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        # Establecer staff_status en True solo si es un Staff nuevo
        if not change:
            obj.staff_status = True
        super().save_model(request, obj, form, change)


admin.site.register(Usuario, UserAdmin)
admin.site.register(Cliente, CustomCliente)
admin.site.register(Staff, CustomStaff)
