#EXERCISE 1
my_string="It's morbin time"
my_number=42
my_list=["Klaatu", "Barada", "Nikto"]
my_boolean=True
print (f"String = {my_string}\nNumber={my_number}\nList={my_list}\nBoolean={my_boolean}")
#EXCERSISE 2
my_3_letter_string=my_string[0:3]
print(f"First three characters of {my_string}={my_3_letter_string}")
#EXCERSISE 3
my_first_listed_word=my_list[0]
print(f"The first item in my list is {my_first_listed_word}")
#EXCERSISE 4
my_number_plus_ten=my_number+10
print(f"{my_number} + 10 = {my_number_plus_ten}")
#EXCERSISE 5
my_last_listed_word=my_list[-1]
print(f"The last item in my list is {my_last_listed_word}")
#EXCERSISE 6
names = 'harry,alex,susie,jared,gail,conner'
my_splitted_list=names.split(",")
print(f"My splitted list is {my_splitted_list}")
#EXCERSISE 7
my_excersise_seven_list=my_string.split()
my_first_word_upper=my_excersise_seven_list[0]
my_first_word_upper=my_first_word_upper.upper()
my_excersise_seven_list=my_excersise_seven_list[1:]
delimiter=" "
my_excersise_seven_list=delimiter.join(my_excersise_seven_list)
my_string_with_upper=my_first_word_upper +" "+ my_excersise_seven_list
print(f"My string with the first word in uppercase is = {my_string_with_upper}")
#EXCERSISE 8
print(f"The meaning of life, the universe, and erything else is {my_number}")
#EXCERSISE 9
print("Hello world")