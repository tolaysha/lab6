from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from datetime import datetime
from tutoring.models import Education, Subjects, Regions, Tutors
# Create your views here.


class OrdersView(View):
    def get(self, request):
        variable = 'Django'
        today_date = datetime.now()
        data = {
            'orders': [
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3}
            ]
        }
        return render(request, 'orders.html', locals())


class OrderView(View):
    def get(self, request, id):
        variable = 'Django'
        today_date = datetime.now()
        data = {
            'order': {
                'id': id
            }
        }
        return render(request, 'order.html', locals())


def main(request):
    return render(request, 'main.html', locals())


def prog_lang(request, prog_lang):
    name = ['C++', 'Python', 'Java']
    cpp_info = 'C++ — компилируемый, статически типизированный язык программирования общего назначения. Синтаксис C++ унаследован от языка C. Одним из принципов разработки было сохранение совместимости с C. Тем не менее, C++ не является в строгом смысле надмножеством C; множество программ, которые могут одинаково успешно транслироваться как компиляторами C, так и компиляторами C++, довольно велико, но не включает все возможные программы на C.'
    java_info = 'Java — сильно типизированный объектно-ориентированный язык программирования, разработанный компанией Sun Microsystems (в последующем приобретённой компанией Oracle). Приложения Java обычно транслируются в специальный байт-код, поэтому они могут работать на любой компьютерной архитектуре, с помощью виртуальной Java-машины. Дата официального выпуска — 23 мая 1995 года.'
    python_info = 'Python — высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода. Синтаксис ядра Python минималистичен. В то же время стандартная библиотека включает большой объём полезных функций.'
    info = [cpp_info, java_info, python_info]
    data1 = {'lang': {'id': prog_lang}}
    data2 = {'langs': [{'id': 'cpp', 'lang_name': 'C++', 'info': cpp_info},
                       {'id': 'java', 'lang_name': 'Java', 'info': java_info},
                       {'id': 'python', 'lang_name': 'Python', 'info': python_info}]}
    return render(request, 'prog_lang.html', locals())


def db(request):
    return render(request, 'db.html', locals())


class UniversitiesList(ListView):
    model = Education
    template_name = "universities.html"


class SubjectsList(ListView):
    model = Subjects
    template_name = "subjects.html"


class RegionsList(ListView):
    model = Regions
    template_name = "regions.html"


class TutorsList(ListView):
    model = Tutors
    template_name = "tutors.html"
