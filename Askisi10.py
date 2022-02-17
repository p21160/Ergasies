count_even = 0
count_div3 = 0
count_div5 = 0
count_div7 = 0
with open("ASCII.txt") as f:
    list_data = []
    item_data = ""
    item_counter = 0
    list_item_count = 0
    for line in f:
        for letter in line:
            list = []
            list.append(bin(ord(letter)))
            count = 0
            data = ""
            for item in list[0]:
                if (count > 1 and count < 4) or (count > 6 and count <9):
                    data += item
                count = count + 1
            item_data += data
            item_counter+=4
            if item_counter % 16 == 0:
                list_data.append(int(item_data,2))
                item_data = ""
                list_item_count += 1
    print(list_data)
for number in list_data:
    if number % 2 == 0:
        count_even += 1
    if number % 3 == 0:
        count_div3 += 1
    if number % 5 == 0:
        count_div5 += 1
    if number % 7 == 0:
        count_div7 += 1
percentage_even = count_even/list_item_count*100
percentage_div3 = count_div3/list_item_count*100
percentage_div5 = count_div5/list_item_count*100
percentage_div7 = count_div7/list_item_count*100
print("Οι ζυγοί αριθμοί είναι:",count_even,"ή",percentage_even,"%")
print("Οι αριθμοί που διαιρούνται ακριβώς με το 3 είναι:",count_div3,"ή",percentage_div3,"%")
print("Οι αριθμοί που διαιρούνται ακριβώς με το 5 είναι:",count_div5,"ή",percentage_div5,"%")
print("Οι αριθμοί που διαιρούνται ακριβώς με το 7 είναι:",count_div7,"ή",percentage_div7,"%")
