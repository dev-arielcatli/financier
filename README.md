# Financier

AI-powered personal finance management API

## ⚠️ Work in progress

As much as I love to work on this project fulltime, I still have a job that I love.

## 🧠 What is it?

Basically a glorified bookkeeper, financial coach, and financial manager.
I wanted to leverage the use of OpenAI models to create an assistant that will:

- keep track of my expenses
- generate reports
- remind me of a money-related event
- make me feel good about my financial health (or not)

### Features

1. 📃 Create, list, read, update, delete income and expense items.
2. 📸 Upload a photo of a receipt and let the assistant book it for you.
3. 📈 Generate daily, monthly, yearly reports of your finances.
4. 💪🏽Set budgets (daily and weekly).
5. 📨 Receive emails about alerts and notifications.
6. ⛰️ Set financial goals.
7. 👨🏽 Ask the assistant about your finances.

## ⚙️ Installation

This repository is a mono-repo. It has two parts:

1. `api` which contains the AWS-based API (infrastructure and business logic).
2. `application` is the Angular-based application code.

You can go to the directories and find their own `README.md` for their own installation instructions.

## 🛣️ Roadmap

### Phase 1

Initial setup.

- ✅ Initialize project structure
- ✅ Setup project
- Setup tests

### Phase 2

Simple proof of concept for data management.

- ✅ Data modelling
  - ✅ Expense
- ✅ Database stack
  - ✅ DynamoDB setup
- ✅ API stack
  - ✅ Create
  - ✅ Read
  - ✅ List
  - ✅ Update
  - ✅ Delete
- Lambda stack
  - ✅ Setup lambda layers
  - Create lambda layer creation script
  - ✅ Create
  - ✅ List
  - ✅ Read
  - ✅ Update
  - ✅ Delete
- Convert function creations to use YAML loading

### Phase 3

Securing our application.

- Stardardize IAM roles
- Cognito setup
  - Identity pools
- API Gateway authorizer

### Phase 4

Setup the assistant

- Write OpenAI model code for the assistant.
- Interface for the Financier API and the assistant API.

### Phase 5

Assistant features

- Tools for the assistant
  - Reports generator
  - Chat
  - Photo manager

### Phase 6

More assistant features

- Budget
- Alarms
- Goals
