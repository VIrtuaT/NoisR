from math import erfc, sqrt
import matplotlib.pyplot as plt

def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read().replace('\n', '')  
            return data.strip()  
    except FileNotFoundError:
        return "File not found."

def convert_to_string(data):

    lines = data.split('\n')  
    binary_string = ''.join(lines)  
    return binary_string

teste = read_txt_file("seq1.txt")
print(teste)

def plot_histogram(int_list):
    plt.hist(int_list, bins=max(int_list)-min(int_list)+1,align="left", edgecolor="black") #(esta linha pertence a de cima)
    plt.xlabel("Integers")
    plt.ylabel("Frequency")
    plt.title("Histogram of Integers")
    plt.grid(True)
    plt.show()
    plot_histogram(int_list)
# Obrigado ChatGPT!

n = len(teste)
s_n = 0
binary_int_list =[]
decimal_int_list = []
for i in range(n):
    if teste[i] == 1:
        s_n += 1
    if teste[i] == 0:
        s_n -= 1
    
    binary_int_list.append(int(teste[i]))

    if len(binary_int_list) == 6:
        num = binary_int_list[0] * 2**5 + binary_int_list[1] * 2**4 +binary_int_list[2] * 2**3 +binary_int_list[3] * 2**2 +binary_int_list[4] * 2**1 +binary_int_list[5] * 2**0
        binary_int_list.clear()
        decimal_int_list.append(num)
    

s_obs = abs(s_n)/sqrt(n)
p_value = erfc(s_obs/sqrt(2))
print(p_value)
print(s_n)

int_list = list(teste)
plot_histogram(decimal_int_list)
#o grafico é MUITO diferente da distribuição normal (bom senso).