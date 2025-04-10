import os

LANDING_PAGE_URL = os.getenv("LANDING_PAGE_URL", "https://useinsider.com/") # PREFERABLY SET IN ENV VARS IN PIPELINE
CAREERS_QA_PAGE_URL = os.getenv("CAREERS_QA_PAGE_URL", "https://useinsider.com/careers/quality-assurance/")
OPEN_POSITIONS_PAGE_URL = os.getenv("OPEN_POSITIONS_PAGE_URL", "https://useinsider.com/careers/open-positions")