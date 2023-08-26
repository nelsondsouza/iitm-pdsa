![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/88c9ac81-24da-4a16-ba00-13a4b2a2f06c)

```python
class HuffmanNode:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

def decode(root, ciphertext):
    message = ''
    temp = root
    for i in ciphertext:
        if i == '0':
            temp = temp.left
        if i == '1':
            temp = temp.right
        if temp.left is None and temp.right is None:
            message += temp.symbol
            temp = root
    return message
```

