
def compare(input):
    for first, second in zip(input, input[1:]):
        if first == second:
            print('hooray!')


if __name__ == '__main__':
    input = [1, 2, 3, 4, 5, 6]
    input2 = [1, 2, 3, 4, 4, 6]
    compare(input)
    compare(input2)