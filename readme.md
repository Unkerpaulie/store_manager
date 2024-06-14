# Store Manager

## About
In this project the user will manage manage a fake store with randomly generated sales orders daily. As products are sold, the use is responsible for restocking their products and managing the store.

## Structure 
Each user/store would have a stock from a general pool of products. They would also have their list of randomly generated customer. You make your first stock order, set store start year, and you're open for business. 

Customers belong to regions. Products belong to subcategries which belong to categories.

Each customer can make orders, which consists of one or more order items, each item consiting of a product id and quantity. The product price is stored in the product table so the order totals will be calculated as needed.

Stock for a given product will be calculated as the total quantity stocked minus the total quantity sold. When the stock of a product is 50 or less, the store manager will be notified. Products cannot be ordered if they are out of stock.

## Automatic script
Either manually or autoamtically, the store manager can advance time by one day. When a new day occurs, the following will happen:
- random generation of cutomer orders, depleting the inventory based on quantity ordered
- random chance of a number of new customers per day (say between 0 and 3)
- very small chance of a new product being added on a given day
- even smaller chance of a product that is older than 1 year being discontinued on a given day

The store manager will monitor the daily activity, view graphics, statistics and reports on products, categories, customers, regions, and other analtyic dimensions. They are also responsible for restocking on products that are low.

A possible issue is generating historical data. Perhaps the best approach is that everyone starts 10 years in the past and may choose to advance time forward when they want.

## Clone this repo

`git clone https://github.com/Unkerpaulie/store_manager`

## setup

`pip install django`

In the project directory

`python manage.py migrate`

`python manage.py runserver`

By default, the server address is http://127.0.0.1:8000/

## Code snippets

Font Awesome cdn 5.15

`<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" />`

Bootstrap js 5.3

`<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>`

* set a default currency or force user to pick a currency on set up