## Tasks

I asked three of my friends to complete the following tasks and document their experience:

1. View all products
2. Sort the products and find the two with the best price and the two with the best rating.
3. Add a product to your cart.
4. Update the quantity to two.
5. Add another product to your cart and then delete it.
6. Create an account.
7. Verify your account by going to your email and click the link.
8. Checkout your product and check the 'save shipping details' button. Use the card number 4242 4242 4242 4242 any futher date and whatever three-digit CVC you want.
9. Find your confirmation email.
10. Rate the product you bought and leave a message.
11. Make another purchase and see if your shipping details are already filled in.
12. Logout of your account.
13. Login again but click the 'Forgot your password' link and reset your password.
14. Login again.

### Feedback

Noone had any problems with any of the tasks but i did get some other good feedback.


* On some pages the footer wasnt sticking to the bottom of the page and there would be white space below it. To fix this I set the container height to 100%
* On the home page where the navigation bar is transparent it looked really weird when scrolling down since the links text are white. I fixed this by adding display: none to the navigation when scrolling down past the image.
* If you scrolled down on the home page there's a section called 'Best rated discs' This section would show all products on the page insted of just a few of the best rated ones. I fixed this by adding [:8] to the query to only get the first eight results. 
* On all pages of the site the products are stored in a cart, the cart is refrenced everywhere except in the products details page. There it says 'Add to Bag' witch is a bit weird. I fixed this by changing the text to 'Add to Cart'


## User Story Testing

### Shoppers

1. As a shopper I want to be able to view all products so that I can browse the websites products.
* All products can be found either by clickling the "Shop Now" button on the home page or by clickling "All Products" in the navigation and then again "All Products"

2. As a shopper I want to be able to sort products based on type of product so that I can find products based on what I want.
* This can be done by clickling the "All Products" link in the navigation, once its clicked it shows a dropdown menu with all diffrent types of products.

3. As a shopper I want to be able to sort products based on category so that i can find the best rated/priced products.
* This can be done with a sort selector on all products pages and on the deals page.

4. As a shopper I want to be able to add products to a cart so that i can save products im interested in.
* This was tested by going to all products detail and clickling the "Add to Cart" button. It was possible to add all products to the cart without any issues.

5. As a shopper I want to be able to select a quantity of the product to add to the cart so that i can add more than one of the same product to my cart
* This was tested by first trying to add 0 of a product to the cart witch made the form give back an error telling the user they couldn't add 0 of a product.
Users can add anywhere from 1-99 of the same product. When testing this i saw that users could add the quantity 99 of a product several times without getting an error. This isn't really a problem though since the user still have to pay for all if they actually try to buy more than 99.

6. As a shopper I want to be able to view the price of my entire cart so that i can be aware of how much it costs.
* I didn't really have to test this since I could see that it works from completing the previous user story.

7. As a shopper I want to be able to update the quantity of a product in my cart so that i can easily make changes in my cart.
* This was tested the same way i tested user story number five. The results were that a user could only update the quantity to a number between 1-99.

8. As a shopper I want to be able to delete products from my cart so that i can remove products i dont want to buy.
* This was tested by adding products to the cart and then on the cart page clicking the button 'delete'.

9. As a shopper I want to be able to easily checkout and enter my shipping details so that i can feel comftrable and safe when placing my order
* This function was tested using Stripe's test card number witch i mentioned earlier.

The following scenarios were tested to make sure the checkout proccess went through securly:


* Submitting an order, only entering the required fields on the form. The order went through both on Stripe and was stored in the database with a success webhook message.


* Attempting to submit an order with incorrect card details. An error message appears underneath the card details form confirming the details are incorrect.
The same happend if a user tried to enter invalid dates.

* Commenting out the form.submit() function and attempting to submit an order.
This simulates a user losing internet access or accidentaly closing down the tab. The order went through anyways both on Stripe and the webook created it in our database.


* Attempting to submit an order with an incomplete order form. All empty required fields alert the user they must be filled to be completed and the form isn't submitted.

10. As a shopper I want to be able to make a purchase using my debit/credit card so that i can pay for my order right away.
* I didn't have to test this since i already did when testing user story 9.

11. As a shopper I want to be able to recive a confirmation email so that i can feel safe that the order went through and keep record of my orders.
* All of my friends that completed the previous mentioned tasks recived a confirmation email and i myself also tested this by placing a few orders witch all sent confirmation emails.

12. As a shopper i want to be able to view an order confirmation so that i can verify that my order details are correct.
* Users with a profile that has chose to save their order information can always find their order details by going to their profile. Incase you dont have a profile you can always refer to your email confirmation. I reviewed  the order details page and made sure it contained the following:
    * Order number
    * Product Name and Quantity
    * Price per item
    * Shipping information
        * Name
        * Email
        * Phone Number
        * Address
        * Order Total
        * shipping Cost
        * Grand Total

