import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import json
import tempfile
import threading

import MERNcraft


class TestMERNProjectSetup(unittest.TestCase):

    # Mock os.system to avoid running actual commands
    @patch('MERNcraft.os.system')
    def test_run_batch_commands(self, mock_system):
        commands = ['echo Hello']
        with tempfile.NamedTemporaryFile(delete=False, suffix='.bat') as temp_batch_file:
            batch_file_path = temp_batch_file.name
            temp_batch_file.write('\n'.join(commands).encode())

        try:
            MERNcraft._run_batch_commands(commands)
            mock_system.assert_called_with(f'"{batch_file_path}"')
        finally:
            os.remove(batch_file_path)

    @patch('builtins.open', new_callable=mock_open, read_data='{}')
    @patch('MERNcraft.json.dump')
    def test_update_package_json(self, mock_json_dump, mock_open):
        mock_open.return_value.__enter__.return_value = MagicMock()
        MERNcraft._update_package_json('package.json')
        mock_open.assert_called_once_with('package.json', 'r')
        mock_json_dump.assert_called_once()

    @patch('builtins.input', return_value='y')
    def test_get_user_choice(self, mock_input):
        result = MERNcraft._get_user_choice('Continue? (y/n): ')
        self.assertTrue(result)

    @patch('builtins.open', new_callable=mock_open)
    @patch('MERNcraft._get_user_choice', return_value=True)
    def test_create_readme(self, mock_get_user_choice, mock_open):
        root_dir = tempfile.mkdtemp()
        readme_path = os.path.join(root_dir, 'README.md')
        with patch('os.chdir'):
            with patch('os.path.exists', return_value=False):
                MERNcraft.create_mern_project(
                    root_dir=root_dir, create_readme=True)
                mock_open.assert_called_once_with(readme_path, 'w')
        os.rmdir(root_dir)

    @patch('builtins.open', new_callable=mock_open)
    @patch('MERNcraft._get_user_choice', return_value=True)
    def test_create_gitignore(self, mock_get_user_choice, mock_open):
        root_dir = tempfile.mkdtemp()
        gitignore_path = os.path.join(root_dir, '.gitignore')
        with patch('os.chdir'):
            with patch('os.path.exists', return_value=False):
                MERNcraft.create_mern_project(
                    root_dir=root_dir, create_gitignore=True)
                mock_open.assert_called_once_with(gitignore_path, 'w')
        os.rmdir(root_dir)

    @patch('builtins.open', new_callable=mock_open)
    @patch('MERNcraft._get_user_choice', return_value=True)
    @patch('MERNcraft._run_batch_commands')
    @patch('MERNcraft._update_package_json')
    def test_create_backend(self, mock_update_package_json, mock_run_batch_commands, mock_get_user_choice, mock_open):
        root_dir = tempfile.mkdtemp()
        backend_dir = os.path.join(root_dir, 'backend')
        with patch('os.makedirs'):
            with patch('os.chdir'):
                with patch('os.path.exists', return_value=False):
                    MERNcraft.create_mern_project(
                        root_dir=root_dir, create_backend=True)
                    mock_open.assert_any_call(
                        os.path.join(backend_dir, 'server.js'), 'w')
                    mock_update_package_json.assert_called_once()
                    mock_run_batch_commands.assert_any_call(['npm init -y'])
                    mock_run_batch_commands.assert_any_call(
                        ['npm install express nodemon'])
        os.rmdir(root_dir)

    @patch('MERNcraft._run_batch_commands')
    @patch('MERNcraft._update_package_json')
    @patch('MERNcraft._get_user_choice', return_value=True)
    def test_create_mern_project(self, mock_get_user_choice, mock_update_package_json, mock_run_batch_commands):
        root_dir = tempfile.mkdtemp()
        with patch('os.chdir'):
            MERNcraft.create_mern_project(root_dir=root_dir)
            mock_run_batch_commands.assert_any_call(
                ['npx create-react-app frontend'])
            mock_update_package_json.assert_called_once()
        os.rmdir(root_dir)


if __name__ == '__main__':
    unittest.main()
