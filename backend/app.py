from flask import Flask, jsonify, request
import pickle
from collab_filt_svd import CollaborativeFiltering

app = Flask(__name__)

# Initialize the CollaborativeFiltering object
collab_filtering = CollaborativeFiltering('backend/prepared_data.csv')

# Define Resources
@app.route('/data', methods=['GET'])
def get_data():
    data_frame = collab_filtering.data
    data_json = data_frame.to_json(orient='records')
    return jsonify(data_json)

@app.route('/train_test_data', methods=['GET'])
def get_train_test_data():
    x_train, x_test, y_train, y_test = collab_filtering.trainset, collab_filtering.testset, collab_filtering.trainset, collab_filtering.testset
    response = {
        'x_train': x_train,
        'x_test': x_test,
        'y_train': y_train,
        'y_test': y_test
    }
    return jsonify(response)

@app.route('/recommendation', methods=['POST'])
def get_recommendation():
    user_data = request.get_json()
    recommendations_df = collab_filtering.get_recommendations()
    recommendations_json = recommendations_df.to_json(orient='records')
    return jsonify({'recommendations': recommendations_json})

@app.route('/category', methods=['POST'])
def get_category():
    user_data = request.get_json()
    recommendations_df = collab_filtering.get_recommendations()
    user_recommendations = recommendations_df[recommendations_df['country'] == user_data['user_id']]
    category = user_recommendations['eventName'].iloc[0] if not user_recommendations.empty else "No recommendations available"
    return jsonify({'category': category})

if __name__ == '__main__':
    app.run(debug=True)