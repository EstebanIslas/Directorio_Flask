from flask import Blueprint, render_template, request, redirect, url_for
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def home():
    contacts = Contact.query.all() #Select * from
    return render_template('index.html', contacts = contacts)

@contacts.route('/new', methods=['POST'])
def add_contacts():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    new_contact = Contact(fullname, email, phone)
    
    db.session.add(new_contact)
    db.session.commit()

    return redirect(url_for('contacts.home'))

@contacts.route('/update/<id>', methods=['POST', 'GET'])
def update_contacts(id):

    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        return redirect(url_for('contacts.home'))

    return render_template('update.html', contact = contact)

@contacts.route('/delete/<id>', methods = ['POST', 'GET'])
def delete_contacts(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    return redirect(url_for('contacts.home'))