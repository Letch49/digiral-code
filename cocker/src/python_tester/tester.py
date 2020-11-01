import sys
import json
import enum
from io import StringIO

class TestResult:
    success = 0
    wrong_answer = 1
    runtime_error = 2
    presentation_error = 3
    timeout = 4
    memory_limit = 5
    internal_error = 6

class Programm:
    def run(self):
        pass

def run_test(programm, test):
    with open('input.txt', 'w') as input_file:
        input_file.write(test['input']) 
    
    try:
        old_out = sys.stdout
        sys.stdout = StringIO()
        programm.run()
    except Exception:
        return TestResult.runtime_error
    finally:
        sys.stdout  = old_out

    try:
        with open('output.txt', 'r') as output_file:
            code_output = output_file.read()
    except Exception:
        return TestResult.presentation_error

    if code_output != test['output']:
        return TestResult.wrong_answer
    
    return TestResult.success