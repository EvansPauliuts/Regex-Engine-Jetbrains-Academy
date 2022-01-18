# write your code here
import sys
import re

sys.setrecursionlimit(10000)


class RegexEngine:
    def __init__(self):
        pass

    @staticmethod
    def get_info(name):
        if len(name) <= 2:
            r = re.compile(name[0])
            print(bool(list(filter(r.search, [name[1]]))))
        else:
            print('Data there should be two!')


def main():
    user_input = input().split('|')
    RegexEngine.get_info(user_input)


if __name__ == '__main__':
    main()
