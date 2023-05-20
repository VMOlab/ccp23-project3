import vm


def main():
    plang_file = 'example/fibonacci.plang'

    my_ptvm = vm.PTVM()
    my_ptvm.load(plang_file)
    snapshots = my_ptvm.run({10, 14})
    print(my_ptvm)


if __name__ == "__main__":
    main()
