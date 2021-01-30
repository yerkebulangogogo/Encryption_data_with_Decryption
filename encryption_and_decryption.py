import math
alphabit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            ]
probel = []
id_plain_text = []
id_cypher_text = []
id_answer = []
word_text = input('Please write PLAIN text: ')
cypher_text = input('Please write CYPHER TEXT: ')
back_up = cypher_text
#Encryption part 1 (Viginer part)
for i in range(len(word_text)):
    if word_text[i] == " ":
        probel.append(i)
word_text.replace(" ", '')

counter = 0
flag = False
for i in range(len(word_text)):
    for j in range(len(alphabit)):
        if word_text[i].lower() == alphabit[j]:
            id_plain_text.append(j)
            print(alphabit[j])
            counter += 1
            if counter == len(word_text):
                flag = True
            break
    if flag:
        break

counter = 0
flag = False
for i in range(len(cypher_text)):
    for j in range(len(alphabit)):
        if cypher_text[i].lower() == alphabit[j]:
            id_cypher_text.append(j)
            print(j)
            counter += 1
            if counter == len(cypher_text):
                flag = True
            break
    if flag:
        break
multiple = math.ceil(len(id_plain_text) / len(id_cypher_text))
for i in range(multiple - 1):
    for j in range(len(id_cypher_text)):
        id_cypher_text.append(id_cypher_text[j])
for i in range(len(id_plain_text)):
    answer = (alphabit[id_plain_text[i] + id_cypher_text[i]])
    id_answer.append(answer)
for i in range(len(probel)):
    id_answer.insert(probel[i], ' ')
answer_final =''
for i in range(len(id_answer)):
    answer_final += id_answer[i]
print('FIRST LAYWER ANSWER: {}'.format(answer_final))
print('FIRST LAYWER ENCRYPTION DONE!  1/2')
#Encryption part #2(Caesar part)
number_encryption = len(cypher_text)
plain_text_part_2 = answer_final
space_2 = []
id_plain_text_2 = []
final_list_2 = []
for i in range(len(plain_text_part_2)):
    if plain_text_part_2[i] == ' ':
        space_2.append(i)
plain_text_part_2.replace(' ', '')
counter = 0
flag = False
for i in range(len(plain_text_part_2)):
    for j in range(len(alphabit)):
        if plain_text_part_2[i] == alphabit[j]:
            id_plain_text_2.append(j)
            print(j)
            if counter == len(plain_text_part_2):
                flag = True
            break
    if flag:
        break
for i in range(len(id_plain_text_2)):
    temp = alphabit[id_plain_text_2[i] + number_encryption]
    final_list_2.append(temp)
for i in range(len(space_2)):
    final_list_2.insert(space_2[i], ' ')
answer_final_2 = ''
for i in range(len(final_list_2)):
    answer_final_2 += final_list_2[i]
print('SECOND LAYWER ANSWER: {}'.format(answer_final_2))
print('FIRST LAYWER ENCRYPTION DONE!  2/2')

#Decryption part:   1/2
print('Decryption part:   1/2')
decrypted_word_2 = answer_final_2
decrypted_number_2 = number_encryption
decrypted_space_location = []
decrypted_word_finaly_2 = []
decrypted_word_list_2 =[]
decrypted_id_word_list_2 =[]

for i in range(len(decrypted_word_2)):
    if decrypted_word_2[i] == ' ':
        decrypted_space_location.append(i)
decrypted_word_2.replace(" ", '')
for i in range(len(decrypted_word_2)):
    decrypted_word_list_2.append(decrypted_word_2[i])

counter = 0
flag = False
for i in range(len(decrypted_word_list_2)):
    for j in range(len(alphabit)):
        if decrypted_word_list_2[i] == alphabit[j]:
            decrypted_id_word_list_2.append(j)
            print(j)
            counter += 1
            if counter == len(decrypted_word_list_2):
                flag = True
            break
    if flag:
        break
for i in range(len(decrypted_id_word_list_2)):
    decrypted_temp_2 = alphabit[26 + decrypted_id_word_list_2[i] - decrypted_number_2]
    decrypted_word_finaly_2.append(decrypted_temp_2)
print(decrypted_word_finaly_2)

for i in range(len(decrypted_space_location)):
    decrypted_word_finaly_2.insert(decrypted_space_location[i], ' ')

decrypted_finaly_answer_2 = ''
for i in range(len(decrypted_word_finaly_2)):
    decrypted_finaly_answer_2 += decrypted_word_finaly_2[i]
print(decrypted_finaly_answer_2)
#Decryption part:   2/2
print('Decryption part:   2/2')

decrypted_word_3 = decrypted_finaly_answer_2
decrypted_cypher_3 = cypher_text
decrypted_cypher_list_3 = []
decrypted_word_list_3 = []
decrypted_space_location_3 = []
decrypted_id_cypher_list_3 = []
decrypted_id_word_list_3 = []
decrypted_word_finaly_3 = []


for i in range(len(decrypted_word_3)):
    if decrypted_word_3[i] == ' ':
        decrypted_space_location_3.append(i)
decrypted_word_3.replace(' ', '')
counter = 0
flag = False
for i in range(len(decrypted_word_3)):
    for j in range(len(alphabit)):
        if decrypted_word_3[i].lower() == alphabit[j]:
            decrypted_id_word_list_3.append(j)
            counter += 1
            if counter == len(decrypted_word_3):
                flag = True
            break
    if flag:
        break

for i in range(len(decrypted_word_3)):
    temp = i % len(decrypted_cypher_3)
    decrypted_cypher_list_3.append(decrypted_cypher_3[temp])

counter = 0
flag = False
for i in range(len(decrypted_cypher_list_3)):
    for j in range(len(alphabit)):
        if decrypted_cypher_list_3[i].lower() == alphabit[j]:
            decrypted_id_cypher_list_3.append(j)
            counter += 1
            if counter == len(decrypted_cypher_list_3):
                flag = True
            break
    if flag:
        break
for i in range(len(decrypted_id_word_list_3)):
    decrypted_temp_3 = alphabit[26 + decrypted_id_word_list_3[i] - decrypted_id_cypher_list_3[i]]
    decrypted_word_finaly_3.append(decrypted_temp_3)
print(decrypted_word_finaly_3)

for i in range(len(decrypted_space_location_3)):
    decrypted_word_finaly_3.insert(decrypted_space_location_3[i], ' ')

decrypted_finaly_answer_3 =''
for i in range(len(decrypted_word_finaly_3)):
    decrypted_finaly_answer_3 += decrypted_word_finaly_3[i]

print(decrypted_finaly_answer_3)
print(decrypted_space_location_3)
print('FINALY DONE!  2/2')