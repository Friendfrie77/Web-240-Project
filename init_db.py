#use when db changes and need to start fresh
from flask import Flask
from app import app, db, Cats, Jobs
from sqlalchemy import inspect, select, exists
import xml.etree.ElementTree as ET

def init_db():
    #check if db is active
    with app.app_context():
        inspector = inspect(db.engine)
        current_tables = inspector.get_table_names
        for tables in db.metadata.sorted_tables:
            if tables.name not in current_tables:
                tables.create(db.engine)

def populate_db():
    try:
        catXML = "static/xml/cats_feed.xml"
        jobsXML = "static/xml/jobs.xml"
        xmlList = [catXML, jobsXML]
        for i in xmlList:
            tree = ET.parse(i)
            root = tree.getroot()
            if root.tag == 'CatsCollection':
                for cats in root.findall('Cat'):
                    name = cats.find('txtCatName').text
                    about = cats.find('txtCatAbout').text
                    gender = cats.find('txtCatGender').text
                    imgPath = cats.find('txtCatImg').text
                    with app.app_context():
                        res = db.session.query(db.session.query(Cats).filter_by(txtCatName = name).exists()).scalar()
                        if not res:
                            cat = Cats(txtCatName = name, txtCatGender= gender, txtCatAbout = about, txtCatImg= imgPath)
                            db.session.add(cat)
                            db.session.commit()
            if root.tag == 'Jobs':
                #check amount of jobs and check it vs xml
                for jobs in root.findall('Job'):
                    job = jobs.find('txtJobName').text
                    with app.app_context():
                        res = db.session.query(db.session.query(Jobs).filter_by(txtJobName = job).exists()).scalar()
                        if not res:
                            des = jobs.find('txtJobdes').text
                            imgPath = jobs.find('txtJobpic').text
                            alt = jobs.find('txtImgalt').text
                            job = Jobs(txtJobName = job, txtJobdes= des, txtJobpic= imgPath, txtImgalt = alt)
                            db.session.add(job)
                            db.session.commit()
    except FileNotFoundError:
        print('file not found')
if __name__ == "__main__":
    # init_db()
    populate_db()