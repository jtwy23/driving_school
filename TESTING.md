# Testing & Bugs

## Testing

### During the development of the site all testing was done manually.

#### Navbar
- All links were clicked to test that it landed on the correct pages.
- All links highlighted when clicked and stayed highlight when on the current page.
- Login / Signup button displays when hovered over in desktop. Burger icon displays and is clickable in mobile and tablet view and the down caret is clickable to show 'For Pupil' or 'For Instructor'.
- The title can be clicked and is navigated back to home page.
- The seach icon is clickable and can search function works as expected.
- When logged in as a pupil the pupils name is displayed as 'Hello NAME' and the pupil can see their 'My Profile' and 'My Orders' tabs.
- The shopping cart will display 0 if there are no products and will display the number of products when products are added.

#### Footer
- Displays the sites three social media icons. All are clickable and open a new page to the social media platform.
- There payment methods are also displayed and are clickable and open to a new page.

#### Index
- The page loads up as expected. 
- On load the carousel loads and scrolls through each of the three images. The text also comes out and the 'See Lessons' button is shown and clickable. 
- When the 'See Lessons' button is clicked it takes me to the all lessons page. The all lessons page can also be accessed by scrolling further down the page.

#### All Lessons
- The page loads up however the lesson products are not in the correct order. The problem is from django templating language. This is still to be fixed. However the page does display all the products as intended.
- Every product when hovered over will display a button to 'View Lesson'. When clicked it till take me to the product description page.
- The link below the image is tested and is clickable. This too will take you to the product desription page.
- The prices are displayed and directly below the price will display and avergae user review rating. The rating is only displayed if a user has reviewed the product. If there is no review no rating will show.

#### Product Detail
- A large image will display. The image is slightly blurry due to the size of the image. It should be below 300px however I wanted users to see that they have clicked onto what they were looking at.
- The add to cart button is displayed in a large manner so a user can see it very clearly. When this is clicked the producted is added to the cart and the button will change to say 'Added to cart'. 
- When a user chooses to click into a product there is a function at the bottom of the page that will display other related products to the current product the user is viewing. This also works. When I click on an hourly lesson I will be shown all the other hourly lessons available and the same for blocks and intensive.

#### About
- Page loads as expected.
- There are two images here that load up and display as expected.

#### Contact
- Page loads as expected.
- The contact form is working. A user can fill in all fields and when the submit button is pressed the form is saved into the database for the Admin to check and reply.
- When clicked and none of the fields are filled an error message displays as well.

#### Shopping Cart
- When the cart icon is pressed a side windows slides out and displays all products a user has selected.
- The view cart button will allow users to proceed to order page.
- The clear cart button will simply clear the cart of all products and the user can start again.

#### Order
- A table will display the image, description and price of what the user has picked.
- The subtotal of the cart is also displayed.
- Depending on the amount the user will get 10% or 30% off.
- When the user is ready the proceed to checkout button will direct them to that page.

#### Proceed to Checkout
- The user details are displayed. The user can have a chance to amend any details at this point before purchase.
- When the checkout button is pressed the user will get to the payment page.

#### Payment 
- The cart at this point should clear as the products have been saved to the database and they are now required to pay.
- Once paid the user will be redirected back to index page and will be allowed to search and buy more products.

#### Responsiveness
- Chrome Dev Tools was used to test the sites responsivness.

Below are my findings on devices and browsers laid out in tables:

- Browser Test

|      Browser      | Responsive | Appearance | Functionality |
|:-----------------:|:----------:|:----------:|:-------------:|
|   Google Chrome   |     Yes    |    Good    |      Good     |
|      Firefox      |     Yes    |    Good    |      Good     |
|       Opera       |     Yes    |    Good    |      Good     |
|       Safari      |     Yes    |    Good    |      Good     |
|        Edge       |     Yes    |    Good    |      Good     |
| Internet Explorer |     Yes    |    Good    |      Good     |

### Device Test

|    Device    | Responsive | Appearance | Functionality |
|:------------:|:----------:|:----------:|:-------------:|
|   Galaxy S5  |     Yes    |    Good    |      Good     |
|    Pixel 2   |     Yes    |    Good    |      Good     |
|  iPhone 5/SE |     Yes    |    Good    |      Good     |
| iPhone 6/7/8 |     Yes    |    Good    |      Good     |
|   iPhone X   |     Yes    |    Good    |      Good     |
|     iPad     |     Yes    |    Good    |      Good     |
|   iPad Pro   |     Yes    |    Good    |      Good     |
|  Surface Duo |     Yes    |    Good    |      Good     |

- On all mobile devices I saw that the payment page was not working properly. The numbers ran into itself and is not clear for the user to know what is being entered. I tried to do a fix it with bootstrap and allowed for the horizontal slider to help users see what was being inputted. However I was not happy with this and reverted back for a more responsive view. I will be fixing this problem at a later date.

- Back to top button works. When not in use it remains red and when pressed to go back up to top the button will turn green, It will also take you to the to of the page.

- User reviews works well. When a user does a review for a product they cannot do another review for the same product. They can edit their review on the product if the choose to do so. Users cannot edit any other users reviews the edit button doesn't show.

---

## Code Validation

- HTML code has a few warnings and errors. Due to my time constraint and my deadline I have not had the chance to correct these. The code has been tested and works across all platforms on the live site. I will continue to fix my errors over time to make the html code clean. The errors are showing up in All lessons, profile, edit profile, all pages related to orders. The errors are most inheritted from the base.html.

