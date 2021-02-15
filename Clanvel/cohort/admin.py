from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Cohort 
from .forms import CohortCreationForm, CohortAdminChangeForm

class CohortAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = CohortAdminChangeForm
    add_form = CohortCreationForm
    exclude = ('password1','password2','username')
    ordering = ('name',)
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = (
            'uid',
            'name',
            'description',
            'city',
            'price',
            'guests',
            'size',
            'check_in',
            'check_out',
            'instant_book',
            'cohort_guide',
            )
    list_filter = (
            'name',
            'city',
            'price',
            'guests',
            'size',
            'check_in',
            'check_out',
            'instant_book',
    )
    fieldsets = (
        (None, {'fields': ('uid', 'name')}),
        ('Description', {'fields': 
            (
            'city',
            'price',
            'cohort_guide'
            )}),
        ('Cohort Info', {'fields': (
            'guests',
            'size',
            'check_in',
            'check_out',
            'instant_book',
            )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    search_fields = ('name','city')
    filter_horizontal = ()


admin.site.register(Cohort, CohortAdmin)
