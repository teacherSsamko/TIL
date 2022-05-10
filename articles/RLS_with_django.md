# RLS with django

## Issue

The problem most people run into when trying to implement row level security is that most web applications, including Django applications, connect to the database with a single user, which makes it hard to take advantage of row level security.