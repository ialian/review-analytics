data = [] #存放的空清單
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		# if count % 100000 == 0:
		# 	print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

# print(data[0])

wc = {} # word_count
for d in data:
	words = d.split(' ') # 遇到空格就分割
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進wc字典

for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])

# 使用者查詢
while True:
	word = input('請輸入要查詢的字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('這個字沒有出現過')

print('感謝使用')





















# sum_len = 0
# for d in data:
# 	sum_len = sum_len + len(d)

# print('留言的平均長度為', sum_len/len(data))

# #篩選條件 選100各字以下的

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('一共有', len(new), '筆資料留言小於100')

# #篩選條件 選有提到good字眼的
# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '筆留言提到good')
# print(good[0])