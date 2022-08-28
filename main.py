from utils.mal import PlayerScrapper
import time
from sqlalchemy import create_engine


if __name__=='__main__':
    bot = PlayerScrapper(headless=True)
    bot.search_team('PSG')
    time.sleep(2)
    psg_info = bot.get_info()
    print("Connecting to DB")
    engine = create_engine('postgresql+psycopg2://postgres:Popcorn24@football.cmoodcpdgod3.ap-south-1.rds.amazonaws.com:5432/football')
    psg_info.to_sql('rsg_info',engine,if_exists='append')