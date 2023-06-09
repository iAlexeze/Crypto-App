from flask import Flask, jsonify, render_template, request
from pycoingecko import CoinGeckoAPI
import redis
import socket 


app = Flask(__name__, static_folder='')

# Initialize CoinGecko API
cg = CoinGeckoAPI()

# Initialize Redis connection
redis_db = redis.Redis()

# Fetch crypto prices from CoinGecko API
crypto_prices = cg.get_price(ids='bitcoin,ethereum,binancecoin,ripple,kucoin-shares,cardano,solana,tron', vs_currencies='usd')

# Extract the individual prices
bitcoin_price = crypto_prices['bitcoin']['usd']
ethereum_price = crypto_prices['ethereum']['usd']
bnb_price = crypto_prices['binancecoin']['usd']
xrp_price = crypto_prices['ripple']['usd']
kucoin_price = crypto_prices['kucoin-shares']['usd']
cardano_price = crypto_prices['cardano']['usd']
solana_price = crypto_prices['solana']['usd']
tron_price = crypto_prices['tron']['usd']

# # Define the IP and Hostname
# def getIP(): 
#     hostname = socket.gethostname() 
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
#     s.connect(("8.8.8.8", 80)) 
#     ip = s.getsockname()[0] 
#     print(ip) 
#     s.close() 
#     return str(hostname),str(ip) 
# @app.route("/") 
# def index(): 
#     hostname,ip = getIP() 
#     return render_template('index.html',hostname=hostname,ip=ip) 

# Route for serving the index.html file
@app.route('/')
def index():
    # Get the hostname and IP address of the container
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    return render_template('index.html', hostname=hostname, ip=ip)


# Route for providing the cryptocurrency prices as JSON data
@app.route('/api/crypto-prices')
def get_prices():
    crypto_prices = {
        'bitcoin': bitcoin_price,
        'ethereum': ethereum_price,
        'bnb': bnb_price,
        'xrp': xrp_price,
        'kucoin': kucoin_price,
        'cardano': cardano_price,
        'solana': solana_price,
        'tron': tron_price
    }
    return jsonify(crypto_prices)


@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    favorite_coin = request.form.get('favorite-coin')
    comment = request.form.get('comment')

    # Process and store the form data in Redis or perform any other required actions

    return 'Success'  # Return a response to indicate the form submission was successful

    # Validate form inputs
    if not name or not phone or not email or not favorite_coin:
        return 'Please fill in all required fields.', 400

    # Store form data in Redis
    submission_id = redis_db.incr('submission_id')
    submission_key = f'submission:{submission_id}'
    submission_data = {
        'name': name,
        'phone': phone,
        'email': email,
        'favorite_coin': favorite_coin,
        'comment': comment
    }
    redis_db.hmset(submission_key, submission_data)

    return 'Form submitted successfully.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

