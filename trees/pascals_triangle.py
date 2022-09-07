





def generate_triangle(numRows):

    # current_row = [1]
    

    # def triangle(numRows, row):
    #     if numRows == 0:
    #         return None

    #     next_row = 



    # return triangle(numRows, current_row)

    current_row = [1]
    answer = [current_row[:]]
    print(f"answer before anything: {answer}")
    for i in range(numRows-1):
        temp = 1
        for j in range(1,len(current_row)):
            sum = temp + current_row[j]
            temp = current_row[j]
            current_row[j] = sum

        current_row.append(1)
        print(f"new row after adding stuff: {current_row}")
        answer.append(current_row[:])
        print(f"answer after appending stuff {answer}")


        print()

    return answer


print(generate_triangle(5))
