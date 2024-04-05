import sys

key = [0,1,1,0,0,0,0,1,
       0,0,1,0,0,0,0,0,
       0,0,0,0,0,0,0,0,
       1,0,1,1,0,0,1,0,
       0,0,0,1,1,1,1,1,
       0,1,1,0,0,1,1,1,
       1,0,1,0,1,1,1,1,
       1,0,1,1,1,1,1,1
       ]
key56 = []
key48 = []
keyL = []
keyR = []
shift_keyL = []
shift_keyR = []
initial_permutation = [
                        58,50,42,34,26,18,10,2,
                        60,52,44,36,28,20,12,4,
                        62,54,46,38,30,22,14,6,
                        64,56,48,40,32,24,16,8,
                        57,49,41,33,25,17,9,1,
                        59,51,43,35,27,19,11,3,
                        61,53,45,37,29,21,13,5,
                        63,55,47,39,31,23,15,7
                        ]
inverse_initial_permutation = [
                                [10,8,48,16,56,24,64,32],
                                [39,7,47,15,55,23,63,31],
                                [38,6,46,14,54,22,62,30],
                                [37,5,45,13,53,21,61,29],
                                [36,4,44,12,52,20,60,28],
                                [35,3,43,11,51,19,59,27],
                                [34,2,42,10,50,18,58,26],
                                [33,1,41,9,49,17,57,25]
                                ]
final_permutation = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]
initial_32_permutation =[15,6,19,20,
                         28,11,27,16,
                         0,14,22,25,
                         4,17,30,9,
                         1,7,23,13,
                         31,26,2,8,
                         18,12,29,5,
                         21,10,3,24]
permuted_choice_1 = [57,49,41,33,25,17,9,
                     1,58,50,42,34,26,18,
                     10,2,59,51,43,35,27,
                     19,11,3,60,52,44,36,
                     63,55,47,39,31,23,15,
                     7,62,54,46,38,30,22,
                     14,6,61,53,45,37,29,
                     21,13,5,28,20,12,4
                     ]
permuted_choice_2 = [14,17,11,24,1,5,
                     3,28,15,6,21,10,
                     23,19,12,4,26,8,
                     16,7,27,20,13,2,
                     41,52,31,37,47,55,
                     30,40,51,45,33,48,
                     44,49,39,56,34,53,
                     46,42,50,36,29,32]
reverse_round_keys = []
plaintext = []
half_plaintext_a = []
half_plaintext_b = []
ciphertext = []
bin_plaintext = []
integer_plaintext = []
integer_plaintexts = []
sub_integer_plaintexts=[]
permutation = []
sub_expention = []
sub_sub_expention = []
expansion = []
xortext = []
S_BOX = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]
# key를 좌측으로 시프트하는 함수
def Left_shift(arr, shift):
    shift %= len(arr)  # 시프트 값이 배열 길이보다 큰 경우를 처리
    return arr[shift:] + arr[:shift]
#이진수를 글자화
def binary_to_ascii(binary_list):
    try:
        byte_list = [binary_list[i:i+8] for i in range(0, len(binary_list), 8)]
        ascii_string = ''.join([chr(int(''.join(map(str, byte)), 2)) for byte in byte_list])
       
        return ascii_string
    except ValueError:
        return "not binary"
#숫자를 떼어내는 작업
def binary(arr):
    integer_plaintexts = []
    subs = []
    for x in arr:
        sub = list(x)
        integer_plaintexts.append(sub)
    for row in integer_plaintexts:
        for element in row:
            subs.append(element)
    integer = [int(x) for x in subs]
    return integer
#이진화
def binary_painting(arr):
    subs = []
    for x in arr:
        sub = bin(x)
        sub = sub[2:]
        result = sub.zfill(4)
        subs.append(result)
    return subs
#반으로 나누기
def split(plaintext):
    index = len(plaintext)//2
    half_plaintext_a = plaintext[:index]
    half_plaintext_b = plaintext[index:]
   
    return half_plaintext_a, half_plaintext_b
#아스키 코드로 변환
def f_ascii_code(arr):
    ascii_codes = []
    for char in arr:
        ascii_code = format(ord(char), '08b')  # 문자를 아스키 코드로 변환
        ascii_codes.append(ascii_code)
   
    binary_strings = [ascii_code for ascii_code in ascii_codes]    # 아스키 코드 리스트를 이진수로 변환하여 저장
    return binary_strings
