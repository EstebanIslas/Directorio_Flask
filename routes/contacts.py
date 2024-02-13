from flask import Blueprint, render_template, request, redirect
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def home():
    return render_template('index.html')

@contacts.route('/new', methods=['POST'])
def add_contacts():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    new_contact = Contact(fullname, email, phone)
    
    db.session.add(new_contact)
    db.session.commit()

    return redirect('/')

@contacts.route('/update')
def update_contacts():
    return 'Update contacts'

@contacts.route('/delete')
def delete_contacts():
    return 'Delete contacts'