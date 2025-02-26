class Node:
    def __init__(self, price, name):
        self.price = price
        self.name = name
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, price, name):
        if self.root is None:
            self.root = Node(price, name)
        else:
            self._insert_recursive(self.root, price, name)

    def _insert_recursive(self, current, price, name):
        if price < current.price:
            if current.left is None:
                current.left = Node(price, name)
            else:
                self._insert_recursive(current.left, price, name)
        else:
            if current.right is None:
                current.right = Node(price, name)
            else:
                self._insert_recursive(current.right, price, name)

    def search(self, price):
        return self._search_recursive(self.root, price)

    def _search_recursive(self, current, price):
        if current is None:
            return None
        if price == current.price:
            return {"price": current.price, "name": current.name}
        elif price < current.price:
            return self._search_recursive(current.left, price)
        else:
            return self._search_recursive(current.right, price)

    def to_dict(self, node):
        if node is None:
            return {}
        return {
            "key": {
                "price": node.price,
                "name": node.name
            },
            "left": self.to_dict(node.left),
            "right": self.to_dict(node.right)
        }

# Danh sách iPhone
iPhones = [
    {"price": 3000, "name": "iPhone12"},
    {"price": 1000, "name": "iPhone10"},
    {"price": 5000, "name": "iPhone14"},
    {"price": 2000, "name": "iPhone11"},
    {"price": 4000, "name": "iPhone13"},
]

# Tạo BST và chèn iPhones
bst = BST()
for phone in iPhones:
    bst.insert(phone["price"], phone["name"])

# Tìm kiếm một số giá trị trong cây
search_prices = [2000, 4500, 5000]  
for price in search_prices:
    result = bst.search(price)
    if result:
        print(f"Tìm thấy: {result}")
    else:
        print(f"Không tìm thấy giá {price} trong BST.")
