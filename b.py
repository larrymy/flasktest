
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


@app.route('/hi', methods=['POST'])
def create_task():
	data = request.json
	dd = data["file2"]
	df = pd.DataFrame(dd)

	df.columns = df.columns.map(lambda x: re.sub(r'\W+', '', x))

	a = DplyFrame(df)
	aa = a >> mutate(name=X.FullNameBilling.str.upper()) >> group_by(X.name) >> summarize(contact = X.PhoneBilling.head(1),
		email = X.EmailBilling.head(1),
        address = X.Address2Billing.head(1),
        num_items_purchased = (X.name).count()
        ) 
	jsondf = aa.to_json(orient='records')

	return (jsondf);

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='127.0.0.1', port=port)