def dao_nguoc_so(x: int) -> int:
    Nho_nhat = -2**31
    Lon_nhat = 2**31 - 1

    ket_qua = 0
    dau = -1 if x < 0 else 1
    x = abs(x)
    while x != 0:
        chu_so = x % 10
        x //= 10
        if ket_qua >Lon_nhat - chu_so // 10:
            return 0
        ket_qua = ket_qua * 10 + chu_so
    return dau * ket_qua
print(dao_nguoc_so(123))
print(dao_nguoc_so(-123))
print(dao_nguoc_so(120))