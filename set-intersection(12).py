N1 = int(input())
storage1 = set(input().split())

N2 = int(input())
storage2 = set(input().split())

storage3 = storage2.intersection(storage1)

print(len(storage3))

