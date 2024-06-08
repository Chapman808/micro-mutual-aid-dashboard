import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  #SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
  #FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

  @staticmethod
  def init_app(app):
    pass
 
class DevelopmentConfig(Config):
  DEBUG = True

class ProductionConfig(Config):
  pass

config = {
  'development': DevelopmentConfig,
  'production': ProductionConfig,
  'default': DevelopmentConfig
}