data = [] #存放的空清單
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data))

#篩選條件 選100各字以下的

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆資料留言小於100')
print(new[0])