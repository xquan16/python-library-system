# 📚 Python Library Management System

This is a command-line application for the "Brickfields Kuala Lumpur Community Library," developed for the "Python Programming (PYP)" module (CT108-3-1).

The system is built entirely in Python and uses `.txt` files as a flat-file database for data persistence. It serves three different roles: System Administrator, Librarian, and Library Member.


## 🔑 Key Features by Role

### 1. System Administrator
* **Member Management**: Full CRUD (Create, Read, Update, Delete) for library member accounts.
* **Librarian Management**: Full CRUD for librarian (staff) accounts.

### 2. Librarian
* **Book Catalogue Management**: Full CRUD (Add, View, Edit, Remove) for all books in the library catalogue.
* **Book Search**: A dedicated search function to find books by ID, Title, or Author.
* **Process Book Loans**: Manages the process of loaning a book to a member. The system validates member eligibility (checks for overdue books and 5-book limit).
* **Process Book Returns**: Manages the process of a member returning a book.
* **View All Loans**: Can see a list of all active and overdue loans.

### 3. Library Member
* **Profile Management**: Allows members to view and update their own profile information.
* **View Current Loans**: Members can check their own loaned books, due dates, and any overdue fees.
* **Search Catalogue**: A public-facing search for members to check book availability.

## 💻 Tech Stack
* **Language**: Python
* **Data Storage**: File I/O (`.txt` files for members, staff, catalogue, and loans)
* **Core Concepts**: Modular programming (splitting roles into different `.py` files), functions, data structures (lists and dictionaries), and file handling.

## Project Status: Completed