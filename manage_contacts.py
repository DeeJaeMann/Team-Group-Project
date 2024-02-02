#Contact list structure Last-First-PhoneNumber-Email
contact_list = []
    


def create_contact():
    default_contact_form = {
        'last_name':  None,
        'first_name': None,
        'phone_number': None,
        'email_adress': None
    }
    # loop through default and let user input for the various keys
    default_contact_form['last_name'] = input('What is the last name? ')
    default_contact_form['first_name'] = input('What is the first name? ')
    default_contact_form['phone_number'] = input('What is the phone number? ')
    default_contact_form['email_adress'] = input('What is the email adress? ')
    print('default form', default_contact_form)
    contact_list.append(default_contact_form)
    print('contacts', contact_list)
    # append to contact list


create_contact()  
create_contact()    

# yeah you could try that. 
# I might have done before what I'm trying to do in JS and it may not be possible in Python so I'm gonna try changing the contact list to a list

# but it put you twice...
# i think it's fixed now
