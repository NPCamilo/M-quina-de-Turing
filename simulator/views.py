from django.shortcuts import render, redirect
from .parser import MTParser
from .turing_machine import TuringMachine

def home(request):
    """
    Vista principal. Si hay una máquina cargada en sesión, muestra el estado actual.
    Si no, muestra el formulario de carga inicial.
    """
    context = {'loaded': False}
    
    if 'mt_config' in request.session:
        cfg = request.session['mt_config']
        context.update({
            'initial_input_display': request.session.get('initial_input_display'),
            'loaded': True,
            'tape': request.session.get('current_tape'),
            'head_pos': request.session.get('head_pos'),
            'current_state': request.session.get('current_state'),
            'step_count': request.session.get('step_count'),
            'halted': request.session.get('halted'),
            'accepted': request.session.get('accepted', False),
            'result_label': 'ACEPTADA' if request.session.get('accepted') else 'RECHAZADA'
        })
    
    if 'error' in request.session:
        context['error'] = request.session.pop('error')
        
    return render(request, 'simulator/home.html', context)

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file_mt'):
        try:
            request.session.flush() 
            file = request.FILES['file_mt']
            with open('temp_machine.mt', 'wb+') as dest:
                for chunk in file.chunks(): dest.write(chunk)
                
            config = MTParser.parse('temp_machine.mt')
            initial_input = request.POST.get('initial_input', '')
            
            # GUARDAR LA CADENA ORIGINAL PARA MOSTRARLA SIEMPRE
            request.session['initial_input_display'] = initial_input if initial_input else "(Vacía)"
            
            config = MTParser.parse('temp_machine.mt')
            initial_input = request.POST.get('initial_input', '')
            if not initial_input: initial_input = config['blank_symbol']

            request.session['mt_config'] = {
                'states': list(config['states']),
                'input_alphabet': list(config['input_alphabet']),
                'tape_alphabet': list(config['tape_alphabet']),
                'initial_state': config['initial_state'],
                'final_states': list(config['final_states']),
                'blank_symbol': config['blank_symbol'],
                'transitions': {f"{k[0]},{k[1]}": v for k, v in config['transitions'].items()}
            }
            request.session['current_tape'] = list(initial_input)
            request.session['head_pos'] = 0
            request.session['current_state'] = config['initial_state']
            request.session['step_count'] = 0
            request.session['halted'] = False
            
        except Exception as e:
            request.session['error'] = str(e)
    return redirect('home')

def step_simulation(request):
    if 'mt_config' not in request.session or request.session.get('halted'):
        return redirect('home')
    
    cfg = request.session['mt_config']
    transitions = {tuple(k.split(',')): v for k, v in cfg['transitions'].items()}
    
    tm = TuringMachine(
        states=set(cfg['states']),
        initial_state=cfg['initial_state'],
        final_states=set(cfg['final_states']),
        transitions=transitions,
        blank_symbol=cfg['blank_symbol'],
        input_alphabet=set(cfg['input_alphabet']), 
        tape_alphabet=set(cfg['tape_alphabet']),   
        initial_tape="".join(request.session['current_tape'])
    )
    tm.head_pos = request.session['head_pos']
    tm.current_state = request.session['current_state']
    
    tm.step()
    
    request.session.update({
        'current_tape': tm.tape,
        'head_pos': tm.head_pos,
        'current_state': tm.current_state,
        'step_count': request.session.get('step_count', 0) + 1,
        'halted': tm.halted,
        'accepted': tm.accepted
    })
    request.session.modified = True 
    return redirect('home')

def run_simulation(request):
    if 'mt_config' not in request.session or request.session.get('halted'):
        return redirect('home')

    cfg = request.session['mt_config']
    transitions = {tuple(k.split(',')): v for k, v in cfg['transitions'].items()}
    
    tm = TuringMachine(
        states=set(cfg['states']),
        initial_state=cfg['initial_state'],
        final_states=set(cfg['final_states']),
        transitions=transitions,
        blank_symbol=cfg['blank_symbol'],
        input_alphabet=set(cfg['input_alphabet']),
        tape_alphabet=set(cfg['tape_alphabet']),
        initial_tape="".join(request.session['current_tape'])
    )
    
    tm.head_pos = request.session['head_pos']
    tm.current_state = request.session['current_state']

    steps = 0
    while not tm.halted and steps < 5000:
        tm.step()
        steps += 1
    
    request.session.update({
        'current_tape': tm.tape,
        'head_pos': tm.head_pos,
        'current_state': tm.current_state,
        'step_count': request.session.get('step_count', 0) + steps,
        'halted': tm.halted,
        'accepted': tm.accepted
    })
    request.session.modified = True 
    
    return redirect('home')

def reset_simulation(request):
    request.session.flush()
    return redirect('home')