from django.contrib.admin import register

from django_announcement.mixins.admin.base import BaseModelAdmin
from django_announcement.models import AnnouncementCategory


@register(AnnouncementCategory)
class AnnouncementCategoryAdmin(BaseModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    list_display_links = ["name"]
    list_filter = BaseModelAdmin.list_filter + ["updated_at"]
    search_fields = BaseModelAdmin.search_fields + ["name", "description"]
    fieldsets = [
        (
            None,
            {
                "fields": ("name", "description"),
            },
        ),
    ] + BaseModelAdmin.fieldsets