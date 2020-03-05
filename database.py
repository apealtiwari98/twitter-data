from sqlalchemy import create_engine,Column,String,Boolean,Integer,Numeric,ARRAY,DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'twitter_data'
    id=Column(Integer, primary_key=True)
    tweet_created_at =Column('tweet_created_at', DateTime)
    tweet_keyword =Column('tweet_keyword', String(100))
    tweet_id=Column('tweet_id', String(32))
    tweet_text=Column('tweet_text', String(500))
    tweet_retweet_count=Column('tweet_retweet_count', Integer)
    tweet_favorite_count=Column('tweet_favorite_count', Integer)
    tweet_hashtags_used=Column('tweet_hashtags_used',ARRAY(String))
    tweet_symbols_used=Column('tweet_symbols_used',ARRAY(String))
    tweet_users_mentioned=Column('tweet_users_mentioned',ARRAY(String))
    tweet_user_screen_name=Column('tweet_user_screen_name', String(100))
    tweet_user_name=Column('tweet_user_name', String(100))
    tweet_user_verified=Column('tweet_user_verified', Boolean)
    tweet_location=Column('tweet_location', String(100))
    tweet_possibly_sensitive=Column('tweet_possibly_sensitive', Boolean)


engine = create_engine('postgresql://upwork:upwork@coin-market.cuovmdkoy4e4.us-east-1.rds.amazonaws.com:5432/coinmarket')

#Create Schema into Database
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