13. As a shopper I want to be able to easily contact the store so that i can ask them questions and get assistans if needed.
* All of the stores contact information is shown in both the footer and on the Contact page

14. As a shopper I want to be able to read course reviews so that i can find new good courses to try out.
* Store owners can create course reviews via the admin panel so to test this I created a few and they all showed up under the Course Reviews page as expected.

15. As a shopper I want to be able to sign up to a newsletter so that i can be the first one to hear about new arrivals and deals.
* This was tested by trying to enter my own email into the newsletter form located in the footer. This works and opens up a new tab for the user letting them know they are now signed up to the newsletter. When setting up mailchimp the user would get a confirmation text showing up next to the sign up form insted of getting a new page pop up. I had to remove the js file that was making this possible becouse of it messing up the toasts. Because of time constraint I didn't have time to look into this more but will for sure do later to give the user a more smooth experience.

16. As a shopper I want to be able to register for an account so that i can see my previous orders and save my shipping details.
* This was tested by my friends when they completed all of their tasks and by me after getting their feedback and making the changes they wished.

17. As a shopper I want to be able to login/logout so that i can Access my profile.
* This was tested by simply clickling on the login link and loggin in and then clicking the logout button and confirming that i wanted to logout.
18. As a shopper I want to be able to recover my password if i forgot it so that i can recover my account.
* This was also tested by my friends during their tasks.

### Site Owner

1. As a store owner I want to be able to add products so that I can add new products to my store
* Products can be added both via the 'Product Managment' page found by clickling on the 'My account' icon in the navigation and via the admin panel.
both ways successfully created products on the website. I also tested visiting the add products page without being logged in as a site owner. This results in the user getting redirected to the sign in page. If the user signs in to an account that doesnt have superuser status they get a toasts saying 'Only admins are allowed here...' and gets redirected to the home page.

2. As a store owner I want to be able to edit already existing products so that I can manage products, ex. update images, price, description etc.
* Products can be edited by going to the product detail and clickling the 'edit' button only visable to superusers.
I made sure this url is only working for superusers by trying to visit the url as a generic user. If a generic user tries to access the url they get a toast saying 'Only admins are allowed here...' and get redirected to the home page.

3. As a store owner I want to be able to delete products so that I can remove products i dont want to sell anymore.
* This works the same way as the edit products user story and was tested the same way.

4. As a store owner I want to be able to see customer reviews on products so that I can know if the product is appricated or not.
* This was tested by looking at product details after my friends completed their tasks and i could see all of their reviews without any problems.

5. As a store owner I want to be able to send emails to customers that signed up to my newsletter so that i can notify them of any new arrivals or upcomming deals to increse sales.
* To complete this user story im using Mailchimp witch provides me with both the form to allow users to sign up to the newsletter and the ability to send email to all users that are signed up.

## Validator Testing
* The HTML templates were validated using the  [W3 Validator](https://validator.w3.org/nu/#textarea). No major errors were returned for the HTML files.
* The CSS style sheet was validated using [W3C Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) and no errors were returned. All CSS files returned with CSS level 3 + SVG.
* The JavaScript files were run through [JSHint](https://jshint.com) and no errors were found apart from a few missing semi-colons which were added. Also, the project was run through whilst checking for any issues in the console. No errors were found.
* The code was validated using[PEP8](http://pep8online.com). No errors were returned.
* Throughout the development proccess i also checked for errors by typing flake8 into the terminal, no major errors or issues are can be found.

## Responsive Testing

To ensure the website is fully responsive i tested it using theese devices and browsers:
* Iphone 11 pro
* Iphone X
* Samsung Galaxy S20
* Ipad (too old for me to know witch one)
* Macbook M1 Pro 16 inch
* Firefox
* Google Chrome
* Safari

## Bugs

I had an issue where there would be white space to the right side of my app on smaller screens such as an iPhone.
* I fixed this by adding overflow-x: auto, padding: 0 and margin: 0 to the body.

Had an issue with toasts not working. This was caused by mail chimps js file
* I fixed this by removing the mail chimp js file witch resulted in users getting a new page when subscribing to the newsletter.
This is just a temporary fix because of time constraints. If I had more time I would have tried to fix the issue by building a newsletter app and fulfil the mailing list requirements there.

When deploying the app to Heroku I got an error basically saying I had to specify the Python version so I originally added a runtime.txt file and added Django 3.8.0. to it When trying to deploy again I got the following message, "A Python security update is available! Upgrade as soon as possible to: python-3.8.13". So I changed the runtime to 3.8.13 witch resulted in the deployment being successful.

Images wouldn't load when referencing them in a template
* To fix this i added 'django.template.context_processors.media' to context_proccesors to handle the MEDIA_URL.

Images didn’t update when submitting the EditProductForm
* I fixed this by adding enctype="multipart/form-data" to the form in the template.



