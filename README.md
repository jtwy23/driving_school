# Driving School
 
---
 
![Logo]()
 
---
 
## Table of Contents
- [UX](#ux)
- [Strategy Plane](#strategy-plane)
- [Scope Plane](#scope-plane)
- [Structure Plane](#structure-plane)
- [Skeleton Plane](#skeleton-plane)
- [Surface Plane](#surface-plane)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Responsive](#responsive)
- [Deployment](#deployment)
- [Credits](#credits)
- [Disclaimer](#disclaimer)
 
Driving School is an e-commerce web site for new and regular pupils to view and buy driving lessons at their leisure. The site does not require a sign up if the user is only viewing lessons that they may want to purchase or even check up on the sites reviews. The user will need to sign up if they choose to buy lessons. to further entice users to sign up we are offering discounts on each lesson or if the users buy a large amount of lessons we will offer an even bigger discount. Driving School is based on 828 Driving School. It is a real business owned and operated by myself. This website is currently built on a Wordpress platform using free templates. The website is also an e-commerce site which allows users to be able to buy driving lessons online as well as get information on learning to drive and company information. I aim to implement the design and new features into the live working 828 Driving School site in the future. The website can be seen [here](https://driving-school-v1.herokuapp.com/).
 
---
 
## UX
 
To develop this website we have broken down the UX into its five planes to define the client’s needs.
 
### Strategy Plane
 
| Client Goals:                                                                               |
|---------------------------------------------------------------------------------------------|
| A fresh new website with new features.                                                      |
| Easy to navigate website for users to find what they need quickly.                          |
| Simple search functionality.                                                                |
| Easy and fast payment system for users (Stripe).                                            |
| Profile page for users to keep track of purchases and have a cancel button.                 |
| Messages for users when they cancel and allow users to know if they will be charged or not. |
 
| User Stories (New User):                                              |
|-----------------------------------------------------------------------|
| As a new user I would like to sign up quickly.                        |
| As a new user I would like to receive an activation email on signup.  |
| As a new user I would like to update my profile.                      |
| As a new user I would like to know I am logged in.                    |
 
| User Stories (Admin):                                                                         |
|-----------------------------------------------------------------------------------------------|
| As a new user I would like to add, edit and delete products on the website.                   |
| As a new user I would like to delete reviews that are offensive or incorrect.                 |
| As a new user I would like to add new instructor details.                                     |
| As a new user I would like to delete instructors who are no longer with the company.          |
| As a user I would like to delete old or unwanted users.                                       |
| As a user I would like to check all contact form messages saved to the database.              |
| As a user I would like to be able to check which pupils are to be refunded from the database. |
| As a user I would like to be able to fully control my website content.                        |
 
| User Stories:                                                                              |
|--------------------------------------------------------------------------------------------|
| As a new user I would like to access the site across desktop, tablet and mobile platforms. |
| As a new user I would like to contact the company through a contact form.                  |
| As a new user I would like to add lessons into my shopping cart.                           |
| As a new user I would like to clear the contents of my shopping cart.                      |
| As a user I would like to buy lessons quickly.                                             |
| As a user I would like to have good discounts on my lessons.                               |
| As a user I would like to be able to check check how many lessons I have purchased.        |
| As a user I would like to be able to cancel my lesson online.                              |
| As a user I would like to know the name of my instructor.                                  |
| As a user I would like to be emailed when I have purchased a lesson.                       |
| As a user I would like to be able to see the lesson details in my email.                   |
| As a user I would like a description of what a lesson entails.                             |
| As a user I would like to see the company social media links.                              |
 
---
 
### Scope Plane
 
| Features Include:                |
|----------------------------------|
| Responsive Design                |
| Navigation Bar                   |
| Slick Carousel                   |
| Call To Action Button            |
| Back To Top Button               |
| Search Functionality             |
| Shows Related Products for users |
| Users have Signup Functionality  |
| Forgotten Password Functionality |
| User Review Functionality        |
| Social Media Links               |
 
| Future Features:                                        |
|---------------------------------------------------------|
| User will be able to increment their lesson amounts.    |
| Automatically assign instructors to pupils by location. |
| Direct messaging system between instructor and pupil.   |
| Instructor diary within the instructor dashboard.       |
 
#### Database Schema
 
##### Contact App
 
###### Contact Us
| Title   | Database Key | Field Types | Validation     |
|---------|--------------|-------------|----------------|
| Email   | email        | CharField   | max_length=200 |
| Message | message      | TextField   | ()             |
 
##### Home App
 
###### Email Activation
| Title           | Database Key    | Field Types          | Validation                     |
|-----------------|-----------------|----------------------|--------------------------------|
| User            | user            | OneToOneField        | User, on_delete=models.CASCADE |
| Activation Key  | activation_key  | models.CharField     | max_length=500                 |
| Email Confirmed | email_confirmed | models.BooleanField  | default=False                  |
| Date Created    | date_created    | models.DateTimeField | auto_now_add=True              |
 
###### Category Lesson Table
| Title         | Database Key  | Field Types      | Validation     |
|---------------|---------------|------------------|----------------|
| Category Name | category_name | models.CharField | max_length=500 |
 
###### Lesson Table
| Title         | Database Key  | Field Types       | Validation                                                              |
|---------------|---------------|-------------------|-------------------------------------------------------------------------|
| Product Name  | product_name  | models.CharField  | max_length=2000                                                         |
| Category      | category      | models.ForeignKey | Categories, on_delete=models.CASCADE                                    |
| Instructor    | Instructor    | models.ForeignKey | instructor_information, on_delete=models.CASCADE, null=True, blank=True |
| Product Price | product_price | models.CharField  | max_length=2000                                                         |
| Image         | image         | models.ImageField | upload_to='uploads/product_image', blank=True, default=''               |
| Image 2       | image2        | models.ImageField | upload_to='uploads/product_image', blank=True, default=''               |
| Image 3       | image3        | models.ImageField | upload_to='uploads/product_image', blank=True, default=''               |
| Description   | description   | models.TextField  | ()                                                                      |
|               |               |                   |                                                                         |
 
###### Customer More Details
| Title        | Database Key | Field Types       | Validation                     |
|--------------|--------------|-------------------|--------------------------------|
| Customer     | Customer     | models.ForeignKey | User, on_delete=models.CASCADE |
| Phone Number | Phone_number | models.CharField  | max_length=200                 |
| Postcode     | Postcode     | models.CharField  | max_length=200, default=''     |
| Address      | Address      | models.CharField  | max_length=200                 |
 
###### Reviews
| Title       | Database Key | Field Types          | Validation                         |
|-------------|--------------|----------------------|------------------------------------|
| Customer    | customer     | models.ForeignKey    | User, on_delete=models.CASCADE     |
| Product     | product      | models.ForeignKey    | products, on_delete=models.CASCADE |
| Ratings     | ratings      | models.CharField     | max_length=1                       |
| Review Text | review_text  | models.TextField     | ()                                 |
| Review Time | review_time  | models.DateTimeField | default=datetime.now(), blank=True |
 
##### Instructor App
 
###### Add Instructor Information
| Title      | Database Key | Field Types      | Validation     |
|------------|--------------|------------------|----------------|
| First Name | first_name   | models.CharField | max_length=200 |
| Last Name  | last_name    | models.CharField | max_length=200 |
| Email      | email        | models.CharField | max_length=200 |
| Phone      | phone        | models.CharField | max_length=200 |
| Address    | address      | models.CharField | max_length=200 |
| Password   | password     | models.CharField | max_length=200 |
 
##### Order App
 
###### Order Table
| Title             | Database Key            | Field Types         | Validation                                                |
|-------------------|-------------------------|---------------------|-----------------------------------------------------------|
| User              | user                    | models.ForeignKey   | User, on_delete=models.CASCADE                            |
| Lesson            | Lesson                  | models.ForeignKey   | products, on_delete=models.CASCADE, blank=True, null=True |
| Instructor        | Instructor              | models.ForeignKey   | on_delete=models.CASCADE, blank=True, null=True           |
| Order ID          | order_id                | models.CharField    | max_length=1000                                           |
| Lesson Price      | Lesson_price            | models.CharField    | max_length=1000                                           |
| First Name        | first_name              | models.CharField    | max_length=1000                                           |
| Last Name         | last_name               | models.CharField    | max_length=1000                                           |
| Email             | email                   | models.CharField    | max_length=1000                                           |
| Phone             | phone                   | models.CharField    | max_length=1000                                           |
| Address           | address                 | models.CharField    | max_length=1000                                           |
| Zip               | zip                     | models.CharField    | max_length=1000                                           |
| Ordered           | ordered                 | models.BooleanField | default=False                                             |
| Instructor Cancel | instructor_cancel_order | models.BooleanField | default=False                                             |
| Customer Cancel   | customer_cancel_order   | models.BooleanField | default=False                                             |
| Completed Order   | Completed_order         | models.BooleanField | default=False                                             |
| Order Date        | order_date              | models.CharField    | max_length=1000                                           |
 
###### Cancelled Orders
| Title       | Database Key | Field Types          | Validation                      |
|-------------|--------------|----------------------|---------------------------------|
| User        | user         | models.ForeignKey    | User, on_delete=models.CASCADE  |
| Order       | order        | models.ForeignKey    | Order, on_delete=models.CASCADE |
| Cancel Time | Cancel_Time  | models.DateTimeField | auto_now_add=True               |
 
### Structure Plane
The website is designed to look simple but elegant. Users will land on the page with a slider going through driving images and text to buy lessons. There is no mistaking the user has landed on a driving school website. The impactful red colored title text 'Driving School' further emphasises the type of website a user is on. As a user scrolls down the page even larger images of UK speed signs will completely reassure the user that it is a drivng school website. The other pages also share the same driving theme as well as the sticky navbar with the red colored title will always be a constant reminder to the user of where they are. Colors also match the traffic light system in the slider texts.
 
### Skeleton Plane
Site map and wire frames
 
- [Desktop](https://)
 
- [Mobile](https://)
 
- [Tablet](https://)
 
### Surface Plane
To keep the elegance and impactfulness of the website the following design choices were made:
 
#### Fonts
Title Text = Courier
Main Text = Poppins
Footer Text = Montserrat
 
#### Colors
rgb(204, 0, 0) (Shade of Red - Title Heading)
rgb(255, 0, 0) (Shade of Red)
rgb(255, 191, 0) (Amber)
rgb(0, 153, 51) (Green)
rgb(113, 127, 224) (Blue - Carousel BTN Color)
rgb(34, 34, 34) (Shade of Black - Subheading)
rgb(34, 34, 34) (Shade of White - Footer text)
rgb(255, 193, 7) (Gold - Shopping cart ico)
rgb(23, 162, 184) (Cyan - User BTN)
 
---
 
## Technologies Used
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
 
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)
 
* [Javascript](https://www.javascript.com/)

* [Python](https://www.python.org/)

* [Django Framework](https://www.djangoproject.com/)
 
* [Boostrap version 4.3.1](https://getbootstrap.com/)
 
* [Fontawesome](https://fontawesome.com/)
 
* [jQuery](https://jquery.com/)
 
* [Balsamiq Wireframes](https://balsamiq.com/)
 
* [Unsplash](https://unsplash.com/)

* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)

* [dj-database-url](https://pypi.org/project/dj-database-url/)

* [Pillow](https://pypi.org/project/Pillow/)

* [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)

* [simplejson](https://pypi.org/project/simplejson/)

* [sqlparse](https://pypi.org/project/sqlparse/)

* [Stripe](https://stripe.com/)

* [ColorLib](https://colorlib.com/)
 
---

## Testing & Bugs

All testing and bugs are logged in my testing file here.

---
 
## Deployment
 
This project is deployed using Git. It's hosted on Heroku and all static files, including images, are hosted on AWS S3 Bucket. Stripe is used for payments and Gmail for an email account.
 
Before deploying the application, install the following modules:
 
- Python 3
- Git
- Pip
- Heroku Command Line Interface (CLI)
 
### Local Deployment 
 
To deploy Driving School locally:
 
1. From the applications [repository](https://github.com/jtwy23/driving_school), click the *code* button and download the zip file.
 
    You can also clone the repository in your terminal using the following:
 
git clone https://github.com/jtwy23/driving_school
 
2. Access the folder in your terminal window and install the application's required modules with the following command:
 
pip3 install -r requirements.txt
 
3. Add environment variables into your IDE (Gitpod)
 
- os.environ.get('STRIPE_API_KEY', 'YOUR_STRIPE_SECRET_KEY')
- os.environ.get('DATABASE_URL', 'YOUR_DATABASE_URL')
- os.environ.get('SECRET_KEY', 'YOUR_DJANGO_SECRET_KEY')
- os.environ.get('DEVELOPMENT', '1')
- os.environ.get('EMAIL_HOST_PASSWORD', 'YOUR_EMAIL_PASSWORD')
 
4. From the IDE terminal, migrate the models:
 
- python3 manage.py makemigrations
- python3 manage.py migrate
 
5. Create a superuser to access the admin panel.
 
6. Start application with command `python3 manage.py runserver` in your terminal. The application is now available in your browser.
 
### Deployment to Heroku 
 
 Deploying app to Heroku:

1.Install postgressSQL, WSGI HTTP Server and do database url to connect to the database. 

2. Create a `requirements.txt` file containing all of the 
 
3. Create a `Procfile` that contains the following: `web: gunicorn --pythonpath driving_school driving_school.wsgi:application`.

4. Push files to the repository master.

5. Login to Heroku and create a new app.

6. In Heroku dashboard of the new app, click deploy, then deployment method and select GitHub to connect your app to your github repository for automatic deployment.

7. In Heroku Resources tab, go to Add-Ons section and search for Heroku Postgres.

8. In settings tab, go to Reveal Config Vars and add the variables:
 
| **KEY**               | **VALUE**                          |
| --------------------- | -----------------------------------|
| AWS_ACCESS_KEY_ID     | ACCESS_KEY_ID_PROVIDED_BY_AWS      |
| AWS_SECRET_ACCESS_KEY | SECRET_ACCESS_KEY_PROVIDED_BY_AWS  |
| DATABASE_URL          | YOUR_DATABASE_URL                  |
| SECRET_KEY            | YOUR_DJANGO_SECRET_KEY             |
| STRIPE_SECRET_KEY     | YOUR_STRIPE_PUBLIC_KEY             |
| USE_AWS               | True                               |
 
9. In settings.py in your IDE, temporarily comment out the database and use the code below:
 
DATABASES = {
        'default': dj_database_url.parse('POSTGRESS URL')
    }
 
10. Migrate models to create the Postgress database:
 
- python manage.py makemigrations
- python manage.py migrate
 
11. Create a superuser to access the admin panel:
 
`python manage.py createsuperuser`
 
12. After you login to the admin panel, you can add data.
 
13. Remove temporary database from settings.py and uncomment other DB code and push code.

14.  Go to Heroku dashboad and deploy application.

15.  To view the site, go to view app.
 
### Hosting Media files in AWS
 
Both static and media files are hosted in the [AWS S3 Bucket](https://aws.amazon.com/). You need to create an account in AWS and create your S3 basket with public access.

---
 
## Credits
 
### Content
 
- Content was all my own.
 
### Media
 
All images are from [Unsplash](https://unsplash.com/) and also from my own website.
 
### Web Template
 
I used a frontend e-commerce web template.
[Colorlib](https://colorlib.com/).

### Aknowledgements
 
- All Code Institute tutors who have helped me. In particular [Michael Park](https://github.com/mparkcode) and [Fatima Aminu](https://github.com/Teemamin) who were there to get me through some dark times.
 
- All the friends and family that have tested my website.
 
---
 
## Disclaimer
 
This is only for educational purposes.
 
---