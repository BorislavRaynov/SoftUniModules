grade_data = float(input())


def grades(grade):
    if 2.00 <= grade <= 2.99:
        return "Fail"
    elif 2.99 <= grade <= 3.49:
        return "Poor"
    elif 3.50 <= grade <= 4.49:
        return "Good"
    elif 4.50 <= grade <= 5.49:
        return "Very Good"
    elif 5.50 <= grade <= 6.00:
        return "Excellent"


print(grades(grade_data))
