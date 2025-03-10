from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contact_Information
from .forms import ContactForm

# Create your views here.
# Adding contact view
def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()

    return render(request, 'contacts/add_contact.html', {'form': form})


# List all contact
def contact_list(request):
    contacts = Contact_Information.objects.all()
    return render(request, 'contacts/contact.html', {'contacts': contacts})

# Search contacts
def search(request):
    query_set = request.GET.get('q', "")
    contacts = Contact_Information.objects.filter(name__icontains=query_set) | Contact_Information.objects.filter(phone_number__icontains=query_set)
    return render(request, 'contacts/contact.html', {'contacts': contacts, 'query_set': query_set})


# Edit Contact View
def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact_Information, id=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contacts/edit_contact.html', {'form': form})

# Delete Contact View
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact_Information, id=contact_id)
    if request.method == "POST":
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/delete_contact.html', {'contact': contact})