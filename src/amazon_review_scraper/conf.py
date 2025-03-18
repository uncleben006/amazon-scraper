"""
    Config module for amazon_review_scraper.
"""

from pydantic_settings import BaseSettings


class AmazonReviewScraperSettings(BaseSettings):
    """Settings class for Amazon Review Scraper"""

    def get_amazon_product_url(self, asin_code: str) -> str:
        """Returns an Amazon product URL for a given ASIN code."""
        return f"https://www.amazon.com/dp/{asin_code}"
    
    def get_amazon_product_reviews_url(self, asin_code: str) -> str:
        """Returns an Amazon product URL for a given ASIN code."""
        return f"https://www.amazon.com/product-reviews/{asin_code}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=1"


amazon_review_scraper_settings = AmazonReviewScraperSettings()
