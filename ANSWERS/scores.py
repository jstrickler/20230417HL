"""
Module docstring

DRY principle  (Don't Repeat Yourself)

"""
DATA_FILE_PATH = "../DATA/testscores.dat"

def main():
    data = get_data()
    for student, (score, grade) in data.items():
        print("{:20s} {} {}".format(student, score, grade))

    average = get_avg(data)
    print("\naverage score is  {:.2f}\n".format(average))

def compute_grade(score):
    """
    Function docstring
    """
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'
    return grade

def get_data():
    scores_by_student = {}

    with open(DATA_FILE_PATH) as scores_in:

        for line in scores_in:
            name, score = line.split(":")
            score = int(score)
            scores_by_student[name] = (score, compute_grade(score))
    return scores_by_student

def get_avg(data):
    sum_of_scores = sum(score[0] for score in data.values())
    return sum_of_scores/len(data)

if __name__ == "__main__":
    main()

