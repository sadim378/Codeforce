n = int(input())

uniforms = []

for i in range(n):
    host, guest = map(int, input().split())
    uniforms.append([host, guest])

count = 0

for host in range(n):
    for guest in range(n):
        if host != guest:
            if uniforms[host][0] == uniforms[guest][1]:
                count += 1

print(count)