#2차원 배열을 1차원 배열로 변환
def one_dimension(array):
    flat_array = []
    for item in array:
        if isinstance(item, list):
            flat_array.extend(item)
        else:
            flat_array.append(item)
    return flat_array
#Expansion
def Expansion(arr):
    sub_expention = []
    sub_sub_expention = []
    one_expansion = []
    sub_expention = [arr[i:i+4] for i in range(0, len(arr) , 4)]

    j = 0
    for i in range(len(sub_expention)):
        if (i == 0):
            sub_sub_expention.append(arr[31])
            sub_sub_expention.append(sub_expention[i])
            sub_sub_expention.append(arr[j+4])
            j = j+3
        elif (i == 7):
            sub_sub_expention.append(arr[j])
            sub_sub_expention.append(sub_expention[i])
            sub_sub_expention.append(arr[0])
        else :
            sub_sub_expention.append(arr[j])
            sub_sub_expention.append(sub_expention[i])
            sub_sub_expention.append(arr[j+5])
            j= j+4

    one_expansion = one_dimension(sub_sub_expention)
    return one_expansion
#평문 64비트 확인 및 추가
def first_Check(arr):
    array = []
    if (len(arr) > 8):
        print("Plaintext is greater than 64 bits.")
        exit(1)
    if (len(arr) < 8):
        a = len(arr)
        for i in range(8-a):
            arr += '\0'
    for char in arr:
        array.append(char)
    return array
#key_permutation_1
def key_permuted_1(arr):
    sub_arr = []
    for i in range(len(permuted_choice_1)):
        index = permuted_choice_1[i]-1
        sub_arr.append(arr[index])
    return sub_arr
#key_permutation_2
def key_permuted_2(arr):
    sub_arr = []
    for i in range(len(permuted_choice_2)):
        index = permuted_choice_2[i]-1
        sub_arr.append(arr[index])
    return sub_arr
def reverse_key (arr,i):
    sub = arr[i]
    sub = key_permuted_2(sub)
    return sub
#key_left_shift
def left_shift(arr):
    sub_arr = []
    for i in range(len(arr)-1):
        sub_arr.append(arr[i+1])
    sub_arr.append(arr[0])
    return sub_arr
#key를 48로 합치는 작업
def key_48(arrL, arrR):
    sub = []
    sub.append(arrL)
    sub.append(arrR)
    one_dimension(sub)
    return sub
