from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.views import LoginView
from django.utils import timezone

from .models import Ticket, ContactRelation, ContactLeader
from .forms import TicketForm, CommentForm, LoginForm, ProviderForm, LeaderForm


class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm


@login_required
def index(request):
    queries = request.GET.get('search', '')
    sort_field = request.GET.get('sort', 'created_at')
    order = request.GET.get('order', 'desc')

    if queries:
        ticket_list = Ticket.objects.filter(Q(title__icontains=queries) |
                                            Q(assignee__username__icontains=queries) |
                                            Q(status__icontains=queries) |
                                            Q(description__icontains=queries) |
                                            Q(location__icontains=queries) |
                                            Q(categories__icontains=queries))

    else:
        ticket_list = Ticket.objects.all()

    if order == 'desc':
        sort_field = '-' + sort_field

    ticket_list = ticket_list.order_by(sort_field)
    paginator = Paginator(ticket_list, 10)
    page = request.GET.get('page')

    try:
        tickets = paginator.page(page)

    except PageNotAnInteger:
        tickets = paginator.page(1)

    except EmptyPage:
        tickets = paginator.page(paginator.num_pages)

    form = TicketForm()
    context = {
        'tickets': tickets,
        'form': form,
        'sort_field': sort_field.replace('-', ''),
        'order': order
    }

    return render(request, 'index.html', context)


def add_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_at = timezone.now()
            ticket.save()

            return redirect('index')

    else:
        form = TicketForm()

    return render(request, {'form': form})


def add_comment(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket
            comment.user = request.user
            comment.save()

    return redirect('ticket_by_id', ticket_id=ticket_id)


def ticket_by_id(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)

    return render(request, 'ticket_by_id.html', {'ticket': ticket})


def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)

        form.fields['location'].disabled = True
        form.fields['categories'].disabled = True

        if form.is_valid():
            form.save()
            return redirect('ticket_detail', ticket_id=ticket.id)

    else:
        form = TicketForm(instance=ticket)

    return render(request, {'form': form, 'ticket': ticket})


def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        ticket.delete()
        return redirect('index')

    return render(request, 'delete_ticket.html', {'ticket': ticket})


def upload_media(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('file_list')

    else:
        form = TicketForm()

    return render(request, 'add_ticket.html', {'form': form})


def list_provider(request):
    queries = request.GET.get('search', '')
    sort_field = request.GET.get('sort', 'created_at')
    order = request.GET.get('order', 'desc')

    if queries:
        provider_list = ContactRelation.objects.filter(Q(provider__icontains=queries))

    else:
        provider_list = ContactRelation.objects.all()

    if order == 'desc':
        sort_field = '-' + sort_field

    provider_list = provider_list.order_by(sort_field)
    paginator = Paginator(provider_list, 50)
    page = request.GET.get('page')

    try:
        providers = paginator.page(page)

    except PageNotAnInteger:
        providers = paginator.page(1)

    except EmptyPage:
        providers = paginator.page(paginator.num_pages)

    form = ProviderForm()
    context = {
        'providers': providers,
        'form': form,
        'sort_field': sort_field.replace('-', ''),
        'order': order
    }

    return render(request, 'list_provider.html', context)


def add_provider(request):
    if request.method == 'POST':
        form = ProviderForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('provider_list')

    else:
        form = ProviderForm()

    return render(request, {'form': form})


def list_elder(request):
    queries = request.GET.get('search', '')
    sort_field = request.GET.get('sort', 'created_at')
    order = request.GET.get('order', 'desc')

    if queries:
        elder_list = ContactLeader.objects.filter(Q(name__icontains=queries))

    else:
        elder_list = ContactLeader.objects.all()

    if order == 'desc':
        sort_field = '-' + sort_field

    elder_list = elder_list.order_by(sort_field)
    paginator = Paginator(elder_list, 20)
    page = request.GET.get('page')

    try:
        elders = paginator.page(page)

    except PageNotAnInteger:
        elders = paginator.page(1)

    except EmptyPage:
        elders = paginator.page(paginator.num_pages)

    form = LeaderForm()
    context = {
        'elders': elders,
        'form': form,
        'sort_field': sort_field.replace('-', ''),
        'order': order
    }

    return render(request, 'list_leader.html', context)


def add_elder(request):
    if request.method == 'POST':
        form = LeaderForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('elder_list')

    else:
        form = LeaderForm()

    return render(request, {'form': form})
