![image](https://github.com/nelsondsouza/iitm-pdsa/assets/19646977/e8f04a39-b8b0-4ab2-9770-4a4bfac12237)

```python
def IsCodeValid(hfcode, message):
    emsg = ''
    huffcode = {}
    maxlength = 0
    for i, j in hfcode.items():
        huffcode[j] = i
        if len(j) > maxlength:
            maxlength = len(j)

    cd = ''
    for b in message:
        cd += b
        if len(cd) > maxlength:
            return False
        if cd in huffcode:
            emsg += huffcode[cd]
            cd = ''

    return True if cd == '' else False
hfcode = eval(input())
message = input()
print(IsCodeValid(hfcode,message)) 
```
