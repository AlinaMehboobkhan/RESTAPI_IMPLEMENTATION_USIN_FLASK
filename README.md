## 📖 **REST API Implementation using Flask**

This project implements a basic **RESTful API** using the **Flask** web framework in Python. The API allows users to manage job applications stored in a local `jobs.json` file, enabling essential **CRUD** operations:

- **GET /jobs** – Retrieve a list of all job applications.
- **GET /jobs/<job_id>** – Retrieve a specific job by its ID.
- **POST /jobs** – Add a new job application.
- **DELETE /jobs/<job_id>** – Delete a job by its ID.

The application uses a simple JSON file as a flat-file database, making it lightweight and easy to use without requiring any external database setup.

### 🔧 Key Functionalities:

- Loads job data from `jobs.json` at runtime.
- Automatically creates `jobs.json` if it does not exist.
- Assigns an auto-incremented `id` to each new job.
- Returns all data in standard JSON format.
- Provides proper HTTP status codes for success and error handling.

This API is ideal for:

- Beginners learning Flask and REST API principles.
- Prototyping backend logic without setting up a full database.
- Demonstrating simple file-based CRUD operations.

> The API runs on `http://127.0.0.1:5000/` by default and can be tested using tools like **Postman**, **cURL**, or a browser (for GET requests).

