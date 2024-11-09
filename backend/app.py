from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from data_loader import DataLoader
from collab_filtering import CollaborativeFiltering

app = Flask(__name__)
api = Api(app)

# Initialize DataLoader
loader = DataLoader('backend/prepared_data.csv')

# Define Resources
class Data(Resource):
    def get(self):
        data_frame = loader.get_dataframe()
        data_json = data_frame.to_json(orient='records')
        return jsonify(data_json)

class TrainTestData(Resource):
    def get(self):
        x_train, x_test, y_train, y_test = loader.get_train_test_data()
        response = {
            'x_train': x_train.to_json(orient='records'),
            'x_test': x_test.to_json(orient='records'),
            'y_train': y_train.to_json(orient='records'),
            'y_test': y_test.to_json(orient='records')
        }
        return jsonify(response)

class Recommendation(Resource):
    def post(self):
        user_data = request.get_json()
        collaborative_filtering = CollaborativeFiltering(loader)
        recommendation = collaborative_filtering.get_recommendation(user_data['user_id'])
        return jsonify({'recommendation': recommendation})

class DataVisualization(Resource):
    def get(self):
        # Assuming you have a function in data_visualization.py to generate plots and save them as images
        from data_visualization import generate_plots
        generate_plots()
        return jsonify({'status': 'Plots generated'})

# Add Resources to API
api.add_resource(Data, '/data')
api.add_resource(TrainTestData, '/train_test_data')
api.add_resource(Recommendation, '/recommendation')
api.add_resource(DataVisualization, '/visualize')

if __name__ == '__main__':
    app.run(debug=True)
