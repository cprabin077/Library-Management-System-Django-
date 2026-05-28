from django.contrib import admin
from .models import Librarian


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone',
        'gender',
        'qualification',
        'salary',
        'joining_date',
        'is_active',
    )

    search_fields = (
        'full_name',
        'email',
        'phone',
        'qualification',
    )

    list_filter = (
        'gender',
        'qualification',
        'is_active',
        'joining_date',
    )

    ordering = (
        '-created_at',
    )

    list_editable = (
        'is_active',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    fieldsets = (
        ('Personal Information', {
            'fields': (
                'full_name',
                'email',
                'phone',
                'gender',
                'address',
            )
        }),

        ('Professional Information', {
            'fields': (
                'qualification',
                'salary',
                'joining_date',
                'is_active',
            )
        }),

        ('System Information', {
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
    )