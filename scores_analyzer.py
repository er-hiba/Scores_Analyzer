# This program allows users to input scores for multiple students across various subjects.
# It then calculates and displays statistics including the mean score of each student,
# and the minimum and maximum score of each subject based on the entered scores.


# Function to calculate and display mean scores for each student
def calculate_mean_scores(matrix):
    for i in range(rows):                                                      # Iterate through each student (row) in the matrix
        sum_scores = 0                                                         # Initialize sum_scores for each student
        for j in range(cols):                                                  # Iterate through each subject (column) for the current student
            sum_scores += matrix[i][j]                                         # Accumulate the scores for the current student
        mean_score = sum_scores / cols                                         # Calculate the mean score for the current student
        print(f"- The mean score for Student n°{i+1} is {mean_score}")         # Display the mean score for each student


# Function to calculate and display minimum score for each subject
def calculate_min_scores(matrix):
    for j in range(cols):                                                          # Iterate through each subject (column) in the matrix
        min_score_subject = matrix[0][j]                                           # Initialize the minimum score for the current subject with the first student's score
        for i in range(rows):                                                      # Iterate through each student (row) in the matrix
            min_score_subject = min(min_score_subject, matrix[i][j])               # Update the minimum score if found lower
        print(f"- The minimum score for Subject n°{j+1} is {min_score_subject}")   # Display the minimum score for each subject


# Calculate and display maximum score for each subject
def calculate_max_scores(matrix):
    for j in range(cols):                                                          # Iterate through each subject (column) in the matrix
        max_score_subject = matrix[0][j]                                           # Initialize the maximum score for the current subject with the first student's score 
        for i in range(rows):                                                      # Iterate through each student (row) in the matrix 
            max_score_subject = max(max_score_subject, matrix[i][j])               # Update the maximum score if found higher
        print(f"- The maximum score for Subject n°{j+1} is {max_score_subject}")   # Display the maximum score for each subject


# Main program

# Ask the user for the number of rows (students)
rows = int(input("Enter the number of students: "))

# Ask the user for the number of columns (subjects)
cols = int(input("Enter the number of subjects: "))

# Initialize a 2D array where scores will be stored
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

# Input scores for each student and subject
for i in range(rows):
    print(f"\nEnter the scores of Student n°{i+1}: ")
    for j in range(cols):
        matrix[i][j] = float(input())

# Calculate and display statistics for mean, minimum, and maximum scores
print("\n")
calculate_mean_scores(matrix)
print("\n")
calculate_min_scores(matrix)
print("\n")
calculate_max_scores(matrix)
