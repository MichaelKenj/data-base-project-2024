# 🚗 AutoRepair Management System

## Project Overview

The **AutoRepair Management System** is a REST API-based application designed to streamline and manage the operations of an auto repair workshop. The application leverages a PostgreSQL database to store data about cars, mechanics, and orders, offering powerful query and data management capabilities.

The project demonstrates the use of modern Python technologies such as **FastAPI**, **SQLAlchemy**, and **Alembic**, along with advanced database features like JSON fields, indexing, and full-text search. The system is built with modularity, scalability, and ease of use in mind, catering to both developers and end-users.

---

## Features

### Core Functionality
1. **Database Initialization**
   - A script to initialize the PostgreSQL database with a specific name and owner.

2. **CRUD Operations**
   - REST API endpoints to perform **Create**, **Read**, **Update**, and **Delete** operations for:
     - **Orders**
     - **Cars**
     - **Mechanics**

3. **Data Population**
   - A script to populate the database with a large amount of data using the REST API.

4. **Data Migrations**
   - Implements two data migrations using Alembic:
     - Adding new columns.
     - Creating indexes for optimized queries.

### Advanced Query Support
1. **Query Types**
   - Complex SELECT queries with multiple conditions.
   - JOIN operations between tables.
   - Conditional UPDATE queries.
   - GROUP BY functionality.
   - API-level sorting of query results.

2. **JSON Field and Full-Text Search**
   - Utilizes PostgreSQL's **pg_trgm** + **GIN index** for efficient full-text search on JSON fields.

### Additional Features
1. **Pagination**
   - API endpoints support pagination for improved performance on large datasets.

2. **User Interface**
   - A simple UI to interact with the application.

3. **ORM Usage**
   - SQLAlchemy ORM for database interaction.

---

## Database Design

### Tables and Relationships
- **Order**
  - Fields: Cost, Issue Date, Type of Work, Planned Completion Date, Actual Completion Date.
  - Relationships:
    - Linked to a **Car** (1:N).
    - Linked to a **Mechanic** (1:N).

- **Car**
  - Fields: Make, License Plate, Year, Owner Name.
  
- **Mechanic**
  - Fields: Name, Experience, Grade, Employee Number.

---

## Technologies Used

- **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **Database:** [PostgreSQL](https://www.postgresql.org/)
- **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
- **Migrations:** [Alembic](https://alembic.sqlalchemy.org/)
- **Frontend (Optional UI):** HTML/CSS with basic interactivity.

---

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
