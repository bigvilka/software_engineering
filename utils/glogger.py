from gunicorn.glogging import Logger as GLogger
from config import Config
import logstash

handler = logstash.TCPLogstashHandler(
    Config.LOGSTASH_HOST,
    Config.LOGSTASH_PORT,
    tags=['api']
)


class GunicornLogger(GLogger):
    def setup(self, cfg):
        super(GunicornLogger, self).setup(cfg)
        self.access_log.addHandler(handler)
        self.error_log.addHandler(handler)
