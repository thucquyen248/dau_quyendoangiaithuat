def so_doi_xung(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    dao_nguoc = 0
    while x > dao_nguoc:
        chu_so = x % 10
        dao_nguoc = dao_nguoc * 10 + chu_so
        x //=10
    return x == dao_nguoc or x == dao_nguoc // 10 
print(so_doi_xung(121))
print(so_doi_xung(-121))
print(so_doi_xung(10))
print(so_doi_xung(0))