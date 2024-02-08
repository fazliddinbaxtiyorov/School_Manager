from django.urls import path
from .views import home, xizmat, contact, adding_students, malumotnoma, hi, admin, adding_news, adding_achievement, adding_teachers, doc_school, adding

urlpatterns = [
    path('', home),
    path('xizmatlar/', xizmat, name='xizmatlar'),
    path('contact/', contact, name='contact'),
    path('adding/', adding_students, name='add'),
    path('malumotnoma/', malumotnoma, name='malumotnoma'),
    path('hi/', hi, name='hi'),
    path('adminpage/director/', admin, name='adminpage'),
    path('adding_news/', adding_news, name='news'),
    path('adding_achievement/', adding_achievement, name='achievement'),
    path('adding_teachers/', adding_teachers, name='teachers'),
    path('doc/', doc_school, name='doc'),
    path('add_information/', adding, name='add_information'),
]
