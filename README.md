# Driving School

---

![Logo](assets/images/logo.jpg)

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

- [Desktop](https://github.com/jtwy23/seed2cigar/blob/master/mockups/Milestone%2002%20-%20Desktop.pdf)

- [Mobile](https://github.com/jtwy23/seed2cigar/blob/master/mockups/Milestone%2002%20-%20Mobile.pdf)

- [Tablet](https://github.com/jtwy23/seed2cigar/blob/master/mockups/Milestone%2002%20-%20Tablet.pdf)

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
    - The markup language used to structure and present the content onto the web.

* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)
    - Used CSS to style the website.

* [Javascript](https://www.javascript.com/)
    - Used javascript to put logic into the website.

* [Boostrap version 4.5.0](https://getbootstrap.com/)
    - Framework used to create website.

* [Google Fonts](https://fonts.google.com/)
    - Used ['Cantarell'](https://fonts.google.com/specimen/Cantarell?query=cantarell) 
    font for all text on website and 
    ['Caveat'](https://fonts.google.com/specimen/Caveat?query=caveat) for all title headings.

* [Fontawesome](https://fontawesome.com/)
    - All icons were used from fontawesome.

* [Google Maps API](https://developers.google.com/maps/documentation/javascript/overview)
    - API used to produce the map for Cigar Globe section.

* [jQuery](https://jquery.com/)
    - The Alphabetical Navigation list was built with jQuery.

* [EmailJS API](https://www.emailjs.com/)
    - Emailing set up with this API to connect to clients email.

* [Balsamiq Wireframes](https://balsamiq.com/)
    - Used to create basic layout of the pages.

* [Pexels](https://www.pexels.com/)
    - Stock images taken from this website.

* [Pexabay](https://pixabay.com/)
    - Stock images taken from this website.

* [Unsplash](https://unsplash.com/)
    - Stock images taken from this website.

* [The Noun Project Favicon](https://thenounproject.com/)
    - Favicon creator.

---

## Testing

### HTML5

I ran all the HTML code into [W3C Markup Validator](https://validator.w3.org/). Out of five pages there were no
errors. However there were two pages that had a warning for an empty heading. As javascript is implemented for
this project these two warnings can be ignored because when these pages load javascript will then populate
the heading. This is why it is left empty.

#### index.html
![index validator img](readme-images/hv-index.jpg)
    - No errors or warnings.

#### cigargame.html
![cigargame validator img](readme-images/hv-cigargame.jpg)
    - No errors but a warning for an empty heading. But javascript will populate the page when 
    loaded.

#### cigarquiz.html
![cigarquiz validator img](readme-images/hv-cigarquiz.jpg)
    - No errors or warnings.

#### end.html
![end validator img](readme-images/hv-end.jpg)
    - No errors but a warning for an empty heading. But javascript will populate the page when 
    loaded.

#### highscores.html
![highscores validator img](readme-images/hv-highscores.jpg)
    - No errors or warnings.

---

### CSS

All style sheets were validated on [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).
No errors came up for any of CSS file. There were two files that came up with a warning in 
regards to Google fonts CSS and ran that file through the validator that also came up with 
no errors.

#### app.css
![app validator img](readme-images/cv-app.jpg)

#### cigargame.css
![cigargame validator img](readme-images/cv-cigargame.jpg)

#### googlefonts.css
![googlefonts validator img](readme-images/cv-googlefonts.jpg)

#### highscores.css
![highscores validator img](readme-images/cv-highscores.jpg)

#### style.css
![style validator img](readme-images/cv-style.jpg)

---

### Javascript

Running all the javascript code through [JSHint](https://jshint.com/) there were no errors. 
There were some warnings on the cigargame.js file but it was only because the code is written in 
ES6. I further tested the viability of the javascript code by getting the target audience to 
visit the website and play the quiz. All came back that the website loaded well and the quiz
populated the questions from the javascript.

#### cigargame.js
![cigargamejs validator img](readme-images/cigargamejs.jpg)

#### emailjs
![emailjs validator img](readme-images/emailjs.jpg)

#### end.js
![endjs validator img](readme-images/endjs.jpg)

#### map.js
![mapjs validator img](readme-images/mapjs.jpg)

#### scripts.js
![scriptjs validator img](readme-images/scriptjs.jpg)

---

## Responsive

The responsiveness of this website was tested using [Am I Responsive](http://ami.responsivedesign.is/#).

![amiresponsive img](readme-images/amiresponsive.jpg)

---

#### Header Section

The header is the sticky navigation bar which consists of the logo on the left and the six 
website sections. All sections were tested through clicking to get to the specified sections
and the logo is clicked to navigate back to the top of the page.

#### index.html Section

This is the single scrolling page which a user can navigate through the main part of the website
by either scrolling or using the navigation bar. I tested through both scrolling and using the
navigation bar with no problems. As all the sections are essentially on this one page I 
individually scrolled and clicked on the navigation bar to land on the section. 

On the Cigar Globe section the 
[Google Maps API](https://developers.google.com/maps/documentation/javascript/overview) loads 
well and shows the marker cluster. The text on this section allows users to hover over each 
factory name and click to show the user where the factory is and is identified with 
a letter corresponding to the letter next to the factory name.

Cigar Journey section is created with the 
[bootstrap accordion](https://getbootstrap.com/docs/4.3/components/collapse/#accordion-example). 
Each tab is clicked to show the next section and the last will collapse. The images were also 
tested for loading with no problems. The buttons too will highlight as the user hovers over each.
At the Cigar Talk section there is an alphabetical navigation list that is created through
[jQuery](https://jquery.com/). Each letter highlights when a user hovers over. Each click on a 
different letter will the show all the definitions for that letter. On load the A section is 
already loaded for the user to see.

On the Cigar Quiz section is the few times a user will navigate out of the main page. The quiz is 
created with [Javascript](https://www.javascript.com/). The button to go to the quiz highlights
and allows the user to click to the quiz.

The final section of the main page is the Contact section. It is a form with three fields. Name,
email and message. All fields are required before a user can send the message. 
[EmailJS API](https://www.emailjs.com/) is used to allow the user to contact the client. This 
too is tested and the email sends to the client seamlessly.

#### Cigar Quiz Section

When the user lands onto the Cigar Quiz section there is the logo which when clicked takes the
user back to the Home section. There are two additional buttons of Play and Highscores. These
buttons have box shadowing when the mouse hovers over. The Play button clicks through to the 
cigar quiz window and the Highscores takes the user to the Highscores list window.

#### Play Section

On the play screen there is a progress bar and score HUD which populates as the users progress.
The questions are randomly generated from the JSON file. There are four multiple choice 
answers a user can choose and when hovered over the each box is highlighted with box shadowing.
When a user clicks on a choice the box will either highlight green if correct or red when it is
wrong.

#### End Section

Once the game is finished the user is taken to the end section where there are a few choices.
The user can enter their name and save the score to their local storage so that they can always
see the score. They cannot save unless a name has been inputted. Once the save button is clicked
the user will be sent to the High Scores page.
They can also play again which will navigate them back to the quiz page. Or they can go home 
through the Go Home button or click the logo at the top of the page.

#### Highscores

This page will only show the top scores set by the user if the sixth score is higher than the
five on the page then the lowest score on the list is replaced. Again the user is given the 
choice of two buttons. Play Again will allow the user to navigate back to the quiz page or
Go Home to get back to the Home section of the website. They can also achieve this by clicking
the logo at the top.

#### Footer Section

The footer has the websites contact details and three social media icons. 
[Facebook](https://www.facebook.com/), [Instagram](https://www.instagram.com/) and 
[Twitter](https://twitter.com/) were tested to see if when these icons are clicked it navigates 
away to the respective page and opens on a new page so the user can get back to our site.

---

### Browser Test

|      Browser      | Good | Bad |
|:-----------------:|:----:|:---:|
|   Google Chrome   |   X  |     |
|      Firefox      |   X  |     |
|       Opera       |   X  |     |
|       Safari      |   X  |     |
|        Edge       |   X  |     |
| Internet Explorer |      |  X  |

In Internet Explorer the main part of the site is working well however the cigar quiz doesn't
populate the javascript code. This is because Internet Explorer is becoming very outdated and
the people that are still using IE browser is not the target audience the client is aiming for.


### Device Test

|    Device    | Good | Bad |
|:------------:|:----:|:---:|
|   Galaxy S5  |   X  |     |
|    Pixel 2   |   X  |     |
|  iPhone 5/SE |   X  |     |
| iPhone 6/7/8 |   X  |     |
|   iPhone X   |   X  |     |
|     iPad     |   X  |     |
|   iPad Pro   |   X  |     |
|  Surface Duo |   X  |     |

---

## Deployment

Github was used for deployment.

To publish the website, the following steps needs to be taken:

Open GitHub and go to your site's 'Repositories'
Go to 'Settings'
Scroll down until you see 'GitHub Pages'
Under GitHub pages, click on the dropdown under 'Source' and select the 'Master Branch' option
A green box should appear with the following message 
'Your site is published at https://jtwy23.github.io/seed2cigar/'

---

## Github Pages

![github img](readme-images/github.jpg)

Clone Website To clone the website to work locally, follow the steps below:

1. Go to the main page of the GitHub repository and click on the dropdown menu 
'Clone or download'
2. Copy the URL and go to your local IDE (Integrated Development Environment)
3. In the terminal of your IDE type in 'git clone' and the paste the URL copied from 
step 2 Press Enter and the clone will be created

---

## Credits

### Content

- Cigar journey content is from the article in 
[Cigar Aficionado](https://www.cigaraficionado.com/article/from-seed-to-shelf-8494).

- Cigar talk content is from 
[Havana House](https://www.havanahouse.co.uk/glossary-of-cigar-terminology-blog/).

### Media

All images are from [Pexels](https://www.pexels.com/), [Pexabay](https://pixabay.com/) and
[Unsplash](https://unsplash.com/).

### Web Template

The original template that gave me inspiration for this web layout is from 
[Drew Ryan](https://w3newbie.com/courses).

### Cigar Quiz

The cigar quiz was created through [James Q Quick's](https://www.jamesqquick.com/) video
tutorial.

### Aknowledgements

- All Code Institute tutors who have helped me build my website. From helping me get EmailJS working
to simple little errors I didn't see right away.

- My friend Chris who also helped me through some coding issues.

- All the friends and family that have tested my website.

---

## Disclaimer

This is only for educational purposes.

---


