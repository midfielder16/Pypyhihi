#!/usr/bin/env python3

'''
Input: một số nguyên trong range(1,13).
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
'''


def solve(input_data):
    '''Trả về 1 `tuple` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February", 28)

    :param input_data: tháng bất kì
    :rtype: tuple
    '''
    assert (input_data in range(1, 13)), "Tháng không tồn tại"
    data = [("January", 31), ("February", 28), ("March", 31), ("April", 30), 
            ("May", 31), ("June", 30), ("July", 31), ("August", 31), 
            ("November", 30), ("October", 31), ("December", 30), ("September", 31)]
    result = tuple((data[input_data - 1]))

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    

    return result


def main():
    month, day = solve(2)
    print(month, day)


if __name__ == "__main__":
    main()
