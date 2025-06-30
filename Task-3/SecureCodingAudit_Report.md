# 🔒 Secure Coding Audit Report – CodeAlpha Internship

## 🧪 Audited Script:
Secure login system written in Python.

## 🔍 Security Issues Identified (based on example):
1. **Hardcoded Credentials** – insecure
2. **Plaintext Passwords** – no hashing
3. **No Input Validation** – allows weak input
4. **No Brute-force Protection**
5. **No Logging**

## ✅ Fixes Applied:
- Password hashing using `bcrypt`
- Validation for username and password
- Brute-force limiter with max 3 attempts and delays
- Organized, secure coding structure

## 🧰 Tools Used:
- Python 3
- `bcrypt`

## ✅ Best Practices:
- Hash all passwords
- Never hardcode credentials
- Validate input
- Limit login attempts
- Use secure libraries

## 👨‍💻 Author:
Youssef Elajmi (CodeAlpha Cyber Security Intern)