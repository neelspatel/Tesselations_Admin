from django.contrib import admin
from data.models import Data
from data.models import Snapshot

admin.site.register(Data)
admin.site.register(Snapshot)
