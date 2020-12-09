with open('resources/day6.data') as file:
    count = 0
    all_count = 0
    group_answers = {}
    persons = 0
    for line in file:
        answers = line[:-1]
        if len(answers) > 0:
            persons += 1
            for a in answers:
                if a in group_answers:
                    group_answers[a] += 1
                else:
                    group_answers[a] = 1
        else:
            print('Answered "yes" to {} questions.'.format(len(group_answers.keys())))
            count += len(group_answers.keys())

            all = 0
            for a in group_answers.keys():
                if group_answers[a] == persons:
                    all += 1
            print('{} persons answered "yes" to {} question.'.format(persons, all))
            all_count += all
            persons = 0
            group_answers = {}
    print('First part: sum of those counts is {}.'.format(count))
    print('Second part: sum of those counts is {}.'.format(all_count))

