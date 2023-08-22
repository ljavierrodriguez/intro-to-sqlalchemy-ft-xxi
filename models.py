Base, declarative_base, Table, relationship, Column, Integer, Boolean, String, Text, DateTime, Float, ForeignKey = None

# SQLAlchemy ORM 

Base = declarative_base()
from datetime import datetime


categories_articles = Table(
    'categories_articles', 
    Column('articles_id', Integer, ForeignKey('articles.id'), primary_key=True),  
    Column('categories_id', Integer, ForeignKey('categories.id'), primary_key=True)    
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), default="")
    username = Column(String(120), nullable=False, unique=True)
    password = Column(String(120), nullable=False)
    active = Column(Boolean(), default=True)
    profile = relationship('Profile', useList=False, backref="user") # [<Profile 1>] => <Profile 1>


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    biography = Column(String, default="")
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    
class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False, unique=True)
    resume = Column(String(300), nullable=False)
    content = Column(Text(), nullable=False)
    published = Column(DateTime(), default=datetime.now)
    is_draft = Column(Boolean(), default=True)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', backref="articles")
    categories = relationship('Category', secondary=categories_articles)
    
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    active = Column(Boolean(), default=True)
    articles = relationship('Article', secondary=categories_articles)