
my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10
print(my_list)

f = open("output.txt", "a")
# open(開啟的檔案名稱及目錄位置(如果沒給位置的話，就存在當前目錄),開啟的方式(包含w:write, r:read, a:append))
for item in my_list:
    f.write(str(item) + "\n")
print(f.closed)

f.close()
# 結束時要記得關閉

with open('test.txt', 'w') as f1:
    f1.write('test\n')
    f1.write('test\n')
# 用with方式打開文件的話，不需要加上close來關閉文件
print(f1.closed)