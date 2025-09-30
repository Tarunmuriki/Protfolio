from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

# --- Personal Info ---
about = {
    "name": "Muriki Tarun",
    "summary": """Enthusiastic B.Tech CSE (AIML) student at Parul University with a strong foundation 
    in Python, Java, SQL, HTML, CSS, and JavaScript. Skilled in problem-solving, data structures, 
    and AI/ML concepts with hands-on project experience. Passionate about building scalable 
    applications and aiming to grow as a Software Engineer.""",
    "email": "murikitharun@gmail.com",
    "github": "https://github.com/Tarunmuriki",
    "linkedin": "https://www.linkedin.com/in/muriki-tarun-b760592bb/",
    "profile_img": "images/profile.jpg"
}

# --- Projects ---
projects = [
    {"title": "DataAnalysis", "desc": "Data Analysis is the process of examining, cleaning, and visualizing data to extract meaningful insights and support decision-making."},
    {"title": "FlavorGraph", "desc": "FlavorGraph suggests recipes based on available ingredients and recommends substitutions."},
    {"title": "NewsHeaslines", "desc": "NewsHeadlines delivers the latest news summaries and trending headlines in a concise format."}
]

@app.route("/")
def home():
    return render_template("index.html", about=about, projects=projects)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        flash(f"Thanks {name}, I received your message! I’ll reply soon at {email}.")
        return redirect(url_for("contact"))

    return render_template("contact.html", about=about)

if __name__ == "__main__":
    app.run(debug=True)
