# Project Overview

This project will be a fully functional eCommerece website with user and guest checkout capabilities.

We will start first by setting up our templates and data structure, then moving on to adding user checkout flow with payment integration.

After we complete basic checkout with a logged in user, we will add in the ability for users to checkout as a guest using cookies

# Project Structure

Before we start building, let's go over the core structure of this project. I’ll first go over templates and what each one will handle and then we’ll cover our models and page functionality.

## Templates

This project will focus on 3 main templates, store.html, cart.html and checkout.html.

![](img/4.png)

# What We Building

### Store.html

![](img/1.png)

This product will be a fully functioning eCommerce website from start to checkout functionality. Users will have the ability to add multiple products to cart, varying from physical to digital products.

## Payment Integration

### Cart.html

![](img/2.png)

### Checkout.html

![](img/3.png)

Payment integration will be handled with PayPal offering the ability to checkout with a PayPal account and checkout with PayPal debit/credit card. Stripe integration is simple to add but for the purpose of international transactions we will focus on PayPal for international availability and security.

# Models

![](img/models.png)

This project will consist of 6 Models, so let's summarize each one:

### 1. USER:

Built in Django user model, instance created for each customer who registers.

### 2. CUSTOMER:

Along with a User model, each customer will contain a Customer model that holds a one to one relationship to each user. (OneToOneFied)

### 3. PRODUCT:

The product model represents product types we have in store.

### 4. ORDER:

The order model will represent a transaction that is placed or pending. The model will hold information such as the transaction ID, data completed and order status. This model will be a child or the customer model but a parent to Order Items.

### 5. ORDERITEM:

An order Item is one item with an order. For example, a shopping cart may consist of many items but is all part of one order. Therfore the OrderItem model will be a child of the PRODUCT model AND the ORDER Model.

### 6. SHIPPING:

Not every order will need shipping information. For orders containing physical products that need to be shipping we will need to create an instance of the shipping model to know where to send the order. Shipping will simply be a child of the order model when necessary.

#

#### Before running this project you need intall below list apps and packages

Install Python 3.7 or above -> https://www.python.org/

Install Pip -> python get-pip.py

pip install Django

pip install Pillow

#### For running

python manage.py runserver
