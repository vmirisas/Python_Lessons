def create_person(**kwargs):
    print(kwargs)
    return kwargs

create_person(name="Jim", occupation="Teacher")
create_person(name="Bruce", ability="fly")