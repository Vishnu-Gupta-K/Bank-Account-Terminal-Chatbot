# 🏦 Indian Student Bank Account Assistant

A helpful AI-powered terminal chatbot specifically designed to assist students in India with opening their bank accounts. This chatbot provides comprehensive guidance on required documents, account types, application processes, eligibility criteria, and covers major Indian banks like SBI, HDFC, ICICI, PNB, and others.

## 🌟 Features

- **Indian Banking Focus**: Specialized knowledge of Indian banking system and requirements
- **Document Guidance**: Complete list of documents required for Indian student accounts
- **Account Types**: Detailed information about student banking options in India
- **Bank Comparisons**: Information about SBI, HDFC, ICICI, PNB, and other major banks
- **Step-by-Step Process**: Complete walkthrough of the Indian banking application process
- **Fees & Charges**: Understanding of Indian student account fee structures
- **Security Tips**: Banking security advice specific to Indian banking
- **Graduation Transition**: Guidance on account conversion after graduation
- **AI-Powered**: Uses Google's Gemini AI for intelligent, contextual responses

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Google Gemini API key

### Installation

1. **Clone or download this project**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key:**
   - The `.env` file should contain your Gemini API key
   - Format: `GEMINI_API_KEY=your_api_key_here`

4. **Run the chatbot:**
   ```bash
   python main.py
   ```

## 💬 How to Use

### Quick Commands
- Type `documents` - See all required documents for Indian student accounts
- Type `account types` - View available student account options in India
- Type `process` - Get step-by-step application guide for Indian banks
- Type `banks` - Compare SBI, HDFC, ICICI, PNB and other options
- Type `fees` - Understanding charges and fee structures
- Type `eligibility` - Check if you qualify for student accounts
- Type `security` - Get banking security tips
- Type `exit` or `quit` - End the conversation

### Sample Conversations
- "What documents do I need for SBI student account?"
- "Which is better - HDFC or ICICI for students?"
- "How do I apply for a student bank account in India?"
- "What's the minimum deposit for student accounts?"
- "Can I open an account without PAN card?"
- "What happens to my account after graduation?"
- "How to keep my account secure?"

## 📋 Information Covered

### Required Documents for Indian Students
- Valid Photo ID (Aadhar Card, Passport, Voter ID, Driver's License)
- Proof of Address (Utility bill, rent agreement, passport)
- Passport-sized photographs
- Student ID or Enrollment Verification
- PAN Card (or Form 60 if unavailable)
- Initial Deposit (₹500 to ₹1000 typically)

### Account Types
- **Student Savings Account**: No minimum balance, lower charges, everyday transactions
- **Student Checking Account**: Active account for frequent transactions
- **Joint Account**: With parent/guardian for students under 18

### Major Indian Banks Covered
- **SBI (State Bank of India)**: Basic student savings with no maintenance charges
- **HDFC Bank**: Student accounts with comprehensive ATM and online banking
- **ICICI Bank**: No minimum balance requirements, easy management
- **PNB (Punjab National Bank)**: Low fees and accessible banking services

### Application Process
1. Choose appropriate account type for your needs
2. Gather all required Indian documentation
3. Visit branch or apply online (where available)
4. Complete application form with accurate details
5. Make initial deposit as per bank requirements
6. Set up internet and mobile banking
7. Receive debit card and cheque book

## 🛠 Technical Details

### Dependencies
- `google-generativeai`: For AI-powered responses
- `python-dotenv`: For environment variable management

### File Structure
```
├── main.py              # Main chatbot application
├── requirements.txt     # Python dependencies
├── .env                # API key configuration
└── README.md           # This documentation
```

## 🎯 Target Audience

This chatbot is specifically designed for:
- **Indian college students** opening their first bank account
- **Indian high school students** preparing for financial independence
- **Students** navigating the Indian banking system
- **Anyone** needing guidance on Indian student banking options
- **Students** looking to compare different Indian banks

## 🔒 Privacy & Security

- No personal information is stored
- Conversations are not logged
- API calls are made securely to Google's Gemini service
- Users are advised to contact banks directly for account-specific policies

## 📞 Support

For technical issues or suggestions:
- Check that your API key is properly configured
- Ensure all dependencies are installed
- Verify your internet connection for AI responses

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

## Acknowledgements


-   Developed by Vishnu Gupta Karapakula
-   Linkedin: https://www.linkedin.com/in/vishnu-gupta-karapakula-a89409272/

---


**Disclaimer**: This chatbot provides general information about Indian student banking. Always verify specific policies and requirements with your chosen Indian financial institution. The chatbot covers major banks like SBI, HDFC, ICICI, and PNB but does not perform any banking transactions.
