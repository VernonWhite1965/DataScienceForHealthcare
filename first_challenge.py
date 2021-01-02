# Using the variables below, print out to the screen the following:

# "Jane Doe takes propranolol 40 mg 4 times a day. Total dose in one day is 160mg."

name = "Jane Doe"
drug = "propranolol"
dose = 40
unit = "mg"
frequency = 4

# Start below
# Simple Print function

daily_dosage = name + ' takes ' + str(drug) + ' ' + str(dose) + str(unit) \
               + ' times a day. Total dose in one day is ' + str(dose * frequency) \
               + str(unit) + '.'

print(daily_dosage)

# Simple Print function with .format text function

dd_text_format = '{0} takes {1} {2}{3} times a day. Total dose in one day is {4}{5}.'.format(name, str(drug), str(dose),
                                                                                             str(unit),
                                                                                             str(dose * frequency),
                                                                                             str(unit))

print(dd_text_format)


# Function with .format text function then print of return

def daily_dose():
    dd_format = '{0} takes {1} {2}{3} times a day. Total dose in one day is {4}{5}.'.format(name, str(drug),
                                                                                            str(dose),
                                                                                            str(unit),
                                                                                            str(dose * frequency),
                                                                                            str(unit))
    return dd_format


print(daily_dose())
