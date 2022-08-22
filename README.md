<h1>Disc Golf</h1>


### **Live Site**
[Disc Golf](https://ci-pp5-e-commerce.herokuapp.com/)

# About
This is a full-stack e-commerce project I build using Python, JavaScript, HTML and CSS.
I created this website for a friends business that sells golf discs.

# Content

[User Experience](#user-experience)


# Strategy
 The purpose of this project is to create a website that allows users to purschase products and the site owner to recive all orders. The target audience for theese products are

 * Active people that enjoys nature
 * Those who often play disc golf
 * All ages

 Thinking aout the main audience i think the most important things for this website to contain is the following:

* Easy to navigate and to sort for the type of disc your interested in buying.
* Has alot of trustability to make the user feel like they are buying from proffesionals that know what their talking about.
* Has social media links to Facebook, Instagram etc.
* User accounts to easily keep track of previous orders.
* Let users that bought a product rate it.

And the most important functionality for the site owner is the following:

* Ability to add, update and delete products. 
* Ability to add discounts to products.
* Allow users to contact the store owner incase they have any questions or if something is not working as expected.
* Look at customer reviews on products.

# User Stories

## User

1. As a shopper I want to be able to view all products so that I can browse the websites products.
2. As a shopper I want to be able to Sort products based on type of product so that I can find products based on what I want.
3. As a shopper I want to be able to sort products based on category so that i can find the best rated/priced products.
4. As a shopper I want to be able to add products to a cart so that i can save products im interested in.
5. As a shopper I want to be able to select a quantity of the product to add to the cart so that i can add more than one of the same product to my cart
6. As a shopper I want to be able to view the price of my entire cart so that i can be aware of how much it costs.
7. As a shopper I want to be able to update the quantity of a product in my cart so that i can easily make changes in my cart.
8. As a shopper I want to be able to delete products from my cart so that i can remove products i dont want to buy.
9. As a shopper I want to be able to easily checkout and enter my shipping details so that i can feel comftrable and safe when placing my order
10. As a shopper I want to be able to make a purchase using my debit/credit card so that i can pay for my order right away.
11. As a shopper I want to be able to recive a confirmation email so that i can feel safe that the order went through and keep record of my orders.
12. As a shopper I want to be able to easily contact the store so that i can ask them questions and get assistans if needed.
13. As a shopper I want to be able to read course reviews so that i can find new good courses to try out.
14. As a shopper I want to be able to sign up to a newsletter so that i can be the first one to hear about new arrivals and deals.
15. As a shopper I want to be able to register for an account so that i can see my previous orders and save my shipping details.
16. As a shopper I want to be able to login/logout so that i can Access my profile.
17. As a shopper I want to be able to recover my password if i forgot it so that i can recover my account.

## Site Owner

1. As a store owner I want to be able to add products so that I can add new products to my store
2. As a store owner I want to be able to edit already existing products so that I can manage products, ex. update images, price, description etc.
3. As a store owner I want to be able to delete products so that I can remove products i dont want to sell anymore.
4. As a store owner I want to be able to see customer reviews on products so that I can know if the product is appricated or not.
5. As a store owner I want to be able to send emails to customers that signed up to my newsletter so that i can notify them of any new arrivals or upcomming deals to increse sales.

# Scope

To achieve my user stories and thinking about the strategy the website will be created with the following functions:

## User
* Navigation thats shown on every page that contains the following:
    * A link back to the home page.
    * A search bar that lets the user search for specific products.
    * Links to the user profile and a cart that displays total price if its not empty.
    * Link to filter for diffrent types of products and links for deals, course reviews and contact
* A landin page that clearly demonstrates what the site is for.
* A product page that lists all products and can be filtered for best price, rating and name.
* Product details page that shows the products details and allows the user to add it to their cart.
* Registration/login functionality so that users can create and manage their account. Built using django allauth to make sure everything is secure.
* A user profile page so that users can save preferred shipping details and view past orders.
* A custom 404 page to let the users go back to the home page.
* A checkout page to let the users place orders safely and secure.
## Site owner
* Link in the nav to add new products.
* Links under the product details to edit and delete products.
* See customer reviews under the product details.
