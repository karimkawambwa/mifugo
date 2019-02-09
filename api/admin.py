from django.contrib import admin

from .models import Shamba, Ngombe, Mbuzi, Kondo


@admin.register(Shamba)
class ShambaAdmin(admin.ModelAdmin):
    search_fields = ["jina", "jina_fupi"]
    list_display = ["jina", "jina_fupi", "owner"]
    list_filter = ["jina", "jina_fupi", "owner", "breeder"]


@admin.register(Ngombe)
class NgombeAdmin(admin.ModelAdmin):
    search_fields = ["breeder", "breed", "jinsia"]
    list_display = ["tag", "shamba", "breeder", "jinsia", "breed"]
    list_filter = ["shamba", "jinsia", "breed", "breeder"]


@admin.register(Mbuzi)
class MbuziAdmin(admin.ModelAdmin):
    search_fields = ["breeder", "breed", "jinsia"]
    list_display = ["tag", "shamba", "breeder", "jinsia", "breed"]
    list_filter = ["shamba", "jinsia", "breed", "breeder"]


@admin.register(Kondo)
class KondoAdmin(admin.ModelAdmin):
    search_fields = ["breeder", "breed", "jinsia"]
    list_display = ["tag", "shamba", "breeder", "jinsia", "breed"]
    list_filter = ["shamba", "jinsia", "breed"]

