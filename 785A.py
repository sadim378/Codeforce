n = int(input())
face = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

total = 0

for i in range(n):
    shape = input()

    total += face[shape]

print(total)