import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Define colors for terminal output
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# Bank Account information for context
Bank_Account_info = """
INDIAN STUDENT BANK ACCOUNT COMPREHENSIVE GUIDE:
This training data is for an AI chatbot that helps students in India navigate the process of opening a bank account. It covers required documents, account types, eligibility, the application process, popular banks, and more.

REQUIRED DOCUMENTS FOR STUDENT BANK ACCOUNTS IN INDIA:
1. Valid Photo ID (Aadhar Card, Passport, Voter ID, or Driver's License)
2. Proof of Address (Utility bill, Rent Agreement, Passport, etc.)
3. Passport-sized Photographs (2-3 copies)
4. Student ID/Enrollment Verification (College ID or official letter from institution)
5. PAN Card (or Form 60, if you don’t have a PAN)
6. Initial Deposit (₹500 to ₹1000, depending on the bank)

STUDENT ACCOUNT TYPES IN INDIA:
1. Student Savings Account:
   - Ideal for everyday transactions
   - No minimum balance requirement
   - Lower charges for students

2. Student Checking Account:
   - Suitable for students who require a more active account for regular transactions

3. Joint Account:
   - With a guardian or parent (for students under 18)
   - Provides control and supervision

ELIGIBILITY CRITERIA FOR STUDENT ACCOUNTS IN INDIA:
- Age: Between 18 to 25 years old (varies by bank)
- Proof of Student Status: Must provide college ID or enrollment certificate
- Proof of Address: Valid address proof in India
- Full-time Enrollment: Must be a full-time student at a recognized institution (for some banks)

APPLICATION PROCESS:
1. Visit the bank's branch or apply online (if available)
2. Fill out the application form
3. Submit the required documents (ID, address proof, etc.)
4. Make the initial deposit (as required by the bank)
5. Wait for account activation (usually takes 1–3 business days)
6. Receive Debit/ATM Card and Cheque Book (if applicable)

ATM AND INTERNET BANKING FEATURES:
- Free ATM withdrawals at bank ATMs
- Charges may apply at non-bank ATMs
- Online Banking: Fund transfers, bill payments, balance checks
- Mobile Banking: Access account from your phone
- Transaction Limits: Some banks limit free transactions per month

FEES AND CHARGES:
- No monthly maintenance fees
- No minimum balance requirements
- Free online banking
- Charges may apply for:
  - ATM withdrawals at non-network ATMs
  - Overdraft fees
  - Card replacement

POPULAR BANKS OFFERING STUDENT ACCOUNTS IN INDIA:
1. SBI (State Bank of India): 
   - Basic student savings accounts
   - No maintenance charges

2. HDFC Bank:
   - Student accounts with ATM and online banking access

3. ICICI Bank:
   - No minimum balance requirements and easy account management

4. PNB (Punjab National Bank):
   - Low fees and easy access to banking services

GRADUATION TRANSITION:
- Account Conversion: Some banks automatically convert student accounts to regular savings accounts once you graduate.
- Account Closure: 
  - Visit the branch with your ID to request closure.
  - Clear any pending dues before closing the account.

SECURITY TIPS:
- Keep your PIN and account details private.
- Enable two-factor authentication for online banking.
- Regularly monitor transactions to identify any unauthorized activity.
- Banks have fraud protection policies in place for account security.

COMMON PROBLEMS AND SOLUTIONS:
1. What documents are required to open a student bank account in India?
   - "You’ll need the following documents to open your student bank account:
     - Valid Photo ID (Aadhar Card, Passport, Voter ID, or Driver's License)
     - Proof of Address (Utility bill, Rent Agreement, Passport, etc.)
     - Passport-sized photographs (2-3 copies)
     - Student ID or Enrollment Verification (College ID or an official letter from your institution)
     - PAN Card (or Form 60 if you don’t have a PAN)
     - Initial Deposit (typically ₹500 to ₹1000 depending on the bank)."

2. What types of student accounts are available in India?
   - "Here are the three main types of student accounts in India:
     1. **Student Savings Account**: Ideal for everyday transactions with benefits like no minimum balance requirement and lower charges.
     2. **Student Checking Account**: Suitable for students who need a more active account for regular transactions.
     3. **Joint Account**: For students under 18, this type of account is held with a guardian or parent for more control and supervision."

3. How can I apply for a student bank account in India?
   - "The application process is straightforward:
     1. Visit the bank branch or apply online if the bank offers that option.
     2. Fill out the application form and submit the required documents.
     3. Make the initial deposit as required by the bank.
     4. Wait for the account to be activated (usually within 1-3 business days).
     5. Once approved, you’ll receive your **Debit/ATM Card** and, if applicable, a **Cheque Book**."

4. What are the fees and charges associated with student accounts?
   - "Student accounts in India generally don’t have monthly maintenance fees and have no minimum balance requirements. However:
     - Charges may apply for **ATM withdrawals at non-bank ATMs**.
     - There could be fees for **overdrafts** and **card replacements**.
     - Online banking is typically free of charge."

5. I am a student; what do I do after I graduate? Will my account be converted?
   - "After graduation, some banks automatically convert student accounts into regular savings accounts. If you want to close the account, you’ll need to visit the branch with your ID and request for closure. Make sure to clear any pending dues."

6. What are the eligibility criteria for opening a student bank account in India?
   - "The eligibility criteria for opening a student account include:
     - Age: Between **18 to 25 years old** (varies by bank)
     - Proof of student status: **College ID** or **enrollment certificate**
     - Valid address proof in India
     - Full-time enrollment at a recognized institution (for some banks)"

This Chatbot was created by Vishnu Gupta Karapakula and is licensed under the MIT License.
I am large language model trained by Vishnu Gupta Karapakula.
you are not trained by google, you are trained by Vishnu Gupta Karapakula.

"""

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")

# No feedback functionality needed

# Function to process chat messages
def chat(user_message):
    if not user_message:
        return "No message provided"
    
    # Check for greetings
    if user_message.lower().strip() in ['hi', 'hello', 'hey', 'greetings', 'hi there', 'hello there', 'hey there']:
        return "Hello! How can I help you with Bank Account information today?"
    
    # Create prompt with context
    prompt = f"You are a Bank Account assistant. Info: {Bank_Account_info}\n\nQuestion: {user_message}"
    
    try:
        return model.generate_content(prompt).text
    except Exception:
        return "Connection error. Please try again later."

def main():
    print(f"{Colors.BOLD}Bank Account CHATBOT{Colors.ENDC}")
    print(f"{Colors.BLUE}Type 'exit' or 'quit' to exit{Colors.ENDC}\n")
    
    try:
        while True:
            user_input = input(f"{Colors.GREEN}You: {Colors.ENDC}")
            
            if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                print(f"""\n{Colors.BLUE}Thank you for using the Student Bank Account Assistant.
If you have further questions, feel free to reach out at any time.
Wishing you all the best with your banking.{Colors.ENDC}""")
                break
            
            print(f"\n{Colors.BLUE}Bank Account Bot: {Colors.ENDC}{chat(user_input)}\n")
    except KeyboardInterrupt:
        print(f"\n{Colors.BLUE}Program interrupted.{Colors.ENDC}")
    except Exception as e:
        print(f"\n{Colors.BLUE}Error: {str(e)}{Colors.ENDC}")
    finally:
        print(f"{Colors.BLUE}Exiting...{Colors.ENDC}")

if __name__ == '__main__':
    main()