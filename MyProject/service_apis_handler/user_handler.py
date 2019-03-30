from MyProject.db.user_models.models import User


def get_user_json(user_object):
    return {
                "userName": user_object.userid,
                "firstName": user_object.fname,
                "middleName": user_object.mname,
                "lastName": user_object.lname,
                "phone": user_object.phone,
                "createdOn": user_object.created_on.strftime('%d/%m/%y'),
            }

def get_user_by_username(username):
    try:
        return User.objects.get(userid=username)
    except:
        raise Exception()

def get_user_by_filter(criteria={}):
    return User.objects.filter(**criteria)

def create_user(bodyparams):
    try:
        return User.objects.create(userid=bodyparams['username'], fname=bodyparams['firstname'],
                        mname=bodyparams['middlename'], lname=bodyparams['lastname'],
                        phone=bodyparams['phone'], password=bodyparams['password'])
    except:
        raise Exception()