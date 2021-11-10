
def sq_num(num):
    sq = []
    for i in range(1, num+1):
        sq.append(i*i)
    return sq

def sq_num_gen(num):
    for i in range(1,num+1):
        yield i*i

print(sq_num(10))
sq_gen = sq_num_gen(10)
for i in sq_gen:
    print(i)