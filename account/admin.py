from django.contrib import admin

from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "firstName",
        "lastName",
        "trustNumber",
        "email",
        "is_active",
        "is_admin",
    )
    list_filter = ("is_active", "is_admin")
