from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.generic import CreateView, DetailView, DeleteView, ListView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Country, Continent, Group
from . import utils
from .forms import *


class AllCountries(ListView):
    model = Country
    template_name = 'main/training.html'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        context['activ_link_all'] = True
        context['form'] = SearchForm()
        return context


def group(request, pk):
    country_list = Country.objects.filter(group_id=pk)
    groups = Group.objects.all()
    template = 'main/training.html'
    form = SearchForm()
    return render(request, template, locals())


def start_game(request):
    activ_link_game: bool = True
    if request.GET.get('group'):
        utils.group_global = request.GET.get('group')

    game = utils.Game()
    groups = Group.objects.all()
    country = game.country
    capitals = game.cap_list_limited()
    form_capital = CapitalSelectForm()
    form_group = GroupSelectForm()
    actiual_group = Group.objects.get(id=utils.group_global) if str(
        group).isdigit() else 'все страны'

    if request.GET.get('capital'):
        if request.GET.get('capital') == utils.old_capital[-2]:
            nice, massage = True, 'Верно!!!'
        else:
            loose, massage = True, f'Столица {utils.old_country[-2]} - {utils.old_capital[-2]}'
    template = 'main/start_game.html'
    return render(request, template, locals())


class CountryDetail(DetailView):
    model = Country
    context_object_name = 'country'
    template_name = 'main/country.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        group = Group.objects.get(pk=context.get('object').group_id)
        context['group'] = group
        return context


class AddCountry(LoginRequiredMixin, CreateView):
    form_class = AddCountryForm
    template_name = 'main/add_country.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['activ_link_add'] = True
        return context


@login_required
def edit_country(request, pk):
    country = Country.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddCountryForm(request.POST, request.FILES, instance=country)
        if form.is_valid():
            form.save()
            return redirect('/')
        return HttpResponse('Форма содержит ошибки')
    else:
        form = AddCountryForm(instance=country)
    template = 'main/edit_country.html'
    return render(request, template, locals())


class DeleteCountry(LoginRequiredMixin, DeleteView):
    model = Country
    template_name = 'main/delete_country.html'
    success_url = '/'


# добавление полей в БД из файлов

# def data(request):
#     countries = Country.objects.all()
#     countries_goup1 = Country.objects.filter(group_id=1)
#     [print(i) for i in countries_goup1]
#     # group_2 = Group.objects.get(id=2)
#     # for c in countries_goup1:
#     #     c.group_id = group_2
#     #     c.save()
#     # with open('main/text_data/raiting.txt', encoding='UTF-8') as data:
#     #     first_class = Group.objects.get(id=1)
#     #     for c in countries:
#     #         for j in data.readlines()[:61]:
#     #             data.seek(0)
#     #             if c.name in j:
#     #                 coutnry = Country.objects.filter(name=c.name)
#     #                 coutnry.update(group_id=first_class.id)
#     return HttpResponse('1')


def search(request):
    search_form = SearchForm()
    if 'search_input' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            country = get_object_or_404(Country, name__iexact=cd['search_input'].capitalize())
    template = 'main/country.html'
    return render(request, template, locals())


def profile(request):
    template = 'registration/profile.html'
    return render(request, template)
