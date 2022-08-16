from utils.mal import PlayerScrapper
import time

if __name__=='__main__':
    bot = PlayerScrapper("https://www.transfermarkt.com")
    bot.accept_cookies()
    time.sleep(4)
    bot.search_team('PSG')
    time.sleep(4)