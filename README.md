# Protfolio
# 🧑‍💻 Muriki Tarun's Portfolio Website

This is a personal portfolio website built using **Flask** (a Python web framework) to showcase my skills, projects, and contact information.

## 🌟 Features

* **Home Page (`/`)**: Displays a summary of my technical skills, educational background, and highlights key projects.
* **Contact Page (`/contact`)**: Allows visitors to send a message via a form, providing immediate feedback via a Flask `flash` message.
* **Dynamic Content**: Personal and project information is managed directly in the Python code (`app.py`), making updates simple.

---

## 🚀 Getting Started

Follow these steps to get a copy of the project up and running on your local machine.

### Prerequisites

You need **Python 3** installed on your system.

### Installation

1.  **Clone the repository (if applicable) or save the files:**

    ```bash
    git clone [https://github.com/YourUsername/YourProjectName.git](https://github.com/YourUsername/YourProjectName.git)
    cd YourProjectName
    ```

2.  **Create and activate a virtual environment (Recommended):**

    ```bash
    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the necessary dependencies:**

    This project only requires `Flask`.

    ```bash
    pip install Flask
    ```

4.  **Create the required templates and static directories:**

    Ensure your project structure includes these folders for the Flask application to run correctly:

    ```
flask-portfolio/
├── app.py
├── requirements.txt
├── templates/
│ ├── base.html
│ ├── index.html
│ └── contact.html
└── static/
├── css/
│ └── style.css
└── img/
└── (put your profile image here, e.g. profile.jpg) 
    ```

    * `templates/`: Contains your HTML files (`index.html`, `contact.html`).
    * `static/`: Contains static assets like images, CSS, and JavaScript. The image **`profile.jpg`** must be placed in the `static/images/` folder.

---

## 🏃 Running the Application

1.  **Ensure your virtual environment is active.**

2.  **Run the main application file:**

    ```bash
    python app.py
    ```

3.  **Access the Website:**

    Open your web browser and navigate to the address shown in the terminal, usually:
    `http://127.0.0.1:5000/`

    *Note: The application is running in **Debug Mode** (`debug=True`) for development.*

---

## ⚙️ Configuration & Customization

All the content displayed on the website is defined in the `app.py` file.

| Section | Python Variable | Description |
| :--- | :--- | :--- |
| **Personal Info** | `about` (Dictionary) | Contains name, summary, email, social links, and profile image path. |
| **Projects** | `projects` (List of Dictionaries) | Defines the title and description for each showcased project. |
| **Security** | `app.secret_key` | **IMPORTANT**: Change `"supersecretkey"` to a strong, unique value for production environments. |

### Example Customization:

To change your name, modify the `about` dictionary in `app.py`:

```python
# app.py snippet
about = {
    "name": "Muriki Tarun", # <-- Change this value
    # ... rest of the dictionary
}
