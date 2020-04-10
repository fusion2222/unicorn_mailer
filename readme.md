# Unicorn Mailer

![Unicorn](./unicorn.png)

This simple Flask application stores newsletter subscriptions, which subsequently must be confirmed by client.

## Notes

Unicorn Mailer uses **sqlite3** as DB engine. It is easy to deploy anywhere, with as less hassle as possible.
Code is engineered with DB performance in mind.

In case of huge DB loads or more complicated DB logic, we can switch to Postgres.

## Prerequisites

In order to run Unicorn Mailer must have following installed:
    
- Any -nix Operating System
- `python 3`
- `virtualenv`
- `sqlite3`

## How to run

You can run development server as follows:

`./run.sh`

For debug mode:

`./run.sh dev`

By default, development server starts on `127.0.0.1:5000` 

## URLs

- Create subscription - **POST**  `/newsletter-subscription`
- Confirm subscription -  **GET** `/newsletter-subscription/<slug>/confirm`
- Delete subscription - **DELETE**  `/newsletter-subscription/<slug>`

## Technical Note

If you would like to delete all data for testing purposes or something, just delete `db.sqlite3` file and run `./run.sh` again.
