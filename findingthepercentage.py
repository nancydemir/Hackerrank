
def main():
    
    student_list = []
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()   
   
    #print("student_list:",student_list)
    #print("query_name:",query_name)
    #print("student_marks:",student_marks)
    
    for name in student_marks:
        if query_name == name:               
            #print(query_name,student_marks)
            average = sum(student_marks[query_name])/3
            print("%.2f"%average)
                
if __name__ == '__main__':
    main()

