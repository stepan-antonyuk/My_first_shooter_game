num = int(input())
dev = 2
rem = [1]
ans = 0
sub = num
per = None

def delete_repeat(List):
    return list(dict.fromkeys(List))

def check_sum(list, s):
    list = delete_repeat(list)
    for i in list:
        s -= i
    if s == 0:
        return True
    else:
        return None

# def devis(n, d, s, l, p):
#     if n % d == 0:
#         l.append(d)
#         x = n / d
#         l.append(x)
#     d += 1
#
#     p = check_sum(l, s)
#
#     if d >= n:
#         p = False
#
#     devis(x, d, s, l, p)

while per == None:
    if num % dev == 0:
        rem.append(dev)
        ans = num / dev
        rem.append(ans)
    dev += 1

    per = check_sum(rem, sub)

    if dev >= num:
        per = False

if per == True:
    print("T")
else:
    print("F")