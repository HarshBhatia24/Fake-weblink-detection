from flask import Flask, request, jsonify, send_file
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Load datasets
safe_data = pd.read_csv('safe-urls.csv')
scam_data = pd.read_csv('scam-urls.csv')

# Combine datasets
data = pd.concat([safe_data, scam_data])

# Feature extraction
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['url'])
y = data['label'].apply(lambda x: 1 if x == 'Scam' else 0)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

# Train model
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)


@app.route('/')
def index():
    return send_file('frontend.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if request has JSON data
        if not request.json:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        # Check if URL is provided
        if 'url' not in request.json:
            return jsonify({'error': 'URL parameter is required'}), 400
        
        url = request.json['url']
        
        # Check if URL is not empty
        if not url or not url.strip():
            return jsonify({'error': 'URL cannot be empty'}), 400
        
        # Transform URL and make prediction
        url_vector = vectorizer.transform([url])
        prediction = model.predict(url_vector)
        result = 'Scam' if prediction[0] == 1 else 'Safe'
        
        return jsonify({'url': url, 'result': result})
        
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid data format: {str(e)}'}), 400
    except AttributeError as e:
        return jsonify({'error': 'Model or vectorizer not properly initialized'}), 500
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
