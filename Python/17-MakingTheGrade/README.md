# Instructions

You're a teaching assistant correcting student exams. Keeping track of results manually is getting both tedious and mistake-prone. You decide to make things a little more interesting by putting together some functions to count and calculate results for the class.

## 1. Rounding Scores

While you can give "partial credit" on exam questions, overall exam scores have to be ints. So before you can do anything else with the class scores, you need to go through the grades and turn any float scores into ints. Lucky for you, Python has the built-in round() function you can use.

A score of 75.45 or 75.49 will round to 75. A score of 40.50 will round to 40. A score of 43.50 (or above) will round to 44. There shouldn't be any scores that have more than two places after the decimal point.

Create the function round_scores() that takes a list of student_scores. This function should consume the input list and return a new list with all the scores converted to ints. The order of the scores in the resulting list is not important.

## 2. Non-Passing Students

As you were grading the exam, you noticed some students weren't performing as well as you'd hoped. But you were distracted, and forgot to note exactly how many students.

Create the function count_failed_students() that takes a list of student_scores. This function should count up the number of students who don't have passing scores and return that count as an integer. A student needs a score greater than 40 to achieve a passing grade on the exam.

## 3. The "Best"

The teacher you're assisting wants to find the group of students who've performed "the best" on this exam. What qualifies as "the best" fluctuates, so you need to find the student scores that are greater than or equal to the current threshold.

Create the function above_threshold() taking student_scores (a list of grades), and threshold (the "top score" threshold) as parameters. This function should return a list of all scores that are >= to threshold.

## 4. Calculating Letter Grades

The teacher you're assisting likes to assign letter grades as well as numeric scores. Since students rarely score 100 on an exam, the "letter grade" lower thresholds are calculated based on the highest score achieved, and increment evenly between the high score and the failing threshold of <= 40.

Create the function letter_grades() that takes the "highest" score on the exam as a parameter, and returns a list of lower score thresholds for each "American style" grade interval: ["D", "C", "B", "A"].

## 5. Matching Names to Scores

You have a list of exam scores in descending order, and another list of student names also sorted in descending order by their exam scores. You would like to match each student name with their exam score and print out an overall class ranking.

Create the function student_ranking() with parameters student_scores and student_names. Match each student name on the student_names list with their score from the student_scores list. You can assume each argument list will be sorted from highest score(er) to lowest score(er). The function should return a list of strings with the format < rank  >. < student name >: < student score >.

## 6. A "Perfect" Score

Although a "perfect" score of 100 is rare on an exam, it is interesting to know if at least one student has achieved it.

Create the function perfect_score() with parameter student_info. student_info is a list of lists containing the name and score of each student: [["Charles", 90], ["Tony", 80]]. The function should return the first [< name >, < score >] pair of the student who scored 100 on the exam.

If no 100 scores are found in student_info, an empty list [] should be returned.
