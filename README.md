# MERNcraft

MERNcraft is an automation script designed to kickstart your MERN stack application development. It helps you set up a basic project structure with React for the frontend and Express for the backend.

## MERNcraft on PyPI

View the MERNcraft package on PyPI: [MERNcraft](https://pypi.org/project/MERNcraft/)

## Features

- **Frontend Setup**: Creates a React application using `create-react-app` with multithreading support.
- **Backend Setup**: Sets up a basic Express server with a sample `server.js` file.
- **Project Structure**: Organizes the project into `frontend/` and `backend/` directories.
- **Top-Level Files**: Includes a `README.md` and `.gitignore` for project documentation and Git management.

## Use Cases

- Quickly start a new MERN project with a clean structure.
- Prototype MERN stack applications.
- Automate the setup of MERN projects for testing or learning purposes.

## Getting Started

1. **Run the Automation Script**

   Install the MERNcraft package from PyPI using pip:

   ```bash
   pip install MERNcraft
   ```

   OR

   Clone this repository or download the script and run it to create your project structure:

   ```bash
   git clone https://github.com/Hardvan/MERNcraft
   cd MERNcraft
   python MERNcraft.py
   ```

   The script will:

   - Create the project directories and files.
   - Set up the React frontend.
   - Set up the Express backend.
   - Generate a `README.md` and `.gitignore` file.

2. **Start the Frontend**

   Navigate to the `frontend` directory and start the React app:

   ```bash
   cd frontend
   npm start
   ```

   Open `http://localhost:3000` to view your React app.

3. **Start the Backend**

   Navigate to the `backend` directory and start the Express server:

   ```bash
   cd backend
   npm run dev
   ```

   Open `http://localhost:5000` to view your Express server.

## Project Files

- **MERNcraft.py**: The main automation script that sets up your MERN project.
- **frontend/**: Contains the React application created with `create-react-app`.
- **backend/**: Contains the Express server setup.
  - **server.js**: The entry point for the Express server.
  - **models/**: Directory for database models.
  - **routes/**: Directory for API routes.
  - **controllers/**: Directory for handling business logic.
- **README.md**: Project documentation (this file).
- **.gitignore**: Contains files and directories to be ignored by Git.

## Notes

- Ensure you have Node.js and Python installed to run the automation script and manage dependencies.
- Customize your React and Express applications as needed.

Happy coding! 🚀

## Run the following commands to update the package (for maintainers)

1. Change version in `setup.py`
2. Run the following commands

   ```bash
   python setup.py bdist_wheel sdist
   twine check dist/*
   twine upload dist/*
   ```
