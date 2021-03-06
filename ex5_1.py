#!/usr/bin/env python3


data = {
    'xanh lá': '#3cba54',
    'vàng': '#f4c20d',
    'đỏ': '#db3236',
    'xanh da trời': '#4885ed',
}


def solve(colors):
    '''Ghi ra file index.html code HTML để tạo ra logo của Google với màu sắc
    chính xác.
    Biết cách để tạo chữ G màu xanh da trời dùng code HTML sau::

      <span style="color:#4885ed">G</span>

    Return list chứa các tuple, mỗi tuple  chứa chữ cái trong 'Google' và màu
    của nó.
    Gợi ý: dùng `zip`

        In [1]: list(zip(['xanh', 'do'], ['XXX', 'YYY']))
        Out[1]: [('xanh', 'XXX'), ('do', 'YYY')]
    '''
    result = []

    # Xoá dòng raise và Viết code vào đây set result làm kết quả
    #raise NotImplementedError("Học viên chưa làm bài này")
    f = open('index.html', 'w')
    result = list(zip(['G', 'o', 'o', 'g', 'l', 'e'], 
                    [colors['xanh da trời'], colors['đỏ'], colors['vàng'], colors['xanh da trời'], colors['xanh lá'], colors['đỏ']]))
    text = ''
    for i in range(len(result)):
        text += '<span style="color :{0}">{1}</span>'.format(result[i][1], result[i][0]) + '\n'
    f.write(text)
    f.close()
    return result


def main():
    '''Biết mã hex của các màu trong Google logo là:
    '''
    colors = data
    print(solve(colors))


if __name__ == "__main__":
    main()
