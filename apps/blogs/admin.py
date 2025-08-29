from django.contrib import admin
from .models import *


admin.site.register(BlogsModel)
admin.site.register(CategoriesModel)
admin.site.register(TagsModel)
admin.site.register(AuthorsModel)

