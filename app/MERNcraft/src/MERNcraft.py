import os
import json
import tempfile
import time


# Global Variables
README_CONTENT = '''# MERN Barebones Project

This project structure sets up the basic file system and packages for a MERN stack project.

## Project Structure

- **frontend/**: Contains the React frontend.
- **backend/**: Contains the Express backend.
- **README.md**: Project documentation (this file).
- **.gitignore**: Contains files and directories to be ignored by Git.

### Backend

- `server.js`: The entry point for the Express server.
- **models/**: Directory for database models.
- **routes/**: Directory for API routes.
- **controllers/**: Directory for handling business logic.

### Frontend

- React app created using `npx create-react-app frontend`.

'''
GITIGNORE_CONTENT = '''node_modules
.DS_Store
.env
dist
build
*.log
*.lock
npm-debug.log
yarn-debug.log
yarn-error.log
coverage/
.vscode/
.idea/

'''
SERVER_JS_CONTENT = '''const express = require("express");
const app = express();
const port = process.env.PORT || 5000;

app.use(express.json());

app.get("/", (req, res) => {
  res.send("Hello, MERN!");
});

app.listen(port, () => {
  console.log(`Server running on port ${port}, link: http://localhost:${port}`);
});
'''


def _run_batch_commands(commands):
    """Creates a temporary batch file, executes it, and deletes it.

    Args
    ----
    - commands (list): List of commands to run in the batch file.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix='.bat') as temp_batch_file:
        batch_file_path = temp_batch_file.name
        temp_batch_file.write('\n'.join(commands).encode())

    try:
        os.system(f'"{batch_file_path}"')
    finally:
        os.remove(batch_file_path)


def _update_package_json(package_json_path='package.json'):
    """Updates the package.json file with custom scripts.

    Args
    ----
    - package_json_path (str, optional): Path to the package.json file. Defaults to 'package.json'.
    """

    with open(package_json_path, 'r') as f:
        package_json = json.load(f)

    package_json['scripts'] = {
        "test": "echo \"Error: no test specified\" && exit 1",
        "start": "node server.js",
        "dev": "nodemon server.js"
    }

    with open(package_json_path, 'w') as f:
        json.dump(package_json, f, indent=2)


def _get_user_choice(prompt):
    """Get user choice (y/n) and return True if 'y' and False if 'n'.

    Args
    ----
    - prompt (str): Prompt message.

    Returns
    -------
    - bool: True if 'y' and False if 'n'.
    """
    while True:
        try:
            print(prompt, end='')
            choice = input().lower()
            if choice in ['y', 'n']:
                return choice == 'y'
            raise ValueError
        except ValueError:
            print("Invalid input. Please enter 'y' or 'n'.")


def create_mern_project(root_dir=os.getcwd(), backend_dir="backend", frontend_dir="frontend",
                        create_backend=True, create_frontend=True,
                        create_readme=True, create_gitignore=True,
                        create_server_js=True):
    """Creates a barebones MERN project with backend (Express) & frontend (React) setup.

    Args
    ----
    - root_dir (str, optional): Root directory for the project. Defaults to the current working directory.
    - backend_dir (str, optional): Directory name for the backend. Defaults to 'backend'.
    - frontend_dir (str, optional): Directory name for the frontend. Defaults to 'frontend'.
    - create_backend (bool, optional): Create backend structure. Defaults to True.
    - create_frontend (bool, optional): Create frontend structure. Defaults to True.
    - create_readme (bool, optional): Create README.md. Defaults to True.
    - create_gitignore (bool, optional): Create .gitignore. Defaults to True.
    - create_server_js (bool, optional): Create server.js in backend. Defaults to True.

    Steps
    -----
    1. Change to project root directory.
    2. Create top-level files (README.md, .gitignore).
    3. Create backend directories & files.
    4. Create frontend directory & run create-react-app.
    """
    start_time = time.time()

    # Step 1: Change to project root directory
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
    os.chdir(root_dir)
    print(f"📂 Changed directory to {root_dir}")

    # Step 2: Create top-level files
    # Create README.md
    if create_readme:
        if os.path.exists("README.md"):
            if _get_user_choice("🔍 Found an existing README.md. Overwrite (y/n)?: "):
                with open("README.md", "w") as readme_file:
                    readme_file.write(README_CONTENT)
                print("✅ Overwritten README.md")
            else:
                print("Skipping README.md creation...")
        else:
            with open("README.md", "w") as readme_file:
                readme_file.write(README_CONTENT)
            print("✅ Created README.md")
    # Create .gitignore
    if create_gitignore:
        if os.path.exists(".gitignore"):
            if _get_user_choice("🔍 Found an existing .gitignore. Overwrite (y/n)?: "):
                with open(".gitignore", "w") as gitignore_file:
                    gitignore_file.write(GITIGNORE_CONTENT)
                print("✅ Overwritten .gitignore")
            else:
                print("Skipping .gitignore creation...")
        else:
            with open(".gitignore", "w") as gitignore_file:
                gitignore_file.write(GITIGNORE_CONTENT)
            print("✅ Created .gitignore")

    # Step 3: Create backend directories & files
    if create_backend:
        os.makedirs(f"{backend_dir}/models", exist_ok=True)
        os.makedirs(f"{backend_dir}/routes", exist_ok=True)
        os.makedirs(f"{backend_dir}/controllers", exist_ok=True)
        print("✅ Created backend structure")

        # Change to backend directory
        os.chdir("backend")

        # Create server.js
        if create_server_js:
            if os.path.exists("server.js"):
                if _get_user_choice("🔍 Found an existing server.js. Overwrite (y/n)?: "):
                    with open("server.js", "w") as server_js:
                        server_js.write(SERVER_JS_CONTENT)
                    print("✅ Overwritten server.js")
                else:
                    print("Skipping server.js creation...")
            else:
                with open("server.js", "w") as server_js:
                    server_js.write(SERVER_JS_CONTENT)
                print("✅ Created server.js")

        # Create & run the batch file for npm initialization
        init_npm_commands = ["npm init -y"]
        _run_batch_commands(init_npm_commands)
        print("📦 Initialized npm in backend")
        express_command = ["npm install express"]
        _run_batch_commands(express_command)
        nodemon_command = ["npm install nodemon --save-dev"]
        _run_batch_commands(nodemon_command)
        print("📦 Installed Express & Nodemon in backend")

        # Update package.json with new scripts
        _update_package_json()
        print("✅ Updated package.json with custom scripts")

        # Change back to project root directory
        os.chdir("..")

    # Step 4: Create frontend directory & run create-react-app with threading
    if create_frontend:
        print("📦 Creating React app in frontend...")
        create_react_app_commands = [
            f"npx create-react-app {frontend_dir}"
        ]
        _run_batch_commands(create_react_app_commands)

        # Install axios
        os.chdir(frontend_dir)
        axios_command = ["npm install axios"]
        _run_batch_commands(axios_command)
        print("📦 Installed axios in frontend")

        # Change back to project root directory
        os.chdir("..")

        print("📦 Created React app in frontend")

    end_time = time.time()

    # Final message
    print("🎉 MERN project setup complete!")
    print(f"⏱️ Time taken: {end_time - start_time:.2f}s")
    print("Additional steps:")
    print(
        f"1. Change directory to {frontend_dir} and start the React app using 'npm start'.")
    print(
        f"2. Change directory to {backend_dir} and start the Express server using 'npm run dev'.")
    print("Happy coding! 🚀")


# Example Usage
if __name__ == "__main__":
    create_mern_project(root_dir="mern_project")
