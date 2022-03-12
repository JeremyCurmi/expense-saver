import logging

from app.migrations import initialize_db
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init() -> None:
    db = SessionLocal()
    initialize_db(db)

def main() -> None:
    logger.info("Initializing data ...")
    init()
    logger.info("Data has been initialized ✅")

if __name__ == '__main__':
    main()