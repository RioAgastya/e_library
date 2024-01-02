# E-library Systems
SQL Database implementation of E-library workflow

# Database Specification:
* Mission Statement
* Table Structure
* Design Requirements
* ERD diagram
* Implementation

# Mission Statement
This mission statement will guide the design and development of the database objects, 
which will likely include entities such as Users, Books, Authors, and more, to support the functionalities of the e-library application. 
The database will be designed to ensure efficient data retrieval, high performance, and scalability, aligning with the mission of providing a seamless and enriching user experience.

# Table Structure
* Users -> Contains data from the user, which contains the user_id for the primary key. Table users are used as important entities in this e-library cycle.
* Libraries -> Table libraries, stores data from each library available in a particular book. There is library_id as the primary key. Which can later be connected to the books you want to search for.
* Authors -> Authors store author data related to the books they publish. Author_id as primary key.
* Books -> Books stores book data containing title, author name, and category. Book_id as primary key. This table book is used to connect authors to almost all the entities involved.
* Categories -> Categories accommodate several book genres. In this database there are 5 genres, namely Self-Improvement, Biography, Fantasy, Romance, Science Fiction. Categories_id as primary key.
* Queues -> Queues are used to queue for books that have a sufficient quantity. Because in this database system the loan period is 2 weeks. Users can return books earlier than the due date. Books will be automatically returned when they exceed the due date. Queues_id as primary key.
* Loans -> Loans regulates all types of book borrowing by users. Such as books lent, time to pick up books, and time to return books. Loan_id as primary key.
* Library_book -> The books library stores library_id and books data so that later it can be searched from which libraries these books are ready and lent.

# Design Requirements
* Manages multiple libraries
  The application manages multiple libraries, each housing a diverse collection of books with varying quantities available for borrowing. 
* Book Collection
  - The database needs to store information about the diverse collection of books, including titles, authors, and available quantities.
  - To make searching easier for users, books are also divided into categories such as: self-improvement, biography, Fantasy, Romance, Science Fiction, etc.
* User Registration
Users can register on the e-library platform. Registered users can interact with the platform by borrowing books, placing holds, and managing their account.
* Loan and Hold System
  - Users can borrow books from any library in this application if the book is available.
  - The loan period is 2 weeks. Users can return books earlier than the due date
  - Books will be automatically returned when they exceed the due date
  - Users can only borrow 2 books at a time
  - The platform keeps track of loan transactions, including loan dates, due dates, and return dates.
  - Users can place holds on books that are currently unavailable.
  - The library maintains a hold queue, and when a book becomes available, it can be borrowed by the customer at the front of the queue. Additionally, if a customer doesn't borrow a held book within one week, the book is released for other users to borrow.
  - Users can only hold 2 books at the same time

# ERD design
![](https://github.com/RioAgastya/e_library/blob/main/ERD/Untitled%20(2).png)

# Implementation Full Versions
Please click this link for the full versions:
https://drive.google.com/drive/folders/1p2WeFI1nuPI7dqITTB5BHL6zswXKzSIF?usp=sharing
