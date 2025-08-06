from django.contrib import admin
from .models import Flat, Claim, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flat_owned.through
    raw_id_fields = ["owner"]


class FlatAdmin(admin.ModelAdmin):
    search_fields = ["town", "town_district", "address"]
    readonly_fields = ["created_at"]
    list_display = ["address", "price", "new_building", "construction_year", "town"]
    list_editable = ["new_building"]
    list_filter = ["new_building", "rooms_number", "has_balcony"]
    raw_id_fields = ["like_by"]
    inlines = [OwnerInline]


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ["user", "flat"]


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ["flat_owned"]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)
