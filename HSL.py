def hue2rgb(v1, v2, vh):
    temp = v1
    if vh < 0.0:
        vh += 1.0
    if vh > 1.0:
        vh -= 1.0
    if 6.0 * vh < 1.0:
        temp = v1 + (v2 - v1) * 6.0 * vh
    elif 2.0 * vh < 1.0:
        temp = v2
    elif 3.0 * vh < 2.0:
        temp = v1 + (v2 - v1) * (2.0 / 3.0 - vh) * 6.0
    return temp

def hsl2rgb(hsl):
    if 0.0001 >= hsl[1] >= -0.0001:
        r = hsl[2]
        g = hsl[2]
        b = hsl[2]
    else:
        if hsl[2] < 0.5:
            var_2 = hsl[2] * (1.0 + hsl[1])
        else:
            var_2 = (hsl[2] + hsl[1]) - (hsl[1] * hsl[2])
        var_1 = 2.0 * hsl[2] - var_2
        r = hue2rgb(var_1, var_2, hsl[0] + 1.0 / 3.0)
        g = hue2rgb(var_1, var_2, hsl[0])
        b = hue2rgb(var_1, var_2, hsl[0] - 1.0 / 3.0)
        r = max(min(1.0, r), 0.0)
        g = max(min(1.0, g), 0.0)
        b = max(min(1.0, b), 0.0)
    return r, g, b

def rgb2hsl(rgb):
    min_val = min(rgb[0], rgb[1], rgb[2])
    max_val = max(rgb[0], rgb[1], rgb[2])
    delta = max_val - min_val
    l = (max_val + min_val) * 0.5
    if 0.0001 >= delta >= -0.0001:
        h = 0.0
        s = 0.0
    else:
        if l < 0.5:
            s = delta / (max_val + min_val)
        else:
            s = delta / (2.0 - max_val - min_val)
        half_delta = delta * 0.5
        inv_delta = 1.0 / delta
        delta_r = ((max_val - rgb[0]) / 6.0 + half_delta) * inv_delta
        delta_g = ((max_val - rgb[1]) / 6.0 + half_delta) * inv_delta
        delta_b = ((max_val - rgb[2]) / 6.0 + half_delta) * inv_delta
        if rgb[0] >= max_val - 0.0001:
            h = delta_b - delta_g
        elif rgb[1] >= max_val - 0.0001:
            h = 1.0 / 3.0 + delta_r - delta_b
        else:
            h = 2.0 / 3.0 + delta_g - delta_r
        if h < 0.0:
            h += 1.0
        if h > 1.0:
            h -= 1.0
    return h, s, l
