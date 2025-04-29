# Blog Summary API

This project provides a **Blog Summarization API** using **Django REST Framework** (DRF) for the backend and **PHP** for external website integration. It uses **Hugging Face's `transformers` library** to summarize blog content with a pre-trained model (`distilbart-cnn-12-6`). The summarized text is then displayed in a **Bootstrap modal** on the frontend.

---

## Features

- **Summarization API**: Automatically summarizes blog content.
- **Frontend Integration**: A simple PHP integration for external websites.
- **Bootstrap Modal**: Display the summary in a modal window.
- **CSRF Protection**: Ensures secure communication between the frontend and backend.

---

## Project Structure

### Backend (Django REST Framework)
- **`SummarizeBlogView`**: API endpoint that handles the blog summarization.
- **`/api/summarize/`**: POST endpoint that accepts a blog text and returns the summary.

### Frontend (PHP + JavaScript)
- **Summarize Button**: A button that triggers the blog summarization.
- **Bootstrap Modal**: Displays the summary of the blog.

---

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.x**
- **Django 3.x or higher**
- **Django Rest Framework**
- **Hugging Face Transformers** library
- **PHP 7.x or higher**
- **Bootstrap** (for modal styling)

---
