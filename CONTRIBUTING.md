
# Contributing to Robotics Club Website

Thank you for considering contributing to our Robotics Club Website! We welcome all kinds of contributions, whether it's fixing a bug, adding a new feature, improving documentation, or anything else.

## How to Contribute

### 1. Clone the repository

Start by cloning the repository to your local machine:

* Open VScode on Windows
* Run the following command in the terminal to clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/robotics-club-website.git
```

### 2. Set up a Python virtual environment

It's important to create a Python virtual environment for your development. This ensures that all dependencies are managed properly. Follow these steps:

1. **Navigate to the project folder**:

   ```bash
   cd robotics-club-website
   ```

2. **Create a virtual environment**:

   * On Mac/Linux:

     ```bash
     python3 -m venv venv
     ```
   * On Windows:

     ```bash
     python -m venv venv
     ```

3. **Activate the virtual environment**:

   * On Mac/Linux:

     ```bash
     source venv/bin/activate
     ```
   * On Windows:

     ```bash
     venv\Scripts\activate
     ```

### 3. Install dependencies

After activating the virtual environment, install the necessary dependencies:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file is missing or needs to be updated, you can generate it with:

```bash
pip freeze > requirements.txt
```

### 4. Create a new branch

Create a new branch for your changes. We follow the convention `feature/branch-name` for features and `bugfix/branch-name` for bug fixes.

```bash
git checkout -b feature/my-new-feature
```

### 5. Make changes

Make your changes in the new branch. Ensure that your code follows our coding style and passes any tests (if applicable).

### 6. Commit your changes

Once you've made your changes, commit them with a clear message:

```bash
git commit -m "Add feature: My new feature"
```

### 7. Push to the repository

Push your changes to the repository:

```bash
git push origin feature/my-new-feature
```

### 8. Open a pull request

Go to the repository on GitHub, and you'll see a prompt to open a pull request from your branch. Click the "Compare & Pull Request" button.

In the PR description, provide a summary of the changes you made and any additional context for the reviewer. Reference any related issues by including `#issue-number`.

## Coding Standards

* Use **Prettier** and **ESLint** for consistent code formatting and linting
* Use **camelCase** for JavaScript variables, functions, and method names
* Write clear, concise commit messages
* Ensure that your changes do not break any existing functionality

## Pull Request Review Process

* Your PR will be reviewed by a team member
* If changes are requested, make them and push them to your branch. The PR will automatically update
* Once approved, your PR will be merged into the main branch

## Issues and Bugs

If you find a bug or have an idea for a new feature, feel free to open an issue in the repository using our issue template.

### Reporting Bugs

Please provide as much detail as possible:

* Steps to reproduce the issue
* Screenshots or error messages
* Environment information (OS, browser, etc.)

## Licensing

By contributing to this repository, you agree that your contributions will be licensed under the MIT License.

## Getting Help

If you have questions about contributing, feel free to:

* Open an issue with the "Question/Help" label
* Reach out to the maintainers
* Check existing issues and discussions

Thank you for contributing!

---

