from dataclasses import dataclass

class Solution:
    @dataclass
    class func_log:
        start_time: int
        exec_time: int
    
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        call_stack = []
        func_dic = {}
        current_func = -1
        for log in logs:
            log_splits = log.split(':')
            function_id = int(log_splits[0])
            status = log_splits[1]
            time = int(log_splits[2])
            if status == 'start':
                call_stack.append(function_id)
                if current_func == -1:
                    current_func = function_id
                    if function_id not in func_dic:
                        func_dic[function_id] = self.func_log(time, 0)
                    else:
                        func_dic[function_id].start_time = time
                elif function_id == current_func:
                    continue
                else:
                    func_dic[current_func].exec_time += time - func_dic[current_func].start_time
                    current_func = function_id
                    if function_id in func_dic:
                        func_dic[function_id].start_time = time
                    else:
                        func_dic[function_id] = self.func_log(time, 0)
            else:
                func_dic[function_id].exec_time += time - func_dic[function_id].start_time + 1
                call_stack.pop()
                if call_stack:
                    current_func = call_stack[-1]
                    func_dic[current_func].start_time = time+1
                else:
                    current_func = -1
            # print(func_dic)
        result = []
        for i in range(n):
            result.append(func_dic[i].exec_time)
        return result
                