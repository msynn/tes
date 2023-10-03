
def hitung_korelasi(x, y):
    n = len(x)
    if n != len(y):
        print("Panjang data x dan y harus sama")
    x2 = []
    y2 = []
    xy = []
    # Tampungan Sigma
    sigma = {
        'x' : 0,
        'y' : 0,
        'x2' : 0,
        'y2' : 0,
        'xy' : 0
    }
    
    for i in range(n):
        # Membuat hasil X^2, Y^2, dan XY
        x2.append((x[i] ** 2))
        y2.append((y[i] ** 2))
        xy.append((x[i] * y[i]))

        # sigma X^2, Y^2, dan XY
        sigma['x'] += x[i]
        sigma['y'] += y[i]
        sigma['x2'] += x2[i]
        sigma['y2'] += y2[i]
        sigma['xy'] += xy[i]

    sxx = sigma['x2'] - (sigma['x']**2)/ n
    syy = sigma['y2'] - (sigma['y']**2)/ n 
    sxy = sigma['xy'] - (sigma[x] * sigma['y'])/n

    hasil_korelasi = sxy / ((syy**0.5) * (sxx**0.5))
    return hasil_korelasi
    
# Contoh penggunaan
data_x = [1, 2, 3, 4, 5]
data_y = [5, 4, 3, 2, 10]

hasil_korelasi = hitung_korelasi(data_x, data_y)
print("Korelasi antara data_x dan data_y:", hasil_korelasi)