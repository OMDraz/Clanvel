from django.contrib import admin
from django.utils.html import mark_safe
from . import models


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Cohort)
class CohortAdmin(admin.ModelAdmin):
    """ cohort Admin Definition """
    inlines = (PhotoInline,)

    fieldsets = (
        (
        "Basic Info",
            {
                "fields": (
                'name',
                'description',
                'city',
                'price',
                'guests',
                'size',
                )
            },
        ),
        ("Times", {"fields": (                
                'check_in',
                'check_out',
                'instant_book',
            )
        }),
        ("Spaces", {"fields": (               
                'cohortName',
                'cohortLocations',
                'cohortRules',
                )
            }
        ),
        ("Last Details", {"fields": ('cohort_guide',)}),
    )

    list_display = (
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
        'description',
        'city',
        'price',
        'guests',
        'size',
        'instant_book',
        'cohort_guide',
    )
    search_fields = ("=city",)
    filter_horizontal = ("cohortLocations", "cohortRules", "cohortName")

    def count_locations(self, obj):
        return obj.cohortLocations.count()

    count_locations.short_description = "Locations Count"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Phot Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"