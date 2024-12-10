# Bevanda Mobile Bar: Booking and Inventory System

## Developers
  - Chris Maynard Ampon
  - Angel Gabriel Litob
  - Tisha Ryle Pusta
  - Kent Elrond Andionne Aspa
  - James Douglas Ancheta

## Subsystem Overview

The **Inventory Management Subsystem** is a component of the larger project aimed at streamlining and managing inventory-related tasks efficiently. It provides tools to monitor stock levels, track stock-ins and stock-outs, and generate detailed inventory reports. This system ensures better inventory control, reduces waste, and improves operational efficiency.

---

## How to Run the Subsystem
1. Clone the repository using:
   ```bash
   git clone https://github.com/chrismaynardampon/bevanda.git
```markdown
2. Navigate to the project directory:
    ```bash
    cd bevanda
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply migrations:
    ```bash
    python manage.py migrate
    ```
5. Start the development server:
    ```bash
    python manage.py runserver
    ```
6. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
```