import inspect

def parse_input_lines():
    caller_filename = inspect.stack()[1].filename
    day_number = int(''.join([c for c in caller_filename if c.isdigit()]))
    input_filename = f'input/{day_number}.in'
    with open(input_filename) as f:
        return [line.strip() for line in f.readlines()]