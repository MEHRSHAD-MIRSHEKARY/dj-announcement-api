from typing import Iterable, Union

from django_announcement.models.announcement_category import AnnouncementCategory
from django_announcement.models.audience import Audience

# Type Alias for Announcement QuerySet
Audiences = Union[Audience, int, Iterable[Audience]]
Categories = Union[AnnouncementCategory, int, Iterable[AnnouncementCategory]]
