def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI based on standard categories."""
    if bmi < 16.0:
        return "Underweight (Severe Thinness)"
    elif 16.0 <= bmi < 17.0:
        return "Underweight (Moderate Thinness)"
    elif 17.0 <= bmi < 18.5:
        return "Underweight (Mild Thinness)"
    elif 18.5 <= bmi < 25.0:
        return "Normal weight"
    elif 25.0 <= bmi < 30.0:
        return "Overweight (pre-obese)"
    elif 30.0 <= bmi < 35.5:
        return "Obesity (Class I)"
    elif 35.5 <= bmi < 40.0:
        return "Obesity (Class II)"
    else:
        return "Obesity (Class III)"

def main():
    try:
        
        print("Welcome to BMI Calculator..!")
        name = str(input("Enter your Name: "))
        print(f"Hello ,{name}")
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

       
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

   
        bmi = calculate_bmi(weight, height)

        
        category = classify_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Dear {name} , You are classified as: {category}")
        print("Thank You for using BMI Calculator..!")

    except ValueError:
        print("Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()
