from logger import Logger

logger = Logger.setup_logger()

try:
    from .api_domain import Covid19StatisticsConfig
    from .api_domain import FakeRestAPIConfig
    from .database import FakeDBConfig
except ImportError as e:
    logger.error(f"Import configurations error: {str(e)}")
    from .api_domain import Covid19StatisticsConfig
    from .api_domain import FakeRestAPIConfig
    from .database import FakeDBConfig