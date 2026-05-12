import re

class MTParser:
    @staticmethod
    def parse(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        raw_data = {}
        for line in lines:
            if ':' in line and '->' not in line:
                key, value = line.split(':', 1)
                raw_data[key.strip().lower()] = value.strip()
            elif '->' in line:
                if 'transitions' not in raw_data:
                    raw_data['transitions'] = []
                raw_data['transitions'].append(line.strip())

        config = {
            'states': set(s.strip() for s in raw_data['estados'].split(',')),
            'input_alphabet': set(s.strip() for s in raw_data['alfabeto_entrada'].split(',')),
            'tape_alphabet': set(s.strip() for s in raw_data['alfabeto_cinta'].split(',')),
            'initial_state': raw_data['inicial'],
            'final_states': set(s.strip() for s in raw_data['finales'].split(',')),
            'blank_symbol': raw_data['blanco'],
            'transitions': {}
        }

        for line in raw_data.get('transitions', []):
            left, right = line.split('->')
            curr_state, curr_sym = [x.strip() for x in left.split(',')]
            next_state, write_sym, direction = [x.strip() for x in right.split(',')]
            config['transitions'][(curr_state, curr_sym)] = (next_state, write_sym, direction)

        return config