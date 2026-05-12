class TuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, initial_state, final_states, blank_symbol, transitions, initial_tape=""):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.current_state = initial_state
        self.final_states = final_states
        self.blank_symbol = blank_symbol
        self.transitions = transitions
        
        self.tape = {i: char for i, char in enumerate(initial_tape)} if initial_tape else {0: self.blank_symbol}
        self.head_position = 0
        self.is_halted = False
        self.is_accepted = False

    def get_tape_content(self):
        if not self.tape:
            return self.blank_symbol
        
        min_idx = min(self.tape.keys())
        max_idx = max(self.tape.keys())
        return "".join(self.tape.get(i, self.blank_symbol) for i in range(min_idx, max_idx + 1))

    def step(self):
        if self.is_halted:
            return False

        current_symbol = self.tape.get(self.head_position, self.blank_symbol)
        transition_key = (self.current_state, current_symbol)

        if transition_key in self.transitions:
            new_state, write_symbol, direction = self.transitions[transition_key]
            
            self.tape[self.head_position] = write_symbol
            self.current_state = new_state
            
            if direction == 'R':
                self.head_position += 1
            elif direction == 'L':
                self.head_position -= 1
                
            if self.current_state in self.final_states:
                self.is_halted = True
                self.is_accepted = True
            return True
        else:
            self.is_halted = True
            self.is_accepted = self.current_state in self.final_states
            return False
            
    def run(self, max_steps=1000):
        steps = 0
        while not self.is_halted and steps < max_steps:
            self.step()
            steps += 1
        return self.is_accepted