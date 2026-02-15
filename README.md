# Whimsica Blog ✨

A magical blog platform where users can register, login, write stories, manage profiles, and share enchanted moments. Built with Flask for the backend, SQLite for data storage, and Jinja2 for templating. Features a whimsical, magical UI theme.

![Demo Video]
<video src="https://github.com/me-r1em/whimsica-blog/raw/main/demo.mp4" controls width="100%">
  Your browser does not support the video tag.
</video>
## Features
- **User Authentication**: Register, login, logout, and password changes using Flask-Login and Werkzeug.
- **Profile Management**: Update username, email, bio, and avatar (with image upload and resizing via PIL).
- **Blog Posts**: Create, view, and delete posts (only by the author). Posts are displayed in a grid with timestamps and author info.
- **Flash Messages**: Magical notifications for actions like publishing or errors.
- **Responsive Design**: Mobile-friendly with CSS gradients, glassmorphism, and Font Awesome icons.
- **Database Initialization**: Script to create tables (`create_db.py`).
- **Alternative Backend**: Includes a Node.js/Express/MongoDB version in `server.js` for a RESTful API (with JWT auth). `App.js` is a placeholder for a potential React frontend.

## Tech Stack
- **Backend**: Flask, Flask-SQLAlchemy (SQLite), Flask-Login, Flask-WTF, Werkzeug.
- **Frontend**: Jinja2 templates, HTML/CSS (with Google Fonts and Font Awesome), Bootstrap-inspired forms.
- **Other**: PIL for image processing, Datetime for timestamps.
- **Alternative**: Node.js, Express, Mongoose (MongoDB), JWT, Bcrypt (in `server.js`).

## Installation

### Prerequisites
- Python 3.x
- pip (for installing dependencies)

### Setup
1. Clone the repository:
git clone https://github.com/me-r1em/whimsica-blog.git
cd whimsica-blog

2.Install Python dependencies:
pip install flask flask-sqlalchemy flask-login flask-wtf werkzeug pillow

3. Initialize the database:
python create_db.py
This creates `blog.db` with User and Post tables.

4. (Optional) For the Node.js alternative:
- Install Node.js dependencies: `npm install express mongoose bcryptjs jsonwebtoken cors dotenv`
- Set up `.env` with `MONGO_URI` and `JWT_SECRET`.
- Run: `node server.js`

### Running the App
- Start the Flask server:
python app.py
- Open http://127.0.0.1:5000/ in your browser.
- Register a user, login, and start writing stories!

For the Node.js backend: `node server.js` (runs on port 5000). Use a frontend like Postman to test API endpoints.

## Usage
- **Home Page**: View all posts. Authenticated users can write new stories.
- **Profile**: View your posts, bio, and avatar. Edit via /settings.
- **Write**: Create new posts at /write.
- **Login/Register**: Secure forms with validation.
- **Admin/Deletion**: Users can only delete their own posts.

## Demo
Watch the output video: [demo.mp4]
<video src="https://github.com/me-r1em/whimsica-blog/raw/main/demo.mp4" controls width="100%">
  Your browser does not support the video tag.
</video>


## Contributing
Feel free to fork and submit pull requests. Issues welcome!

## License
MIT License – see [LICENSE](./LICENSE) for details.

Built with ✨ by Chehd. Inspired by magical realms and storytelling.
