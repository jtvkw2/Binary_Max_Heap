from BinaryMaxHeap import BinaryMaxHeap
from TernaryMaxHeap import TernaryMaxHeap


def main():
    print("What heap would you like?")
    bt_input = input("Binary or Ternary | B or T: ")
    bt_max = input("What is the max: ")
    op = bt_input[0].strip().lower()
    print(op)
    if op == "b" or op == "binary":
        heap = BinaryMaxHeap(bt_max)
    elif op == "t" or op == "ternary":
        heap = TernaryMaxHeap(bt_max)
    else:
        print("Not a valid input")
        main()

    print('\nCommands: ')
    print('insert <data>')
    print('max get')
    print('max extract')
    print('exit\n')

    while True:
        do = input('What would you like to do? ').split()

        to_do = do[0].strip().lower()
        if to_do == 'insert':
            data = int(do[1])
            heap.insert(data)
        elif to_do == 'max':
            sub_operation = do[1].strip().lower()
            if sub_operation == 'get':
                print('Maximum value: {}'.format(heap.get_max()))
            elif sub_operation == 'extract':
                print('Maximum value removed: {}'.format(heap.extract_max()))
        elif to_do == 'exit':
            exit(0)


main()
