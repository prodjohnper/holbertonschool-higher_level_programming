#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

argc = len(argv)
if argc == 0:
    print("{} arguments.".format(argc - 1))

if argc == 1:
    print("{} argument:".format(argc))
    print("{}: {}".format(argc, argv[argc]))
else:
    print("{} arguments:".format(argc - 1))
    for _ in range(1, argc):
        print("{}: {}".format(_, argv[_]))
