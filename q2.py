def do_sort(students):
    # write codes here
    return sorted_students
 
def get_list(func):
    def decorated(students):
        
    return decorated
 
@get_list
def print_output(each_student):
    # write codes here
    return output
 
students = [['Paul', 90, 'a'], ['Michael', 50, 'b'],['Gina', 90, 'c'],['Marie', 70, 'b']]
print(*print_output(students), sep='\n')