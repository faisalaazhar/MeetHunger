from lib2to3.pgen2.token import EQUAL
from urllib import request
from app import *
import stripe

public_key = "	pk_test_51LcHrBSCYTwdqfA3okrXWJOUHLhRCtEXBdThqkZQIyWVld0s65qCSsIpVoW3r9e066xNhkiU71AXpqhpi9iSBsQv00V6QnozwH"
stripe.api_key = "sk_test_51LcHrBSCYTwdqfA3DdEHK1CbHyeDJf7oAwMkv5m2qL1329OmPLlOSsjjISJqXpGUIYvLnL1zufXGVQZ9MaIBto0d00Omovn6ku"
app.secret_key = "testing"

@app.route('/confirm', methods=['GET','POST'])
def confirm():
    amount = session["amount"]
    amount = int(amount)
    session.pop("amount", None)
    return render_template('payment.html',public_key=public_key,amount=amount)

@app.route('/donate', methods=['GET','POST'])
def donate():
    amount = ""
    if "username" in session:
        if request.method=='POST':
            if request.form["btn"]=="#":
                amount = request.form["amount"]
                if amount == "":
                    amount = 0
                session["amount"]=amount
                return redirect(url_for("confirm"))
            elif request.form["btn"]=="*":
                 date = request.form["date"]
                 location = request.form["location"]
                 name = session["username"]
                 user_input = {'name': name, 'location': location, 'date': date}
                 db_money.insert_one(user_input)
                 return redirect(url_for("donate"))
        return render_template('donate.html')
    else:
        return redirect(url_for("login"))

@app.route('/payment', methods=['POST'])
def payment():
    customer = stripe.Customer.create(
        email=request.form['stripeEmail'],
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return "Thank You"

@app.route('/donateFood', methods=['GET','POST'])
def donateFood():
    if request.method=='POST':
        amount = request.form["amount"]
        session["amount"]=amount
        return redirect(url_for("confirm"))
    return render_template('donate.html')
