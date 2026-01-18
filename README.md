# Wondor-WebApp Instruction
WONDOR is a blog based travel web app—you can think of it as TikTok, but only for travel.
It helps users discover destinations, experiences, and travel ideas quickly and visually by the help of different people around the world.

## Features Provided
1. User can **Create posts** just like a social media app.  
2. They can **View others** posts.

### Instructions to use Wondor
Follow these steps to run Wondor in your local machine
1. Clone the Repository
   ```bash
   git clone https://github.com/AkarshRaj-7920/Wondor-Webapp.git cd [folder-name]

2. Create and activate Virtual Enviornment.  
   ```bash
   # Windows
   python -m venv .venv
   .venv/Scripts/activate
   
   # Mac/Linux
   python3 -m venv .venv
   source .venv/bin/activatesa
   
3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   
4. Run Migrations
   ```bash
   python manage.py migrate
   
5. Start the Development Server
   ```bash
   python manage.py runserver

### Project Structure
- app/  
  |── Authentication #Everything related to User Authentication login, register, forgot password and etc...  
  |── crudpost #Create, delete, view a post
- media/ #Stores all the media files provided by the user
- static/ #All the **CSS** and styling files  
- templates/ #All the **HTML** files  
- Wandor/ #All the files for deployment and connecting the project files with each other  
