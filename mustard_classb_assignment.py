#Assignment 1


def calculate_average(scores_list):
    total = 0

    for score in scores_list:
        total += score

    average = total / len(scores_list)
    return average

def get_grade(average):
    if average >= 70:
        return "A - Excellent"
    elif average >= 60:
        return "B - Very Good"
    elif average >= 50:
        return "C - Good"
    elif average >= 45:
        return "D - Fair"
    elif average >= 40:
        return "E - Pass"
    else:
        return "F - Fail"

def rank_students(student_data):

    results = []
    for name, scores in student_data:
        average = calculate_average(scores)
        grade = get_grade(average)

        results.append([name, average, grade])

    for i in range(len(results)):
        for j in range(i + 1, len(results)):
            if results[j][1] > results[i][1]:
                results[i], results[j] = results[j], results[i]

    print("\n📊 STUDENT PERFORMANCE RANKING")
    print("-" * 60)
    print(f"{'Pos':<5}{'Name':<15}{'Average':<12}{'Grade'}")
    print("-" * 60)

    position = 1

    for student in results:
        print(f"{position:<5}{student[0]:<15}{student[1]:<12.2f}{student[2]}")
        position += 1

students = [
    ("John", [75, 80, 70, 85]),
    ("Mary", [90, 88, 92, 95]),
    ("David", [60, 65, 58, 62]),
    ("Sarah", [78, 72, 80, 76]),
    ("Peter", [45, 50, 48, 42])
]

rank_students(students)

#Assignment 2


def analyze_text_sentiment(text):
    positive_words = {
        "good", "great", "happy", "excellent", "love",
        "awesome", "wonderful", "amazing", "fantastic", "success"
    }

    negative_words = {
        "bad", "sad", "hate", "terrible", "awful",
        "poor", "angry", "failure", "worst", "problem"
    }

    words = text.lower().split()

    positive_count = 0
    negative_count = 0
    vowels = 0
    consonants = 0
    vowel_run_found = False

    for word in words:
        cleaned_word = ""

        for char in word:
            if char.isalpha():
                cleaned_word += char

        if cleaned_word in positive_words:
            positive_count += 1
        elif cleaned_word in negative_words:
            negative_count += 1

    current_vowel_run = 0

    for char in text.lower():
        if char.isalpha():

            if char in "aeiou":
                vowels += 1
                current_vowel_run += 1

                if current_vowel_run >= 3:
                    vowel_run_found = True
            else:
                consonants += 1
                current_vowel_run = 0
        else:
            current_vowel_run = 0

    sentiment_score = positive_count - negative_count

    return {
        "Positive Words": positive_count,
        "Negative Words": negative_count,
        "Vowels": vowels,
        "Consonants": consonants,
        "Vowel Run Found": vowel_run_found,
        "Sentiment Score": sentiment_score
    }

def compare_texts(text1, text2):
    result1 = analyze_text_sentiment(text1)
    result2 = analyze_text_sentiment(text2)

    print("\n--- TEXT 1 ANALYSIS ---")
    for key, value in result1.items():
        print(f"{key}: {value}")

    print("\n--- TEXT 2 ANALYSIS ---")
    for key, value in result2.items():
        print(f"{key}: {value}")

    print("\n--- COMPARISON RESULT ---")

    if result1["Sentiment Score"] > result2["Sentiment Score"]:
        print("Text 1 is more positive.")
    elif result2["Sentiment Score"] > result1["Sentiment Score"]:
        print("Text 2 is more positive.")
    else:
        print("Both texts have the same sentiment score.")

song_lyrics = """
I love this beautiful day,
everything feels great and amazing.
"""

motivational_quote = """
Success comes to those who work hard.
Believe in yourself and achieve great things.
"""

complaint_message = """
This service is terrible and awful.
I hate the poor customer support.
"""

print("========== SONG LYRICS ==========")
song_result = analyze_text_sentiment(song_lyrics)
for key, value in song_result.items():
    print(f"{key}: {value}")

