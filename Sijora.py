from Setting import *
import json

# initalisation DB
db = SQLAlchemy(app)


class Sentiment(db.Model):
    __tablename_ = 'sijora'
    id = db.Column(db.Integer, primary_key=True)
    input_mobile = db.Column(db.String(80), nullable=False)
    output_positive = db.Column(db.String(80), nullable=True)
    output_negative = db.Column(db.String(80), nullable=True)

    def json(self):
        return{
            'id':self.id,
            'input_mobile':self.input_mobile ,
            'output_positive':self.output_positive,
            'output_negative':self.output_negative
        }

    def add_sentiment(_input_mobile, _output_positive, _output_negative):
        new_sentiment = Sentiment(input_mobile=_input_mobile, output_positive=_output_positive, output_negative=_output_negative)
        db.session.add(new_sentiment)
        db.session.commit()

    def get_all_sentiment():
        return [Sentiment.json(sentiment) for sentiment in Sentiment.query.all()]

    def get_sentiment(_id):
        return [Sentiment.json(Sentiment.query.filter_by(id=_id).first())]

    def update_sentiment(_id, _input_mobile, _output_positive, _output_negative):
        sentiment_to_update = Sentiment.query.filter_by(id=_id).first()
        sentiment_to_update.input_mobile = _input_mobile
        sentiment_to_update.output_positive = _output_positive
        sentiment_to_update.output_negative = _output_negative
        db.session.commit()   

    def delete_sentiment(_id):
        '''function to delete a movie from our database using
           the id of the movie as a parameter'''
        Sentiment.query.filter_by(id=_id).delete()
        # filter movie by id and delete
        db.session.commit()  # commiting the new change to our database