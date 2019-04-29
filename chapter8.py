# Write a course_grader function that takes a list of test scores as its parameter. It will add up these test scores and calculate an average score. It should then return a message of "pass" or "fail" depending on these two conditions:
#
# If the average score is greater than or equal to 70 and no single test score is below 50, then return a message of "pass".
# If the average score is lower than 70 or at least one test score is below 50, then return a message of "fail".
# Some sample function calls with comments on what should be printed out are included in main for testing purposes.

def course_grader(test_scores):
    average = sum(test_scores) / len(test_scores)
    if average < 70:
        return("fail")
    else:
        i = 0
        while test_scores:
            i += 1
            if test_scores[i] < 49:
                return ("fail")
                break
            else:
                return("pass")




# import code; code.interact(local=dict(globals(), **locals()))