CSS code has been ran through the validator and all work and clean.

Javascript code has been ran through jshint and although some of the code has errors the code has been tested on the live site and it all runs as expected.

Python code has been checked for PEP8 compliance. A lot of the python code was not PEP8 compliant through choice as I believed the code was more readable when lines were not seperated. Although some I did make split up and make PEP8 compliant. 

---

## Testing User Stories

User Stories (New Users):
- As a new user I would l like to be able to sign up quickly.
    * Users can land on the page and see quickly the button on the navbar to sign up.
- As a new user I would like to know I have signed up with an activation email.
    * Upon signing up the user will recieve and email to activate account before they can utilize the sites discounts.
- As a new user I would like to be able to update my profile.
    * Once the user is signed up they can navigate easily to the my profile page through the button in the navbar.
- As a new user I would like to know I am logged in.
    * When user is signed in the navbar button will announce the users name 'Hello Username'

User Stories (Site Admin):
- As a user I would like to add, edit and delete products on the website.#
    * From the admin panel the site admin can go to add catergories and products.
- As a user I would like to be able to delete reviews that are offensive or incorrect.
    * Site admin can go to product reviews and delete any unwanted reviews.
- As a user I would like to add in new instructor details.
    * Only the site admin can add in new instructors to the company. Instructors do not have a signup option like pupils.
- As a user I would like to delete old instructors who are no longer with the company.
    * Site admin can delete any unwanted or old instructors through instructor information table.
- As a user I would like to delete old or unwanted users.
    * This can be achieved from deleting users table.
- As a user I would like to check all messages sent to the company through the contact form.
    * From the admin panel the site Admin can login and check the contact us table where it shows the messages of pupils and saves the email address to reply to.
- As a user I would like to be able to check which pupils are to be refunded.
    * There is a customer refund table that you can see where pupils are to be refunded. Pupils not due a refund is not saved to the databasse.
- As a user I would like to be able to fully control my content.
    * The site admin has full control over the database and can create read update and delete everything.


User Stories:
- As a user I would like to be able to access the site across desktop, tablet and mobile platforms.
    * I can view the site on all platforms and is fully responsive.
- As a user I would like to contact the company easily with a form.
    * There is a contact form a user can use to contact the company.
- As a user I would like to add lessons into my shopping cart.
    * The shopping cart is easily identifiable and increments when products are added.
- As a user I would like to be able to clear my shopping cart contents.
    * The shopping cart has a clear cart button that will clear the cart completely and quickly.
- As a user I would buy lessons quickly.
    * Users who have signed up can simply add products and buy. However users who are not signed up must do so first and then can buy products.
- As a user I would like to have discounted lessons.
    * The main enticement to the website is the 10% and 30% discount. When a user is signed up they will get a 10% discount every time they buy a lesson but if they spend over £100 they will always get a 30% discount.
- As a user I would like to be able to track how many lessons I have bought.
    * Users can check their my orders page and a list of lessons purchased will show up and allow them to track the amount of lessons they have bought.
- As a user I would like to be able to cancel my lesson online.
    * Users who purchase lessons have the option to cancel within the my orders page.
- As a user I would like to know the name of my instructor.
    * When users purchase a lesson, the site admin will then manually assign an instructor to the user and the user can check on the order and the name of the instructor will be displayed.
- As a user I would like to be emailed when I have bought a lesson.
    * All purchases will have an email sent out to the user. If the user bys multiple lessons each lesson will be shown in the email and will have a unique purchase ID.
- As a user I would like to see details of the lesson I have bought in my email.
    * The email sent out will detail what lesson was bought and for how much.
- As a user I would like to know what the driving lesson entails.
    * Within each of the products view in the site there is a short description of what the lesson is what contains and how long the driving is.
- As a user I want to see the company’s social media links.
    * All social media links are clicakable and take the user to the respective social media platforms.


---

## Bugs

- Adding products bug. I was unable to add any products and have them display. This was fixed when I added the function into my index.html to display the products.

- The search bar was not working no results showed and did not seem to be searching. This was due to an invalid url. When I changed it to the correct url the search worked as expected.

- Cart page javascript code error. In the javascript the code repeatedly changed after saving. This issue was resolved by using the VS Code autosave function and the code seemed to remain the same. However whenever I restart my workspace the code reverts so I have had to push the code to heroku immediately before closing the work space and remember to correct the code before any other push after I restart the workspace.

- Procfile did not push to heroku. This is because I had managed to start the main project in a sub folder instead of the root directory. To fix this I had to navigate back to root level change the procfile and then push to Heroku.

- After my Heroku build the site did not open. I fixed this problem by going to my settings.py file and change the templates setting.

- During development I had forgotten to add the secret keys into the env.py file and commited the secret keys to github. I have left the keys unchnaged due to my time constraint with the project deadline and my own work but will change in the future by renewing all published secret keys and adding the new keys to an env.py file and making sure it is in the .gitignore file as well so the keys will be kept safe. Also complete the gitpod environment variables.

- The review and rating system works. However the rating stars could be made larger to be more eyecatching. If a user does not use the star rating on the inital review they will lose the chance to do so altogether. The review section is editable. There is no delete function built in as the site admin is the only person to have control over this and if the user did want it changed then they would need to contact the company.



