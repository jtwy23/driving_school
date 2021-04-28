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

### Browser Test

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

- On all mobile devices I saw that the payment page was not working properly. The numbers ran into itself and is not clear for the user to know what is being entered. I tried to do a fix it with bootstrap and allowed for the horizontal slider to help users see what was being inputted

---

## Bugs