#XOR
def xor(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Arrays must have the same length for XOR operation.")
    result = []
    for i in range(len(arr1)):
        bit1 = int(arr1[i])
        bit2 = int(arr2[i])
        xor_result = bit1 ^ bit2
        result.append(xor_result)
   
    return result
#S-BOX
def s_box(arr):
    array = []
    subs = [arr[i:i+6]for i in range(0,len(arr),6)]
    for i in range(len(S_BOX)):
        a_box = S_BOX[i]    
        sub = subs[i]
        if sub[0]==0 and sub[5]==0:
            row = 0
        elif sub[0]==0 and sub[5]==1:
            row = 1
        elif sub[0]==1 and sub[5]==0:
            row = 2
        elif sub[0]==1 and sub[5]==1:
            row = 3
        b_box = a_box[row]
        new = sub[1:6]
        if new[0]==0 and new[1]==0 and new[2]==0 and new[3]==0:
            cal = 0
        elif new[0]==0 and new[1]==0 and new[2]==0 and new[3]==1:
            cal = 1
        elif new[0]==0 and new[1]==0 and new[2]==1 and new[3]==0:
            cal = 2
        elif new[0]==0 and new[1]==0 and new[2]==1 and new[3]==1:
            cal = 3
        elif new[0]==0 and new[1]==1 and new[2]==0 and new[3]==0:
            cal = 4
        elif new[0]==0 and new[1]==1 and new[2]==0 and new[3]==1:
            cal = 5
        elif new[0]==0 and new[1]==1 and new[2]==1 and new[3]==0:
            cal = 6
        elif new[0]==0 and new[1]==1 and new[2]==1 and new[3]==1:
            cal = 7
        elif new[0]==1 and new[1]==0 and new[2]==0 and new[3]==0:
            cal = 8
        elif new[0]==1 and new[1]==0 and new[2]==0 and new[3]==1:
            cal = 9
        elif new[0]==1 and new[1]==0 and new[2]==1 and new[3]==0:
            cal = 10
        elif new[0]==1 and new[1]==0 and new[2]==1 and new[3]==1:
            cal = 11
        elif new[0]==1 and new[1]==1 and new[2]==0 and new[3]==0:
            cal = 12
        elif new[0]==1 and new[1]==1 and new[2]==0 and new[3]==1:
            cal = 13
        elif new[0]==1 and new[1]==1 and new[2]==1 and new[3]==0:
            cal = 14
        elif new[0]==1 and new[1]==1 and new[2]==1 and new[3]==1:
            cal = 15
        array.append(b_box[cal])
    array = binary_painting(array)
    array = binary(array)
    return array
#32bit permutation
def permutation_32(arr):
    sub =[]
    for index in initial_32_permutation:
        sub.append(arr[index])
    return sub
#key 를 뒤집는 함수
def reverse_subkeys(round_keys):
    return round_keys[::-1]
#복호화 permutation
def reverse_permutation(input_array, permutation_array):
    inverse_permutation = [0] * len(permutation_array)
    for i in range(len(permutation_array)):
        inverse_permutation[permutation_array[i] - 1] = i + 1

    repermutation = [0] * len(input_array)
    for i in range(len(input_array)):
        index = inverse_permutation[i] - 1
        repermutation[i] = input_array[index]

    return repermutation
#main
user_input = input("plaintext: ")

#평문 64비트 확인 및 추가
plaintext = first_Check(user_input)

#아스키 코드/바이너리화
bin_plaintext = f_ascii_code(plaintext)
integer_plaintext = binary(bin_plaintext)
print(f"integer_plaintext: {integer_plaintext}")

#permutation
permutation = [0] * len(integer_plaintext)
for i in range(len(integer_plaintext)):
    index = initial_permutation[i] - 1  # initial_permutation의 값을 인덱스로 사용
    permutation[i] = integer_plaintext[index]
print(f"permutation {permutation}")
#반으로 나누기
half_plaintext_a, half_plaintext_b = split(permutation)

#key
key56 = key_permuted_1(key)
keyL, keyR = split(key56)
#Round1
for k in range(16):
    keyL = left_shift(keyL)
    keyR = left_shift(keyR)
    key48_sub = key_48(keyL,keyR)
    sub_key48 = one_dimension(key48_sub)
    key48 = key_permuted_2(sub_key48)
    reverse_round_keys.append(sub_key48)
    print(f"Round {k+1}")
    print("-------------Expention-------------")
    expansion = Expansion(half_plaintext_b)
    print(f"expansion {expansion}")
    print("-------------XOR-------------------")
    xortext = xor(expansion,key48)
    print(f"xor {xortext}")
    print("-------------S-BOX-------------------")
    boxing = s_box(xortext)
    print(f"S-BOX {boxing}")
    text = permutation_32(boxing)
    nexttext = xor(half_plaintext_a, text)
    half_plaintext_a = half_plaintext_b
    half_plaintext_b = nexttext
    print("")
   

#라운드 종료 이후
ciphertext.append(half_plaintext_a)
ciphertext.append(half_plaintext_b)
ciphertext = binary(ciphertext)
cipherstring = binary_to_ascii(ciphertext)
print(f"ciphertext: {cipherstring}")
#복호화
# 초기 변수 설정
half_ciphertext_a, half_ciphertext_b = split(ciphertext)
half_ciphertext_a, half_ciphertext_b = half_ciphertext_b, half_ciphertext_a

help_arr = []
    # 라운드 키 역순으로 사용
for j in range(len(reverse_round_keys)):
    sub = reverse_key(reverse_round_keys,j)
    help_arr.append(sub)
round_keys = reverse_subkeys(help_arr)
    # 라운드 별로 복호화 수행
for k in range(16):
    expansion = Expansion(half_ciphertext_b)
    xortext = xor(expansion, round_keys[k])
    boxing = s_box(xortext)
    text = permutation_32(boxing)
    nexttext = xor(half_ciphertext_a, text)
    half_ciphertext_a = half_ciphertext_b
    half_ciphertext_b = nexttext
# 최종 복호화 결과
replaintext = []
replaintext.append(half_ciphertext_b)
replaintext.append(half_ciphertext_a)
replaintext = binary(replaintext)
replaintext = reverse_permutation(replaintext, initial_permutation)
replaintext = binary_to_ascii(replaintext)
print(f"Decrypted plaintext: {replaintext}")