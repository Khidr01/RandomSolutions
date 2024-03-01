def call(r, g, b):
    red = ''
    green = ''
    blue = ''
    def deci_to_hex(num):
        hex_vals = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }
        if num > 255:
            return 'FF'
        if num < 0:
            return '00'
        if num >= 0 and num <= 9:
            return '0' + str(num)
        if num >= 10 and num <= 15:
            return '0' + str(hex_vals.get(num))

        values = []
        divide = 0
        final_res = ''

        while num > 15:
            divide = num % 16
            if divide > 9:
                values.append(hex_vals.get(divide))
            else:
                values.append(divide)
            num = int(num / 16)

        if num > 9:
            values.append(hex_vals.get(num))
        else:
            values.append(num)

        for i in range(len(values) - 1, -1, -1):
            final_res = final_res + str(values[i])

        return final_res

    red = deci_to_hex(r)
    green = deci_to_hex(g)
    blue = deci_to_hex(b)

    return red + green + blue

print(call(11, 12, 13))
