import math

points = [(4, 5), (4, 6), (4, 8), (4, 10)]  

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Tüm nokta çiftleri arasındaki mesafeleri hesaplama
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma - yazdırma
min_distance = min(distances)
print(f"Minimum Öklid mesafesi: {min_distance}")
