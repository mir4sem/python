```python
def main(input_string):
    input_int = int(input_string)
    hex_representation1 = hex(input_int & 0xFF)
    hex_representation2 = hex((input_int >> 8) & 0xFF)
    hex_representation3 = hex((input_int >> 16) & 0x7)
    hex_representation4 = f"0x{((input_int >> 20) & 0x3FF):3x}"
    hex_representation4 = hex_representation4.replace(" ", "")
    hex_representation5 = hex((input_int >> 30) & 0xFF)
    res = (hex_representation1, hex_representation2,
           hex_representation3, hex_representation4, hex_representation5)
    return res

```
