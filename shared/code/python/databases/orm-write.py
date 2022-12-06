from sqlalchemy.orm import Session

with Session(engine) as session:
    hugo = User(name="hugo", fullname="Hugo Mougard")
    john = User(name="john", fullname="John Doe")

    session.add_all([hugo, john])

    session.commit()
