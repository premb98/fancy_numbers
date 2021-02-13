import sys
class FancyNumbers:
    def __init__(self,number):
        self.number = number
        
    def select_number_combo(self):
        try:
            sel_list = []
            for every in range(0,9999):
                no_list = [int(d) for d in str(every)]
                # print(no_list)
                res = 0
                for i in range(0, len(no_list)):
                    res = res + int(no_list[i])
                # print(res)
                sub_no_list = [int(d) for d in str(res)]
                final_result = 0
                for each in range(0, len(sub_no_list)):
                    final_result = final_result + int(sub_no_list[each])
                # print(final_result)
                if final_result == self.number:
                    sel_list.append(no_list)
                   # print(*no_list,sep=" ")
            return sel_list
        except Exception as e:
            return str(e)

c_obj = FancyNumbers(int(sys.argv[1]))
op = c_obj.select_number_combo()
print(op)
print(len(op))