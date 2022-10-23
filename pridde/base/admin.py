from django.contrib import admin


from .models import ClientMessages, CompanyDetails, Location, Owners, Property,PropertyImage
# Register your models here.

class PictureInline(admin.StackedInline):
    model=PropertyImage
    list_display=("")


class PropertyAdmin(admin.ModelAdmin):
    list_display=("name","location","owner",)
    inlines=[PictureInline]

    class Meta:
        model=Property

admin.site.register(Property,PropertyAdmin)
admin.site.register(Owners)
admin.site.register(CompanyDetails)
admin.site.register(ClientMessages)
admin.site.register(PropertyImage)
admin.site.register(Location)
