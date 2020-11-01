import sys
import tester
import json
import enum
import timeit
from io import StringIO


if __name__ == '__main__':
    result = {'status' : tester.TestResult.success, 'output' : '', 'execution_time' : 0.0}
    if (len(sys.argv) != 3):
        result = tester.TestResult.internal_error
    else:
        code = sys.argv[1]
        test = sys.argv[2]

        with open('input.txt', 'w') as input_file:
            input_file.write(test) 
    
        try:
            old_out = sys.stdout
            sys.stdout = StringIO()
            start_time = timeit.default_timer()
            exec(code)
            result['execution_time'] = timeit.default_timer() - start_time
        except Exception:
            result['status'] = tester.TestResult.runtime_error
        finally:
            sys.stdout  = old_out

        try:
            with open('output.txt', 'r') as output_file:
                result['output'] = output_file.read()
        except Exception:
            result['status'] = tester.TestResult.presentation_error
    
    print(json.dumps(result))