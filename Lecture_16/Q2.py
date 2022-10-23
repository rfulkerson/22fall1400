# What will the following code print when the input is 'incomprellion'?

spell = 'incomprehensibilities'
score = 0
answer = input('21-letter word meaning impossible to comprehend: ')
for i in range(len(spell)):
    if answer[i] == spell[i]:
        score += 1
print(score)
