# from django.contrib import admin
# from .models import Movie, Director
# from django.db.models import QuerySet
#
# admin.site.register(Director)
#
# class RatingFilter(admin.SimpleListFilter):
#     title = "Movie by rating"
#     parameter_name = 'qwe'
#
#     def lookups(self,request,model_admin):
#         return [
#                 ('<50','low'),
#                 ('50-70','middle'),
#                 ('70-90','ok'),
#                 ('90+','perfect'),
#         ]
#
#     def queryset(self,request,queryset:QuerySet):
#         if self.value()=='<50':
#             return queryset.filter(rating__lt=50)
#         if self.value()=='50-70':
#             return queryset.filter(rating__gte=50).filter(rating__lt=70)
#         if self.value()=='70-90':
#             return queryset.filter(rating__gte=70).filter(rating__lt=90)
#         return queryset
#
#
#
#
#
# @admin.register(Movie)
# class MovieAdmin(admin.ModelAdmin):
# # !!!!!!!!!!!
#     prepopulated_fields = {'slug':('name',)}
# # !!!!!!!!!!!
#     list_display = ['name','rating','currency','rating_status']
#     list_editable = ['rating','currency']
#     readonly_fields = ['rating']
#     ordering = ['-rating']
#     list_per_page = 7
#     actions = ['set_dollar']
#     search_fields = ['name','rating']
#     list_filter = ['name',RatingFilter]
#
#     @admin.display(description='Status')
#     def rating_status(self,mov:Movie):
#         if mov.rating < 60:
#             return 'Bad'
#         if mov.rating < 75:
#             return 'Not bad'
#         return 'Good'
#
#     @admin.action(description='All in USD')
#     def set_dollar(self,request,qs:QuerySet):
#         count = qs.update(currency=Movie.Usd)
#         self.message_user(request,f'Was changed {count} ')
#
