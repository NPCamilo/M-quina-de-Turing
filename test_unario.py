from turing_machine import TuringMachine

def run_test():
    transitions = {
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', '#'): ('q1', '1', 'R'),
        ('q1', '1'): ('q1', '1', 'R'),
        ('q1', 'B'): ('q2', 'B', 'L'),
        ('q2', '1'): ('qf', 'B', 'S')
    }

    tm = TuringMachine(
        states={'q0', 'q1', 'q2', 'qf'},
        input_alphabet={'1', '#'},
        tape_alphabet={'1', '#', 'B'},
        initial_state='q0',
        final_states={'qf'},
        blank_symbol='B',
        transitions=transitions,
        initial_tape="11#111"
    )

    print(f"Cinta Inicial: {tm.get_tape_content()}")
    
    step_count = 0
    while not tm.is_halted:
        tm.step()
        step_count += 1
        print(f"Paso {step_count} | Estado: {tm.current_state} | Posición: {tm.head_position} | Cinta: {tm.get_tape_content()}")
    print(f"Máquina detenida. Resultado final: {tm.get_tape_content()}")
    print(f"Aceptada: {tm.is_accepted}")

if __name__ == "__main__":
    run_test()