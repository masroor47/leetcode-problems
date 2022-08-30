def print_matrix(matrix):
    for i in matrix:
        print(i)


def rotate_image(matrix):
    length = len(matrix)
    layers_count = length // 2
    print(f"num layers {layers_count}")
    for layer in range(layers_count):
        start = layer
        end = length - layer - 1
        print(f"start: {start}, end: {end}")
        
        # print(f"temp: {temp}, layer= {layer}")
        for i in range(start, end):
            temp = matrix[layer][i]
            # print(f"i: {i}")
            # print(f"moving {matrix[end-i+layer][layer]} to {matrix[layer][i]}")
            matrix[layer][i] = matrix[end+layer-i][layer]

            print(f"moving {matrix[length - layer - 1][end + layer - i]} to {matrix[end+layer-i][layer]}")
            matrix[end+layer-i][layer] = matrix[length - layer - 1][end + layer - i]

            matrix[length - layer - 1][end + layer - i] = matrix[i][end]
            
            matrix[i][end] = temp
        print()

    return matrix
            










test1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
test2 = [[1,2,3],[4,5,6],[7,8,9]]


print("matrix before rotation: ")
print_matrix(test2)
print()
print_matrix(rotate_image(test2))