#!/usr/bin/env python3
def solve(input_data):
    '''Đầu vào: một số nguyên dương

    Đầu ra: số nguyên tạo bởi phần từ số 1 cuối cùng trở về bên
    phải - của dạng binary của số đầu vào.

    Ví dụ::

      input_data = 5 # (0b101)
      output = 1

      input_data = 24 (11000)
      output = 1000

      input_data = 9 (1001)
      output = 1

    Hàm có sẵn: bin(10) == '0b1010'
    '''

    result = None
    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    result = bin(input_data)[bin(input_data).rfind('1'):]
    return result


def main():
    print(solve(1000))


if __name__ == "__main__":
    main()
