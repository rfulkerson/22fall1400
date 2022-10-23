# Which of the following can be added in the space below to help correct this mistake?

spell = 'incomprehensibilities'
score = 0

answer = input('21-letter word meaning impossible to comprehend: ')
while len(answer) != len(spell):
    answer = input('21-letter word meaning impossible to comprehend: ')
    
for i in range(len(spell)):
    if answer[i] == spell[i]:
        score += 1

print(score)

