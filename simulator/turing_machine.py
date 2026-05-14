class TuringMachine:
    def __init__(self, states, initial_state, final_states, transitions, blank_symbol, input_alphabet, tape_alphabet, initial_tape=""):
        self.tape = list(initial_tape) if initial_tape else [blank_symbol]
        self.head_pos = 0
        self.current_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.blank = blank_symbol
        self.halted = False
        self.accepted = False

    def step(self):
        if self.halted: return
        
        char_under_head = self.tape[self.head_pos]
        key = (self.current_state, char_under_head)

        if key in self.transitions:
            next_state, write_char, direction = self.transitions[key]
            self.tape[self.head_pos] = write_char
            self.current_state = next_state

            if direction == 'R':
                self.head_pos += 1
                if self.head_pos == len(self.tape): self.tape.append(self.blank)
            elif direction == 'L':
                if self.head_pos == 0: self.tape.insert(0, self.blank)
                else: self.head_pos -= 1

            if self.current_state in self.final_states:
                self.halted = True
                self.accepted = True
        else:
            self.halted = True
            self.accepted = self.current_state in self.final_states