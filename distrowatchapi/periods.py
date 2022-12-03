from enum import Enum


class PeriodType(str, Enum):
    LAST_WEEK = "1"
    LAST_MONTH = "4"
    LAST_THREE_MONTHS = "13"
    LAST_SIX_MONTHS = "26"
    LAST_YEAR = "52"
    AVERAGE_RATING = "score"
    MOST_RATINGS = "votes"
    TRENDING_PAST_YEAR = "trending-52"
    TRENDING_PAST_SIX_MONTHS = "trending-26"
    TRENDING_PAST_THREE_MONTHS = "trending-13"
    TRENDING_PAST_MONTH = "trending-4"
    TRENDING_PAST_WEEK = "trending-1"
