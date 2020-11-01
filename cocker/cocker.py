import docker
import json
from src.python_tester import tester

# def test_python_code(code, tests, timeout = 1, memory_limit = '256m'):
#     result = {'passed_tests' : 0, 'status' : tester.TestResult.success}
#     client = docker.from_env()
#     for test in tests:
#         status = tester.TestResult.success
#         arguments = [code, json.dumps(test)]
#         container = client.containers.create('test-cocker', arguments, mem_limit=memory_limit)
#         container.start()
#         stats = container.stats(stream=False)
#         container.stop(timeout=timeout)
#         container.wait()
#         output_str = container.logs().decode('utf-8')
#         if len(output_str) == 0:
#             status = tester.TestResult.timeout
#         else:
#             try:
#                 output_status_int = int(output_str)
#             except Exception:
#                 status = tester.TestResult.internal_error
#             else:
#                 status = tester.TestResult(output_status_int)


#         print(stats)
#         result['status'] = status
        
#         print(status)
#         if status != tester.TestResult.success:
#             break

#         result['passed_tests'] = result['passed_tests'] + 1
#     return result


def test_python_code(code, tests, timeout = 1000, memory_limit = '256m'):
    result = []
    client = docker.from_env()
    for test in tests:
        test_result = {'status' : tester.TestResult.success, 'execution_time' : 0.0}

        arguments = [code, test['input']]
        container = client.containers.create('test-cocker', arguments, mem_limit=memory_limit, cpuset_cpus='1')
        container.start()
        container.stop(timeout=timeout)
        container.wait()
        output_str = container.logs().decode('utf-8')
        if len(output_str) == 0:
            test_result['status'] = tester.TestResult.timeout
        else:
            try:
                container_result = json.loads(output_str)
                test_result['status'] = container_result['status']
                if container_result['status'] == tester.TestResult.success:
                    if container_result['output'] != test['output']:
                        test_result['status'] = tester.TestResult.wrong_answer
                test_result['execution_time'] = container_result['execution_time']
            except Exception as e:
                print(e)
                test_result['status'] = tester.TestResult.internal_error

        result.append(test_result)

        if test_result['status'] != tester.TestResult.success:
            break
    return result

 

def build_python_image():
    client = docker.from_env()
    print(client.images.build(path='C:\\Users\\admin\\Desktop\\cocker\\src\\python_tester', dockerfile='dockerfile', tag='test-cocker')[0])


build_python_image()
print(test_python_code('''
print("test out")
a = 0
while a != 100000:
    print("")
    a = a + 1
with open("output.txt", "w") as input_file:
    input_file.write("123")''',
     [{'input' : "test1", 'output' : "123"}, {'input' : "aaaaaaa", 'output' : "1234"}]))

docker.from_env().containers.prune()