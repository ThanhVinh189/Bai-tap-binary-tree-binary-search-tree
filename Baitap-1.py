# Danh sách iPhones
iPhones = [
    {"price": 3000, "name": "iPhone12"},
    {"price": 1000, "name": "iPhone10"},
    {"price": 5000, "name": "iPhone14"},
    {"price": 2000, "name": "iPhone11"},
    {"price": 4000, "name": "iPhone13"},
]

# Lọc các mẫu iPhone có giá từ 3000 đến 5000
filtered_iPhones = sorted(
    [iphone for iphone in iPhones if 3000 <= iphone["price"] <= 5000],
    key=lambda x: x["price"]
)

# In kết quả
print("Danh Sách iPhones có giá từ 3000 đến 5000:")
for iphone in filtered_iPhones:
    print(f"- {iphone['name']} (Giá: {iphone['price']})")
