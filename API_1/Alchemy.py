from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, Date, DATETIME, DateTime, TIME, Time
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
class Casedata(Base):
    __tablename__ = "Casedata"
    Sr_no = Column("SrNo.",Integer, primary_key=True, autoincrement=True)
    Court_name = Column("Court Name", String)
    Scrap_type = Column("Scrap type", Integer)
    Court_link = Column("Court Link", String)
    Response_Status_code = Column("Response Status Code", Integer)
    Site_Status = Column("Site Status", String)
    Date_and_Time = Column("Date and Time", DateTime)
    Error = Column("Error Displayed", String, nullable=True, default=None)


    def __init__(self,court_name,scrape_type,court_link,response_status_code,site_status,date_and_time,error):
        self.Court_name = court_name
        self.Scrap_type = scrape_type
        self.Court_link = court_link
        self.Response_Status_code = response_status_code
        self.Site_Status = site_status
        self.Date_and_Time = date_and_time
        self.Error = error

    def __repr__(self):
        return f"Court Name:{self.Court_name}, Scrap Type:{self.Scrap_type}, Court Link::{self.Court_link}, Response Status Code:{self.Response_Status_code}, Site Status:{self.Site_Status}, Date and Time:{self.Date_and_Time}, Error:{self.Error}"

engine = create_engine("sqlite:///db.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
