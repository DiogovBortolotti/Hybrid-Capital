from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChaveAPI, RegistroTrade
from .forms import ChaveAPIForm
from .tasks import monitorar_e_operar


@login_required
def painel(request):
    chaves = ChaveAPI.objects.filter(usuario=request.user)
    logs = RegistroTrade.objects.filter(chave__usuario=request.user).order_by('-criado_em')[:200]
    return render(request, 'bots/dashboard.html', {'chaves': chaves, 'logs': logs})


@login_required
def adicionar_chave(request):
    if request.method == 'POST':
        form = ChaveAPIForm(request.POST)
        if form.is_valid():
            chave = form.save(commit=False)
            chave.usuario = request.user
            chave.definir_secret(form.cleaned_data['api_secret'])
            chave.save()
            return redirect('painel')
    else:
        form = ChaveAPIForm()
    return render(request, 'bots/api_form.html', {'form': form})


@login_required
def iniciar_monitoramento(request, chave_id):
    monitorar_e_operar.delay(chave_id, 'BTCUSDT')
    return redirect('painel')
