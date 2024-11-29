def count_colors(formation):
    color_count = {}
    for color in formation:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    return color_count

def calculate_penalty(Fi, Fi_plus_1):
    count_Fi = count_colors(Fi)
    count_Fi_plus_1 = count_colors(Fi_plus_1)

    total_penalty = 0

    for color in count_Fi:
        if color not in count_Fi_plus_1:
            total_penalty += count_Fi[color] * 7  # Penarikan
        else:
            difference = count_Fi[color] - count_Fi_plus_1[color]
            if difference > 0:
                total_penalty += difference * 7  # Penarikan
            elif difference < 0:
                total_penalty += -difference * 11  # Penyisipan

    for color in count_Fi_plus_1:
        if color not in count_Fi:
            total_penalty += count_Fi_plus_1[color] * 11  # Penyisipan

    return total_penalty

def main():
    T = int(input("Masukkan jumlah formasi: "))
    formasi = []
    for i in range(T):
        formation = input(f"Masukkan formasi F{i + 1} (pisahkan dengan spasi): ").split()
        formasi.append(formation)

    total_penalty = 0
    for i in range(T - 1):
        total_penalty += calculate_penalty(formasi[i], formasi[i + 1])

    print("Total pengurangan poin minimum: ", total_penalty)

if __name__ == "__main__":
    main()