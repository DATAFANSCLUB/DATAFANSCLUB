from django.shortcuts import render, redirect
from .models import contact  

def contact_view(request):
    if request.method == 'POST':
        new_contact = contact(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            message=request.POST.get('message')
        )
        new_contact.save()
        return redirect('success_url')  # Redirect to a success page

    return render(request, 'contact/contact.html')

def success_view(request):
    return render(request, 'contact/success.html')
