#Matrix inverter and system of linear equation solver by Yannik Holenstein

def main():
    try:
        decision = input("Do you want to calculate the inverse matrix (enter A) or solve a system of linear equations (enter B)?: ")
        print("\n")
        if decision == "A":
            dimension = check_dimension()
            all_rows = enter_columns(dimension)
            extended_rows = extend_rows(all_rows, dimension)
            check_invertibility(all_rows, dimension)
            inverse_matrix = calculation(extended_rows, dimension)
            output(inverse_matrix, dimension)
        elif decision == "B":
            dimension = check_dimension()
            all_rows = enter_columns(dimension)
            b_vector = insert_b_vector()
            extended_rows = extend_rows(all_rows, dimension)
            check_invertibility(all_rows, dimension)
            inverse_matrix = calculation(extended_rows, dimension)
            result = adjust_matrix(inverse_matrix, dimension)
            calculate_x(result, b_vector)  
        else:
            exit()
    except:
        print("\n")
        print("Your input is invalid. Please check it.")

#Checks if the input for the dimension is valid. The input must be an integer.
def check_dimension():
    while True:
        try:
            dimension = int(input("What dimension should your square matrix have: "))
            print("\n")
            return dimension 
        except:
            print("Your input is invalid. Try again.")

#The user can enter the numbers for each row separated by comma.
#The function returns a list of a list with all all rows
def enter_columns(dimension):
    all_rows = []
    for i in range(dimension):
        string_user_input = input(f"Enter the numbers for row {i+1} separated by comma: ")
        elements = string_user_input.split(",")
        float_elements = [float(e) for e in elements]
        all_rows.append(float_elements)
    return all_rows

#This function extends each rows with the one from the identity matrix.
#(For example the first row 1 3 5 gets extended to 1 3 5 1 0 0)
def extend_rows(all_rows, dimension):
    all_rows_with_zero = []
    extended_rows = []
    for element in all_rows:
            test = element + [0] * dimension
            all_rows_with_zero.append(test)
    counter = 0
    for element in all_rows_with_zero:
        element[dimension+counter] = 1
        extended_rows.append(element)
        counter += 1
    return extended_rows

#This function calculates the inverse matrix
def calculation(extended_rows, dimension):
    #This function sets the pivot value to one and the others to zero
    def function(i, extended_rows):
        matrix = []
        extended_rows.sort(key=lambda sublist: [abs(x) for x in sublist], reverse=True)
        divider = extended_rows[i][i]
        pivot_row = [element/divider for element in extended_rows[i]]
        for index, element in enumerate(extended_rows):
            if index != i:
                multiplier = element[i]
                subtraction = [x * multiplier for x in pivot_row]
                result = [x - y for x, y in zip(element, subtraction)]
                matrix.append(result)
        matrix.insert(i, pivot_row)
        return matrix
    extended_rows.sort(key=lambda sublist: [abs(x) for x in sublist], reverse=True)
    new_matrix = extended_rows
    for i in range(dimension):
        new_matrix = function(i, new_matrix)
    return new_matrix

#Checks if the matrix is invertible.
#It sets the matrix to upper triangular form and multiplies the pivot values.
#If the product is zero, the matrix is not invertible.
def check_invertibility(all_rows, dimension):
    #This function sets the matrix to upper triangular form.
    def upper_triangular(i, all_rows, counter):
        matrix = []
        all_rows.sort(key=lambda sublist: [abs(x) for x in sublist], reverse=True)
        divider = all_rows[i][i]
        pivot_row = [element/divider for element in all_rows[i]]
        for element in all_rows[i+1:]:
            multiplier = element[i]
            subtraction = [x * multiplier for x in pivot_row]
            result = [x - y for x, y in zip(element, subtraction)]
            matrix.append(result)
        for j in range(counter):
            matrix.insert(j, all_rows[j])
        return matrix
    all_rows.sort(key=lambda sublist: [abs(x) for x in sublist], reverse=True)
    new_matrix = all_rows
    counter=1
    for i in range(dimension-1):
        new_matrix = upper_triangular(i, new_matrix, counter)
        counter +=1
    product = 1
    for i in range(dimension):
        product *= new_matrix[i][i]
    if product == 0:
        print("\n")
        print("The determinant of the matrix is zero. Therefore the matrix is singular.")
    else: 
        None

#This function prints the inverse matrix in the terminal  
def output(inverse_matrix, dimension):
    rounded_list = [[round(x, 2) for x in row] for row in inverse_matrix]
    print("\n")
    print("The inverse of the matrix is:")
    print("\n")
    for element in rounded_list:
            print(element[dimension:])
    print("\n")
    print("The numbers are rounded to two decimal places")

#This function adjusts the inverse matrix so that its a correct list.
def adjust_matrix(inverse_matrix, dimension):
    rounded_list = [[round(x, 2) for x in row] for row in inverse_matrix]
    result = []
    for element in rounded_list:
        result.append(element[dimension:])
    return result

#This function asks the user to enter the vector b in the terminal.
def insert_b_vector():
    print("\n")
    user_input = input("Enter the b vector separted by commas: ")
    element = user_input.split(",")
    b_vector = [float(e) for e in element]
    return b_vector
     
#This function calculates the vector x. Therefore it multiplies the inverse matrix with vector b.
#It also prints the solution in the terminal.
def calculate_x(result, b_vector):  
    x_vector = []   
    for element in result:
        summe = 0  
        for i in range(len(b_vector)):
            product = element[i] * b_vector[i]
            summe += product
        x_vector.append(summe)
    rounded_vector = [round(x) for x in x_vector]
    print("\n")
    print("The solution of the system is:")
    print("\n")
    for i in range(len(rounded_vector)):
        print(f"x{i+1} = {rounded_vector[i]}")

main()