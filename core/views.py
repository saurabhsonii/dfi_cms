from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, ContactForm, AgentRegistrationForm, AgentUpdateForm
from django.contrib.auth import logout
from .models import Contact, CustomUser
# Create your views here.


def index_view(request):
    contact_count = Contact.objects.all().count()
    agent_count = CustomUser.objects.filter(parent_id=request.user.id).count()
    context = {
        "contact_count": contact_count,
        "agent_count": agent_count
    }
    return render(request, "dashboard/index.html", context)

# ---------------------------------contact section-------------------------------------------------------


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your message has been sent successfully!')
            # Redirect to a success page or another view
            return redirect('contact')
        else:
            messages.error(
                request, 'There was an error in your submission. Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'dashboard/contact.html', {'form': form})


def contact_list(request):
    contacts = Contact.objects.all().order_by("-created_at")
    return render(request, 'dashboard/contact-list.html', {'contacts': contacts})


def contact_details(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.is_seen = True
    contact.save()
    return render(request, 'dashboard/contact-details.html', {'contact': contact})


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('contact_list')
# -----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------login section------------------------------------------


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                # Change this to your desired URL after login
                return redirect('home')
            else:
                messages.error(
                    request, 'Invalid email or password. Please try again.')
    else:
        form = LoginForm()

    return render(request, 'dashboard/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
# -------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------


def register_agent(request):
    manager = request.user.id
    if request.method == 'POST':
        form = AgentRegistrationForm(request.POST)

        if form.is_valid():
            agent = form.save(commit=False)
            agent.parent_id = manager
            agent.user_role = 'agent'
            agent.is_agent = True
            agent.save()
            messages.success(request, 'Agent registered successfully.')
            # Redirect to the agent list page
            return redirect('register_agent')

    else:
        form = AgentRegistrationForm()

    return render(request, 'dashboard/register_agent.html', {'form': form})


def agent_list(request):
    manager = request.user.id
    agents = CustomUser.objects.filter(
        user_role='agent', parent_id=manager).order_by("-date_joined")
    return render(request, 'dashboard/agent-list.html', {'agents': agents})


def update_agent(request, agent_id):
    agent = get_object_or_404(CustomUser, id=agent_id, user_role='agent')

    if request.method == 'POST':
        form = AgentUpdateForm(request.POST, instance=agent)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agent details updated successfully.')
            return redirect('agent_list')  # Redirect to the agent list page
    else:
        form = AgentUpdateForm(instance=agent)

    return render(request, 'dashboard/update-agent.html', {'form': form, 'agent': agent})
