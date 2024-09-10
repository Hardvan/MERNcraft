import os
import json
import tempfile


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
  console.log(`Server running on port ${port}`);
});

'''


def run_batch_commands(commands):
    """Creates a temporary batch file, executes it, and deletes it."""
    with tempfile.NamedTemporaryFile(delete=False, suffix='.bat') as temp_batch_file:
        batch_file_path = temp_batch_file.name
        temp_batch_file.write('\n'.join(commands).encode())

    try:
        os.system(f'"{batch_file_path}"')
    finally:
        os.remove(batch_file_path)


def update_package_json():
    """Updates the package.json file with custom scripts."""
    package_json_path = 'package.json'

    with open(package_json_path, 'r') as f:
        package_json = json.load(f)

    package_json['scripts'] = {
        "test": "echo \"Error: no test specified\" && exit 1",
        "start": "node server.js",
        "dev": "nodemon server.js"
    }

    with open(package_json_path, 'w') as f:
        json.dump(package_json, f, indent=2)


def create_mern_project(root_dir=os.getcwd(), backend_dir="backend", frontend_dir="frontend"):
    """Creates a barebones MERN project with backend & frontend setup."""

    # Step 1: Change to project root directory
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
    os.chdir(root_dir)
    print(f"📂 Changed directory to {root_dir}")

    # Step 2: Create top-level files
    # Create README.md
    with open("README.md", "w") as readme_file:
        readme_file.write(README_CONTENT)
    print("✅ Created README.md")
    # Create .gitignore
    with open(".gitignore", "w") as gitignore_file:
        gitignore_file.write(GITIGNORE_CONTENT)
    print("✅ Created .gitignore")

    # Step 3: Create backend directories ""
    os.makedirs(f"{backend_dir}/models", exist_ok=True)
    os.makedirs(f"{backend_dir}/routes", exist_ok=True)
    os.makedirs(f"{backend_dir}/controllers", exist_ok=True)
    print("✅ Created backend structure")

    # Change to backend directory
    os.chdir("backend")

    # Create server.js
    with open("server.js", "w") as server_js:
        server_js.write(SERVER_JS_CONTENT)
    print("✅ Created server.js")

    # Create and run the batch file for npm initialization
    init_npm_commands = [
        "npm init -y",
        "npm install express nodemon",
    ]
    run_batch_commands(init_npm_commands)
    print("📦 Initialized npm in backend")

    # Update package.json with new scripts
    update_package_json()
    print("✅ Updated package.json with custom scripts")

    # Step 5: Create frontend directory & initialize React app
    os.chdir("..")

    # Create and run the batch file for creating React app
    create_react_app_commands = [
        f"npx create-react-app {frontend_dir}"
    ]
    run_batch_commands(create_react_app_commands)
    print("📦 Created React app in frontend")

    # Final message
    print("🎉 MERN project setup complete!")


if __name__ == "__main__":
    create_mern_project(root_dir="mern_project")
