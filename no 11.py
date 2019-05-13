for i in range(100,1000):
    for j in range(100,1000):
        answer = str(i * j)
        if answer == answer[::-1]:
            final_answer = answer

print(final_answer)