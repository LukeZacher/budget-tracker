from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

transactions = []

@app.route('/')
def index():
    total = sum(t['amount'] for t in transactions)
    return render_template('index.html', transaction_list=transactions, balance=total)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    amount = float(request.form['amount'])
    description = request.form['description']
    transaction_type = request.form['type']

    if transaction_type == 'expense':
        amount = -amount

    transaction = {
        'amount': amount,
        'display_amount': "${:,.2f}".format(abs(amount)),
        'description': description,
        'type': transaction_type,
        'date': datetime.now()
    }

    transactions.append(transaction)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)