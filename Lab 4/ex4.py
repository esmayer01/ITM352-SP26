# Try to append a tuple. It won't work!
# Name: Ethan Mayer
# Date: Jan. 29, 2026

survey_respondents = (1012, 1035, 1021, 1053)
print("Original survey respondents tuple:", survey_respondents)
# survey_respondents.append(1054)  # This will raise an AttributeError
survey_respondents = survey_respondents + (1054,)
print("Updated survey respondents tuple:", survey_respondents)