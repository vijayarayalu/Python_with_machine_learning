""" Question 3: User Age Verification and Log File Management 
Steps: 
1. Define a custom exception UnderageError for age verification failures. 
2. Implement verify_age(age):  
o If age < 18, raise UnderageError. 
o Otherwise, print a success message. 
3. Implement log_error(error_message):  
o Open error.log in append mode. 
o Write the error message. 
o Handle IOError. 
Example: 
verify_age(16)  # Should raise UnderageError"""

class UnderageError(Exception):
    def __init__(self, message="User is underage. Access denied."):
        super().__init__(message)

# Step 2: Define a function to verify age
def verify_age(age):
    try:
        if age < 18:
            raise UnderageError()
        print("Age verification successful. Access granted.")
    except UnderageError as e:
        print(f"Error: {e}")
        log_error(str(e))

# Step 3: Define a function to log errors
def log_error(error_message):
    try:
        with open("error.log", "a") as file:
            file.write(error_message + "\n")
    except IOError:
        print("Failed to write to log file.")

# Example Usage
verify_age(16)
verify_age(56)