#!/usr/bin/env python3
def chunk_a_list(animals, N):
    ''' Chia input_data thành các tuple chứa N phần tử (chunk a list).
    Nếu tuple cuối không đủ phần tử thì bỏ đi.
    '''
    result = []
    res = []
    for i in range(len(animals)):
        res.append(animals[i])
        if len(res) == N:
            result.append(tuple(res))
            res = []
        
    return result
def main():
    li = ['meo', 'bo', 'ga', 'cho', 'chim', 'gau', 'voi']
    print(chunk_a_list(li, 2))


if __name__ == "__main__":
    main()
