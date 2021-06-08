from Sijora import *

@app.route('/sentiment', methods=['GET'])
def get_sentiment():
    '''Function to get all the movies in the database'''
    return jsonify({'Sijora': Sentiment.get_all_sentiment()})


# route to get movie by id
# @app.route('/sentiment/<int:id>', methods=['GET'])
# def get_sentiment_by_id(id):
#     return_value = Sentiment.get_sentiment(id)
#     return jsonify(return_value)
@app.route('/sentiment/<int:id>', methods=['GET'])
def get_sentiment_by_id(id):
    return_value = Sentiment.get_sentiment(id)
    return jsonify({'Sijora' : return_value})


# route to add new movie
@app.route('/sentiment', methods=['POST'])
def add_sentiment():
    '''Function to add new movie to our database'''
    request_data = request.get_json()  # getting data from client
    Sentiment.add_sentiment(request_data["input_mobile"], request_data["output_positive"],
                    request_data["output_negative"])
    response = Response("Sentiment added", 201, mimetype='application/json')
    return response


# route to update movie with PUT method
@app.route('/sentiment/<int:id>', methods=['PUT'])
def update_sentiment(id):
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    Sentiment.update_sentiment(id, request_data["input_mobile"], request_data["output_positive"],
                    request_data["output_negative"])
    response = Response("Sentiment Updated", status=200, mimetype='application/json')
    return response


# route to delete movie using the DELETE method
@app.route('/sentiment/<int:id>', methods=['DELETE'])
def remove_sentiment(id):
    '''Function to delete movie from our database'''
    Sentiment.delete_sentiment(id)
    response = Response("Sentiment Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)
