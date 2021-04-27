"""This Module contains all files ie images , pdf , docs  etc , from chancellor college
Official website. Some files can only be accessed once a student has logged into his/ her
account since The files are specific to a student .
 """

def get_portal_display_image(reg_number):
    try:
         return "https://portal.cc.ac.mw/students/images/scripts/display_image.php?id={}".format(reg_number)

    except Exception as _:
        return "https://freepikpsd.com/wp-content/uploads/2019/10/no-image-png-5-Transparent-Images.png"
