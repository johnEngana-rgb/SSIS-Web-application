from ssis_app.models.student import Student
from ssis_app.models.course import Course
from werkzeug.utils import secure_filename
import cloudinary.uploader as cloud


def add_student_to_db(student: list):
    id = student['id'].strip()
    firstname = (student['firstname'].strip()).title()
    middlename = (student['middlename'].strip()).title()
    lastname = (student['lastname'].strip()).title()
    gender = student['gender'].strip()
    yearlevel = student['yearlevel']
    course = student['course']
    photo = student['photo']
    # ID validation
    if id:
        if id not in Student().get_IDs():
            # Name validation
            if firstname and lastname:
                Student(
                    id=id, 
                    firstName=firstname, 
                    middleName=middlename, 
                    lastName=lastname,
                    yearLevel=yearlevel,
                    gender=gender,  
                    course=Course().get_coursecode_for(course),
                    college=Course().get_collegecode(course),
                    photo = photo
                ).add_new()
                return True
            else:
                return False
        else:
            return False


def update_student_record(student: list = None):
    id = student['id'].strip()
    firstname = student['firstname'].strip()
    middlename = student['middlename'].strip()
    lastname = student['lastname'].strip()
    gender = student['gender'].strip()
    yearlevel = student['yearlevel']
    course = student['course']
    photo = student['photo']
    
    if firstname and lastname:
        if photo:
            Student(
                id=id, 
                firstName=firstname,
                middleName=middlename, 
                lastName=lastname,
                photo=photo,
                yearLevel=yearlevel,
                gender=gender, 
                course=Course().get_coursecode_for(course),
                college=Course().get_collegecode(course)
            ).update()
        else:
            Student(
                id=id, 
                firstName=firstname,
                middleName=middlename, 
                lastName=lastname,
                yearLevel=yearlevel,
                gender=gender, 
                course=Course().get_coursecode_for(course),
                college=Course().get_collegecode(course)
            ).update()
        return None
    else:
        return False


def save_image(file: str = None):
    result = cloud.upload(file, phash=True)
    url = result.get('secure_url')
    return url


def delete_image(id: str = None):
    image_url = (Student().get_image_url(id))[0]
    file_name = (image_url.split('/')[-1]).split('.')[0]
    cloud.destroy(file_name)
    return 


def check_page_limit(min: bool = None, max: bool = None):
    if min:
        return 'min'
    elif max:
        return 'max'
    else:
        return


def check_limit_validity(number_input: int = None, max_limit: int = None):
    if number_input < 5:
        return 5
    elif number_input > max_limit:
        return max_limit
    else:
        return number_input
    