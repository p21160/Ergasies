import json

first_time = 0
close = "Οχι"
while (close == "Οχι" or close == "οχι") or first_time == 0:
    first_time = 1
    print("Επιλέξτε ένα απο τα παρακάτω κλειδιά")
    print("Πληκτρολογήστε: x, y, name")
    ans = input()
    if ans =="x" :
        with open("Dictionary.txt") as f:
            values = []
            count = 0
            for line in f:
                js = json.loads(line)
                values.append(js["x"])
                count+=1
                print(count)

        values.sort(reverse = True)
        print("Η μέγιστη τιμή του κλειδιού είναι:", values[0])
        print("Η ελάχιστη τιμή του κλειδιού είναι:", values[count-1])
    elif ans == "y" :
        with open("dictionary.txt") as f:
            values = []
            count = 0
            for line in f:
                js = json.loads(line)
                values.append(js["y"])
                count+=1
        values.sort(reverse = True)
        print("Η μέγιστη τιμή του κλειδιού είναι:", values[0])
        print("Η ελάχιστη τιμή του κλειδιού είναι:", values[count-1])
    else:
        with open("Dictionary.txt") as f:
            values = []
            count = 0
            for line in f:
                js = json.loads(line)
                values.append(js["name"])
                count+=1
        values.sort(reverse = True)
        print("Η μέγιστη (αλφαβητικά) τιμή του κλειδιού είναι:", values[0])
        print("Η ελάχιστη (αλφαβητικά) τιμή του κλειδιού είναι:",values[count-1])

    close = input("Θέλετε να εξέλθετε απο την εφαρμογή;(Ναι/Οχι):")
