russian = int(input('Enter your Russian language score: '))
math = int(input('Enter your Math score: '))
informatics = int(input('Enter your Informatics score: '))

total_score = russian + math + informatics

if total_score >= 270:
    print('Congratulations! You’ve been admitted with a scholarship!')
else:
    print('Unfortunately, you didn’t qualify for a scholarship.')
