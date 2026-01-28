# # trò  chơi đoán từ 
# secret_word = "python"
# hint=" gợi ý đây là 1  ngôn ngữ lập trình giống với 1 con vật dài thòn khôn chân"
# guess=""
# guess_count = 0
# guess_limit = 3
# print(hint)

# while guess!=secret_word:
#     if guess_count < guess_limit:
#         guess = input("Bạn đoán từ gì? ")
#         guess_count +=1
#         if guess != secret_word and guess_count < guess_limit:
#             print("nhap lai !")
#     else:
#         break
    
# if guess == secret_word:
#     print("Chính xác ! ")
# else: 
#     print("Thua rồi !")

charactor = ["duong","hao","quang", "an", "binh", "chi", "dung", "giang", "huong", "khanh", "lan", "minh"]

# Dùng range: Phải gọi charactor[i] để lấy tên
for i in range(len(charactor)):
    if i >= 10:
        break
    print(f"Lần {i + 1}: {charactor[i]}")