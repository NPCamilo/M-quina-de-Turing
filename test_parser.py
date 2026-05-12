from parser import MTParser
from turing_machine import TuringMachine

def test_palindrome_parser():
    config = MTParser.parse('palindromo.mt.txt')
    
    tm = TuringMachine(
        states=config['states'],
        input_alphabet=config['input_alphabet'],
        tape_alphabet=config['tape_alphabet'],
        initial_state=config['initial_state'],
        final_states=config['final_states'],
        blank_symbol=config['blank_symbol'],
        transitions=config['transitions'],
        initial_tape="101"
    )

    print("--- Configuración Cargada ---")
    print(f"Estados: {tm.states}")
    print(f"Transiciones detectadas: {len(tm.transitions)}")
    
    print("\n--- Ejecución de Prueba (101) ---")
    while not tm.is_halted:
        tm.step()
    
    print(f"Resultado final: {'Aceptada' if tm.is_accepted else 'Rechazada'}")
    print(f"Cinta final: {tm.get_tape_content()}")

if __name__ == "__main__":
    test_palindrome_parser()