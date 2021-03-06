import json
import pandas as pd
import collections as col
from constants.dash_constants import BASICS_PATH, DAILY_TWEETS_PATH, HASHTAGS_PATH, MENTIONS_PATH, \
    POTENTIALLY_SENSITIVE_TWEETS_COUNT_PATH, POTENTIALLY_SENSITIVE_TWEETS_PATH, \
    POTENTIALLY_SENSITIVE_TWEETS_DEFAULT_PERCENTILE, \
    SENTIMENTS_PATH
from constants.country_config import COUNTRY_ALTS, COUNTRY_CODE


def get_date_range(tweets):
    '''
        Returns the min and max date of the collected tweets
    '''
    max_date = tweets['tweet_date'].max()
    min_date = tweets['tweet_date'].min()
    return min_date, max_date


def generate_dash_basic_stats(tweets, save=False, basics_save_path=BASICS_PATH):
    '''
        Returns total_tweets, min_date, max_date, users_count, avg_tweets
    '''
    total_tweets = len(tweets)

    min_date, max_date = get_date_range(tweets)

    daily_tweets_count = tweets.groupby(
        'tweet_date')['tweet_id'].count().reset_index(name='count')
    avg_tweets = sum(daily_tweets_count['count']) / \
        len(daily_tweets_count['count'])

    users = tweets['user_id_x'].nunique()

    basic = {
        'total_tweets': total_tweets,
        'min_date': min_date,
        'max_date': max_date,
        'users_count': users,
        'avg_tweets': int(avg_tweets)
    }

    if save:
        with open(basics_save_path, 'w') as fp:
            json.dump(basic, fp)
            print('Saved:', basics_save_path)
            print('total_tweets, min_date, max_date, users_count, avg_tweets')
    return basic


def generate_dash_daily_tweets(tweets, save=False, daily_tweets_save_path=DAILY_TWEETS_PATH):
    daily_tweets = tweets.groupby(
        'tweet_date')['tweet_id'].count().reset_index(name='count')
    if save:
        pd.DataFrame.to_csv(daily_tweets, daily_tweets_save_path)
        print("Saved:", daily_tweets_save_path)

    return daily_tweets


def generate_dash_hashtags(tweets, from_date, to_date, save=False, hashtags_save_path=HASHTAGS_PATH, top_hash_count=20):
    min_date, max_date = get_date_range(tweets)
    if not from_date:
        from_date = min_date
    if not to_date:
        to_date = max_date

    # filtering tweets in the date range
    tweets_hashtags = tweets[tweets['entity_hashtags'].notna(
    ) & tweets['tweet_date'].between(from_date, to_date, inclusive='both')]['entity_hashtags']

    hashtags = []

    # joining all the country name alternatives 
    country_alts_str = '|'.join(COUNTRY_ALTS)
    
    # creating list of hashtags
    for h in tweets_hashtags:
        h_list = [hh for hh in h.split(
            # excluding the country name alternatives 
            '|') if COUNTRY_CODE and (hh not in country_alts_str)]
        hashtags.extend(h_list)

    # counting hashtags and sorting them by count
    count_hashtags = col.Counter(hashtags).most_common()

    # getting the top hashtags by frequency
    hashtags = [c[0] for c in count_hashtags[:top_hash_count]]
    counts = [c[1] for c in count_hashtags[:top_hash_count]]

    # data for the dashboard
    hashtags_data = {
        "counts": counts[::-1],
        "hashtag": hashtags[::-1]
    }

    df_hashtags_data = pd.DataFrame(data=hashtags_data)

    if save:
        pd.DataFrame.to_csv(df_hashtags_data, hashtags_save_path)
        print("Saved:", hashtags_save_path)

    return df_hashtags_data


def generate_dash_mentions(tweets, from_date, to_date, save=False, mentions_save_path=MENTIONS_PATH, top_mentions_count=20):
    min_date, max_date = get_date_range(tweets)
    if not from_date:
        from_date = min_date
    if not to_date:
        to_date = max_date

    # filtering tweets in the date range
    tweets_mentions = tweets[tweets['entity_mentions'].notna(
    ) & tweets['tweet_date'].between(from_date, to_date, inclusive='both')]['entity_mentions']

    mentions = []

    # getting the top mentions by frequency
    for m in tweets_mentions:
        m_list = [mm for mm in m.split('|')]
        mentions.extend(m_list)

    count_mentions = col.Counter(mentions).most_common()
     # getting the top mentions by frequency
    mentions = [c[0] for c in count_mentions[:top_mentions_count]]
    counts = [c[1] for c in count_mentions[:top_mentions_count]]

    # Saving data for the dashboard
    mentions_data = {
        "counts": counts[::-1],
        "mention": mentions[::-1]
    }

    df_mentions_data = pd.DataFrame(data=mentions_data)

    if save:
        pd.DataFrame.to_csv(df_mentions_data, mentions_save_path)
        print("Saved:", mentions_save_path)

    return df_mentions_data


def generate_dash_sentiments(tweets, from_date, to_date, save=False, sentiments_save_path=SENTIMENTS_PATH):
    min_date, max_date = get_date_range(tweets)
    if not from_date:
        from_date = min_date
    if not to_date:
        to_date = max_date
    
    # filtering tweets by date range
    # getting sentiment distribution for positive, negative and neutral categories
    df_sentiments = tweets[tweets['tweet_date'].between(from_date, to_date, inclusive='both')] \
        .value_counts(subset=['tweet_sentiment']).reset_index(name='count').sort_values(['count'], ascending=False)

    if save:
        pd.DataFrame.to_csv(df_sentiments, sentiments_save_path)
        print("Saved:", sentiments_save_path)
    return df_sentiments


def generate_dash_potentially_sensitive_tweets(tweets, save=False,
                                               pst_count_save_path=POTENTIALLY_SENSITIVE_TWEETS_COUNT_PATH,
                                               pst_tweets_save_path=POTENTIALLY_SENSITIVE_TWEETS_PATH,
                                               percentile=POTENTIALLY_SENSITIVE_TWEETS_DEFAULT_PERCENTILE):
    
    # filter tweets marked as potentially sensitive
    tweets_pst = tweets[tweets['tweet_possibly_sensitive'] == True]
    # counting potentially sensitive tweets by date
    c_tweets_pst = tweets_pst.value_counts(subset=['tweet_date']).reset_index(name='count') \
        .sort_values(['tweet_date'], ascending=False)
    # getting potentially sensitive tweets and their dates
    pst_tweets = tweets_pst[['tweet_date', 'processed_tweet_text']]

    if save:
        pd.DataFrame.to_csv(c_tweets_pst, pst_count_save_path)
        pd.DataFrame.to_csv(pst_tweets, pst_tweets_save_path)
        print("Saved:", pst_count_save_path, pst_tweets_save_path)

    return (c_tweets_pst, pst_tweets)
