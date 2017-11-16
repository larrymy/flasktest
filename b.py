
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
import os
import pandas as pd
from dplython import (DplyFrame, X, diamonds, select, sift, sample_n,
    sample_frac, head, arrange, mutate, group_by, summarize, DelayFunction) 
import json
import re

app = Flask(__name__)


def clean_df(requestjson):
	# data = request.json
	data = requestjson
	dd = data["file2"]
	df = pd.DataFrame(dd)

	df.columns = df.columns.map(lambda x: re.sub(r'\W+', '', x))
	a = DplyFrame(df)

	return(a)

def supp(datacategory):
	# print(list(datacategory))
	# datacategory = list(datacategory)
	supplier = ["Mr Rice Corner", "Pontian Noodle", "Meet Mee", "Lim Fried Chicken"]
	supplier2 = [element.lower() for element in supplier]


	# datacategory = ["Mr Rice Corner foo", "pontian noodle foobar", "bar lim fried chicken", "pontian noodle, cake"]
	# datacategory = [element.lower() for element in datacategory]
	x = datacategory.lower()
	for p, q in enumerate(supplier):
		# for i,x in enumerate(datacategory):
			if supplier2[p] in x:
				# datacategory[i] = supplier[p]
				datacategory = supplier[p]

	return datacategory

def most_common(lst):
    return max(set(lst), key=lst.count)


@app.route('/customer', methods=['POST'])
def create_task():
	df = clean_df(request.json)
	df_customer = df >> mutate(name=X.FullNameBilling.str.upper()) >> group_by(X.name) >> summarize(contact = X.PhoneBilling.head(1),
		email = X.EmailBilling.head(1),
        address = X.Address2Billing.head(1),
        num_items_purchased = (X.name).count()
        ) 
	jsondf = df_customer.to_json(orient='records')

	return (jsondf);


@app.route('/fav', methods=['POST'])
def create_task2():
	df = clean_df(request.json)
	print(df["Category"])	
	df['supplier'] = df['Category'].apply(lambda x: supp(x))
	df = DplyFrame(df) >> group_by(X.supplier) >> summarize(max1 = most_common( X.Name ) ) 

	print(df)
	# df_fav = df >> mutate(new = supp(X.Category))
	jsondf = df.to_json(orient='records')

	return (jsondf);


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='127.0.0.1', port=port)