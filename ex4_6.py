#!/usr/bin/env python3


def solve(text):
    '''Bóc tách từ `text` ra một list các số theo thứ tự chúng xuất hiện.

    VD: 'Bé lên 3 bé đi lớp 4' -> [3, 4]
    '''

    result = []

    numb = ''
    for i in range(len(text)):
        if text[i].isdigit():
            numb += text[i]
        else:
            if len(numb) > 0:
                result.append(int(numb))
                numb = ''
    return result


def main():
    ss = 'Em ơi có bao nhiêu, 60năm cuộc đời, 20 năm đầu, sung sướng0bao lâu'

    print(solve(ss))
    assert solve(ss) == [60, 20, 0]


if __name__ == "__main__":
    main()
