score_list = []; # do not forget to declare a list
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    
    score_list.append([name, score])
second_highest = sorted(set([score for name, score in score_list]))[1]
print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))

