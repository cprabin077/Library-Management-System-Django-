from django.contrib import admin

# Register your models here.
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone",
        "email",
        "gender",
        "is_active",
        "joined_at",
    )

    list_filter = (
        "gender",
        "is_active",
        "joined_at",
    )

    search_fields = (
        "first_name",
        "middle_name",
        "last_name",
        "phone",
        "email",
    )

    ordering = ("-joined_at",)

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Personal Information", {
            "fields": (
                "first_name",
                "middle_name",
                "last_name",
                "gender",
            )
        }),

        ("Contact Information", {
            "fields": (
                "phone",
                "email",
                "country",
            )
        }),

        ("Membership Details", {
            "fields": (
                "is_active",
                "joined_at",
            )
        }),

        ("Timestamps", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )
