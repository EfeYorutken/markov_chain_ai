import random as r
import codecs

def compute_text(dic : dict[str, dict[str,int]], current_word : str, step : int) -> str:
    if step == 0:
        return "."
    if current_word not in dic:
        keys = list(dic.keys())
        return compute_text(dic,r.choice(keys), step)
    mini = dic[current_word]
    list_of_vals = list(mini.values())
    max_int = max(list_of_vals)
    rint = r.randint(0,max_int-1)
    next_word = ""
    smallest_dif = 999

    total_weight = sum(mini.values())
    rand_val = r.uniform(0,total_weight)

    current_weight = 0
    for key,weight in mini.items():
        current_weight += weight
        if rand_val < current_weight:
            next_word = key
    return next_word + " " +compute_text(dic,next_word,step-1)


def generate(example_text : str, output_length : int) -> str:

    transition : dict[str, dict[str,int]] = {}
    
    example_arr = example_text.split(" ")
    
    for i in range(len(example_arr) - 1):
        current_word = example_arr[i]
        next_word = example_arr[i+1]
    
        if current_word not in transition:
            transition[current_word] = {next_word : 1}
        else:
            if next_word not in transition[current_word]:
                transition[current_word] = {next_word:1}
            else:
                transition[current_word][next_word] += 1
    
    first_word = r.choice(list(transition.keys()))
    
    output = compute_text(transition,first_word,output_length)
    return output

file_content = ""
with codecs.open("test.txt", "r", encoding="utf-8") as f:
    file_content = f.readlines()

#with open("test.txt", "r", encoding) as f:
#    file_content = f.readlines()

output = generate(file_content[0], 200).replace("\n","\n.")
print(output)
