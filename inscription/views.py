from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import InscriptionForm
from django.shortcuts import render


def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "✅ Félicitations, vous êtes inscrit(e) avec succès !")
            # Rediriger vers la page de confirmation avec le numéro d'inscription
            return redirect('confirmation', reference_number=instance.numero_inscription)
    else:
        form = InscriptionForm()

    context = {
        'form': form
    }
    return render(request, 'inscription.html', context)

def confirmation_inscription(request, reference_number):
    return render(request, 'confirmation.html', {'reference_number': reference_number})

def confirmation(request, reference_number):
    return render(request, 'confirmation.html', {'reference_number': reference_number})

