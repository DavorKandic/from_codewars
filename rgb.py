"""Description:
The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3"""



def format(num):
    if num < 0:
        num = 0
    if num > 255:
        num = 255
    hex_str = hex(num)
    formated = hex_str[2:].upper()
    if formated in [str(x) for x in range(0,16)]:
        formated = '0' + formated
    return formated
 
def rgb(r, g, b):
    lst = [r,g,b]
    lst = [format(num) for num in lst]
    return ''.join(lst)
    
    


print(rgb(111, 222, 121))    # [111, 222, 121]

print(rgb(-10, 234, 305))    # [0, 234, 255]

print(rgb(1,2,3))



# sample tests
assert(rgb(0,0,0) == "000000", "testing zero values")
assert(rgb(1,2,3) == "010203", "testing near zero values")
assert(rgb(255,255,255) == "FFFFFF", "testing max values")
assert(rgb(254,253,252) == "FEFDFC", "testing near max values")
assert(rgb(-20,275,125) == "00FF7D", "testing out of range values")

print('All tests are OK!')