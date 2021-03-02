import unittest
import os
import shutil
#import tempfile
#import requests_mock
import glob
from instagram_scraper.app import InstagramScraper
from instagram_scraper.constants import *

class InstagramTests():

    def setUp(self):
        #fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures')

        #fixture_files = glob.glsob(os.path.join(fixtures_path, '*'))

        #for file_path in fixture_files:
        #    basename = os.path.splitext(os.path.basename(file_path))[0]
        #    self.__dict__[basename] = open(file_path).read()

        # This is a max id of the last item in response_first_page.json.
        #self.max_id = "1369793132326237681_50955533"

        self.test_dir = './temp'

        #tags = ['내가웃는게태교다']
        #tags = ['신생아가디건']
        tags = ['생후55일']
        #tags = ['기내에서맥주먹는느낌내봤지모야']

        args = {
            'usernames': tags,
            'destination': self.test_dir,
            'login_user': 'alethio.a01',
            'login_pass': 'dhtlfpdkf3#',
            'quiet': False,
            'maximum': 100000,
            'retain_username': False,
            'media_metadata': False,
            'media_types': ['image'],
            'latest': False
        }

        self.scraper = InstagramScraper(**args)

        

    def tearDown(self):
        shutil.rmtree(self.test_dir)


it = InstagramTests()
it.setUp()
it.scraper.scrape_hashtag()






