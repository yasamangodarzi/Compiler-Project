# Compiler Project

## Project Overview
This repository contains an implementation of a compiler using ANTLR. The project includes defining the grammar, implementing parsing and lexical analysis, generating three-address code (TAC), and handling syntax testing.

---

## Features  
- **Grammar Definition:**  
  - Implemented using **ANTLR4**.  
  - Covers syntax and semantics of the target language.  
- **Parsing and Lexical Analysis:**  
  - Tokenization and syntax validation.  
  - Resolving **grammar ambiguities**.  
- **Code Generation:**  
  - Converts parsed code into **three-address code (TAC)**.  
  - Supports basic arithmetic and control flow.  
- **Testing & Debugging:**  
  - Sample test files included.  
  - **ANTLR Debugging** used to verify parsing.  

---
## Steps to Run the Compiler
1. Clone the repository.
2. Ensure you have ANTLR installed.(pip install antlr4-python3-runtime)
3. Navigate to the project directory.
4. Compile the grammar using ANTLR.(antlr4 -Dlanguage=Python MyGrammar.g4)
5. Run test cases to verify the implementation.(python compiler.py input_file.txt)

## Grammar Definition
The grammar is structured to avoid ambiguities and follows mathematical precedence rules.
The grammar for the custom language includes:
Arithmetic Operations: Addition, subtraction, multiplication, and division.
Conditional Statements: If-else structures.
Loops: While and for loops.
Variable Declarations.
Function Definitions.


![Screenshot from 2025-03-18 21-59-30](https://github.com/user-attachments/assets/94c0d1d7-427b-4eb8-83f7-c14c582f644c)

![Screenshot from 2025-03-18 21-59-40](https://github.com/user-attachments/assets/c706b3c7-8c33-4089-b0cf-9e926f4be497)

## Syntax Testing
Various test cases ensure correct parsing and compilation.
![intarith2](https://github.com/user-attachments/assets/bee0d916-4808-4904-bbbb-b6afc1591b67)


