email = input('Enter Valid Email ID : ')          # Take email input from the user

k, d = 0, 0                                       # k → space flag, d → invalid character flag

if len(email) > 6:                               # Check if email length is greater than 6
    if email[-4] == '.' or email[-3] == '.':     # Check dot position near the end
        if email[0].isalpha():                   # Check if first character is alphabet
            if ('@' in email) and (email.count('@') == 1):  # Check exactly one '@' symbol

                for i in email:                  # Loop through each character in email
                    if i == i.isspace():         # Intended to check for space (logical error)
                        k = 1
                    elif i.isdigit():       # Intended to allow digits (logical error)
                        continue
                    elif i == '_' or i == '@' or '.':  # Intended to allow _, @, . (logical error)
                        continue
                    else:                         # Any other character considered invalid
                        d = 1

                if k == 1 or d == 1:              # Check if any error flag is raised
                    print('❌ Invalid email-5')     # Invalid due to space or character issue
                else:
                    print('you Email is Correct ✅')   # Email considered valid

            else:
                print('❌ Invalid email-4')         # '@' missing or more than one '@'
        else:
            print('❌ Invalid email-3')              # First character is not alphabet
    else:
        print('❌ Invalid Email-2')                  # Dot not in valid position
else:
    print('❌ Invalid Email!1')                      # Email length too short



print('Created by Akash coder.')