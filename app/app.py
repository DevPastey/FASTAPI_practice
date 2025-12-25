from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate

app = FastAPI()

text_posts = {
    1: {
        "title": "Getting Started with Python",
        "content": "Python is a beginner-friendly programming language used for web development, data analysis, automation, and more."
    },
    2: {
        "title": "Understanding Variables and Data Types",
        "content": "Variables store data in a program. Common data types include integers, strings, floats, and booleans."
    },
    3: {
        "title": "Control Flow in Python",
        "content": "Control flow tools like if statements and loops help you control how your program runs based on conditions."
    },
    4: {
        "title": "Working with Lists and Dictionaries",
        "content": "Lists and dictionaries allow you to store and manage collections of data efficiently in Python."
    },
    5: {
        "title": "Functions and Code Reusability",
        "content": "Functions help you organize your code, avoid repetition, and make programs easier to maintain."
    },
    6: {
        "title": "Error Handling and Debugging",
        "content": "Using try and except blocks allows your program to handle errors gracefully without crashing."
    },
    7: {
        "title": "Introduction to Object-Oriented Programming",
        "content": "Object-oriented programming focuses on creating reusable objects that combine data and behavior."
    },
    8: {
        "title": "Working with Files in Python",
        "content": "Python makes it easy to read from and write to files, which is useful for storing persistent data."
    },
    9: {
        "title": "Building Simple APIs with FastAPI",
        "content": "FastAPI is a modern Python framework for building fast and scalable APIs with automatic documentation."
    },
    10: {
        "title": "Next Steps in Your Python Journey",
        "content": "After learning the basics, explore frameworks, databases, and real-world projects to grow your skills."
    }
}

@app.get("/posts")
def get_all_posts(Limit: int):

    if Limit and Limit <= len(text_posts):
        return list(text_posts.values())[:Limit]
    if Limit > len(text_posts):
        raise HTTPException(status_code=404, detail="Limit exceeds available posts")
    

@app.get("/posts/{post_id}")
def get_post(post_id: int):
    
    if post_id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(post_id)

@app.post("/posts")
def create_post(post: PostCreate):
    pass