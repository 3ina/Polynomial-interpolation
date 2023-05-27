import numpy
from Point import Point


def change_col(matrx, col_n, value_list):
    matrix_res = matrx.copy()
    for i in range(len(value_list)):
        matrix_res[i, col_n] = value_list[i]

    return matrix_res


program_continue = True

while program_continue:

    print("""
            
██████   ██████  ██      ██    ██ ███    ██  ██████  ███    ███ ██  █████  ██          ██ ███    ██ ████████ ███████ ██████  ██████   ██████  ██       █████  ████████ ██  ██████  ███    ██ 
██   ██ ██    ██ ██       ██  ██  ████   ██ ██    ██ ████  ████ ██ ██   ██ ██          ██ ████   ██    ██    ██      ██   ██ ██   ██ ██    ██ ██      ██   ██    ██    ██ ██    ██ ████   ██ 
██████  ██    ██ ██        ████   ██ ██  ██ ██    ██ ██ ████ ██ ██ ███████ ██          ██ ██ ██  ██    ██    █████   ██████  ██████  ██    ██ ██      ███████    ██    ██ ██    ██ ██ ██  ██ 
██      ██    ██ ██         ██    ██  ██ ██ ██    ██ ██  ██  ██ ██ ██   ██ ██          ██ ██  ██ ██    ██    ██      ██   ██ ██      ██    ██ ██      ██   ██    ██    ██ ██    ██ ██  ██ ██ 
██       ██████  ███████    ██    ██   ████  ██████  ██      ██ ██ ██   ██ ███████     ██ ██   ████    ██    ███████ ██   ██ ██       ██████  ███████ ██   ██    ██    ██  ██████  ██   ████ 
                                                                                                                                                                                             
                                                                                                                                                                                             
                                made by Sina Roydel
    
    """)


    number_of_point = int(input("how many Point do you have?"))

    list_of_point = []
    list_of_y_value = []
    for i in range(number_of_point):
        x_value = int(input("please inter x" + str(i) + " :"))
        y_value = int(input("please inter y" + str(i) + " :"))
        list_of_point.append(Point(x_value, y_value))
        list_of_y_value.append(y_value)

    matrix = []

    for point in list_of_point:
        row = []
        for i in range(number_of_point):
            row.append(point.x ** i)
        matrix.append(row)

    matrix_coefficient = numpy.matrix(matrix)

    det_A = numpy.linalg.det(matrix_coefficient)

    print("Polynomial : ")
    for i in range(len(list_of_point)):
        det_A1 = numpy.linalg.det(change_col(matrix_coefficient, i, list_of_y_value))
        str_res = str(round(det_A1/det_A,2)) + "x^" + str(i)
        if i == len(list_of_point) - 1:
            print(str_res, end="")
        else:
            print(str_res, end=" + ")

    flag = True
    while flag:
        answer = input("Do you want to continue? 'y' or 'n' : ").lower()
        if answer == 'y':
            break
        elif answer == 'n':
            program_continue = False
        else:
            print("please inter 'y' or 'n' ")






