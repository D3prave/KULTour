from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)

# Load the DataLoader and CollaborativeFiltering objects
with open('backend/data_loader.pkl', 'rb') as f:
    loader = pickle.load(f)

with open('backend/collab_filtering.pkl', 'rb') as f:
    collab_filtering = pickle.load(f)

# Define Resources
@app.route('/data', methods=['GET'])
def get_data():
    data_frame = loader.get_dataframe()
    data_json = data_frame.to_json(orient='records')
    return jsonify(data_json)

@app.route('/train_test_data', methods=['GET'])
def get_train_test_data():
    x_train, x_test, y_train, y_test = loader.get_train_test_data()
    response = {
        'x_train': x_train.to_json(orient='records'),
        'x_test': x_test.to_json(orient='records'),
        'y_train': y_train.to_json(orient='records'),
        'y_test': y_test.to_json(orient='records')
    }
    return jsonify(response)

@app.route('/recommendation', methods=['POST'])
def get_recommendation():
    user_data = request.get_json()
    recommendation = collab_filtering.get_recommendation(user_data['user_id'])
    return jsonify({'recommendation': recommendation})

@app.route('/category', methods=['POST'])
def get_category():
    user_data = request.get_json()
    category = collab_filtering.get_category(user_data['user_id'])
    return jsonify({'category': category})

if __name__ == '__main__':
    app.run(debug=True)

