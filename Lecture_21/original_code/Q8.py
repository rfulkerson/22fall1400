def check(word):
    result = True
    for w in word:
        if not w.isalnum():
            result = False
    return result

print(check("h2o"), end=' ')
print(check("O'Malley"), end=' ')
print(check("TeAgAn"))

# Or, the much easier ....
print("h2o".isalnum())
print("O'MALLEY".isalnum())
print("tEaGaN".isalnum())


