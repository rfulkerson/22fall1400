import time 

password = "JeFf!"

source = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"

found = "N/A - DID NOT FIND PASSWORD"

print(f"Please wait ... trying {len(source)**5:,} passwords ... ")
start = time.perf_counter()
for a in source:
    for b in source:
        for c in source:
            for d in source:
                for e in source:
                    guess = f'{a}{b}{c}{d}{e}'
                    if guess == password:
                        print(f'Your password is {guess}')
                        found = guess
                        found_time = time.perf_counter()

end = time.perf_counter()

print("done!")
print(f'It took {end-found_time:.2f} seconds to find {found}.')
print(f'Total time to check {len(source)**5:,} passwords: {end-start:.2f} seconds.')
