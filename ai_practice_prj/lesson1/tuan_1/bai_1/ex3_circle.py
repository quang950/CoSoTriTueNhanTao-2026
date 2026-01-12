import math

try:
    r = float(input("Nhập bán kính r: "))
    if r < 0:
        print("Bán kính phải là số không âm.")
    else:
        cv = 2 * math.pi * r
        dt = math.pi * r**2
        print(f"Chu vi hình tròn: {cv:.2f}")
        print(f"Diện tích hình tròn: {dt:.2f}")
except ValueError:
    print("Hãy nhập một số thực hợp lệ")