print("\n========== MOTIVATIONAL QUOTE ==========")
quote_result = analyze_text_sentiment(motivational_quote)
for key, value in quote_result.items():
    print(f"{key}: {value}")

print("\n========== COMPLAINT MESSAGE ==========")
complaint_result = analyze_text_sentiment(complaint_message)
for key, value in complaint_result.items():
    print(f"{key}: {value}")


print("\n\nCOMPARING SONG LYRICS AND COMPLAINT MESSAGE")
compare_texts(song_lyrics, complaint_message)

print("\n\nCOMPARING MOTIVATIONAL QUOTE AND COMPLAINT MESSAGE")
compare_texts(motivational_quote, complaint_message)



#Assignment 3


def print_pattern_table(n):

    print("\nMULTIPLICATION TABLES FROM 1 TO", n)
    print("-" * 40)
    for i in range(1, n + 1):
        print("\nTable of", i)

        for j in range(1, 11):
            result = i * j
            if result % 3 == 0 or result % 5 == 0 or result % 7 == 0:
                print(i, "x", j, "=", str(result) + " *")
            else:
                print(i, "x", j, "=", result)

    print("\nTRIANGLE PATTERN")
    print("-" * 40)

    for row in range(1, n + 1):
        for col in range(row):
            print("*", end=" ")
        print()

print_pattern_table(10)
print("\n" + "=" * 50)
print_pattern_table(15)


#Assignment 4


def validate_credentials(username, password):
    results = {
        "username_valid": True,
        "password_valid": True,
        "errors": []
    }

    if len(username) < 6:
        results["username_valid"] = False
        results["errors"].append("Username must be at least 6 characters long.")

    if " " in username:
        results["username_valid"] = False
        results["errors"].append("Username must not contain spaces.")

    if not username[0].isalpha():
        results["username_valid"] = False
        results["errors"].append("Username must start with a letter.")

    uppercase = 0
    lowercase = 0
    digits = 0
    special = 0

    for char in password:

        if char.isupper():
            uppercase += 1

        elif char.islower():
            lowercase += 1

        elif char.isdigit():
            digits += 1

        else:
            special += 1


    if len(password) >= 8:

        if uppercase > 0:

            if lowercase > 0:

                if digits > 0:

                    if special > 0:
                        pass

                    else:
                        results["password_valid"] = False
                        results["errors"].append(
                            "Password must contain at least one special character."
                        )

                else:
                    results["password_valid"] = False
                    results["errors"].append(
                        "Password must contain at least one digit."
                    )

            else:
                results["password_valid"] = False
                results["errors"].append(
                    "Password must contain at least one lowercase letter."
                )

        else:
            results["password_valid"] = False
            results["errors"].append(
                "Password must contain at least one uppercase letter."
            )

    else:
        results["password_valid"] = False
        results["errors"].append(
            "Password must be at least 8 characters long."
        )

    return results

def generate_suggestions(password):

    suggestions = []

    if len(password) < 8:
        suggestions.append("Increase password length to at least 8 characters.")

    if not any(char.isupper() for char in password):
        suggestions.append("Add at least one uppercase letter.")

    if not any(char.islower() for char in password):
        suggestions.append("Add at least one lowercase letter.")

    if not any(char.isdigit() for char in password):
        suggestions.append("Add at least one digit.")

    if not any(not char.isalnum() for char in password):
        suggestions.append("Add at least one special character.")

    if not suggestions:
        suggestions.append("Excellent password! No improvements needed.")

    return suggestions

test_data = [
    ("mustard", "Pass123!"),          
    ("blueboy", "Pass123!"),      
    ("chiamaka chidi", "Pass123!"),    
    ("scepter123", "password"),       
    ("tegah01", "Password1"),      
    ("Michael7", "Strong@123")   
]

for username, password in test_data:

    print("=" * 60)
    print(f"Username: {username}")
    print(f"Password: {password}")

    result = validate_credentials(username, password)

    print("\nValidation Result:")
    print(result)

    if not result["password_valid"]:
        print("\nSuggestions:")
        for tip in generate_suggestions(password):
            print("-", tip)

    print()