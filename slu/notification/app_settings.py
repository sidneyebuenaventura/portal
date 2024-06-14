from slu.framework.utils import get_config

MESSAGE_ADMIN_PORTAL_URL = get_config("NOTIFICATION_MESSAGE_ADMIN_PORTAL_URL")
MESSAGE_STUDENT_PORTAL_URL = get_config("NOTIFICATION_MESSAGE_STUDENT_PORTAL_URL")
MESSAGE_IT_DEPARTMENT_EMAIL = get_config("NOTIFICATION_MESSAGE_IT_DEPARTMENT_EMAIL")
MESSAGE_IT_DEPARTMENT_PHONE = get_config("NOTIFICATION_MESSAGE_IT_DEPARTMENT_PHONE")
MESSAGE_STUDENT_AFFAIRS_EMAIL = get_config("NOTIFICATION_MESSAGE_STUDENT_AFFAIRS_EMAIL")
MESSAGE_STUDENT_AFFAIRS_PHONE = get_config("NOTIFICATION_MESSAGE_STUDENT_AFFAIRS_PHONE")
MESSAGE_FINANCE_EMAIL = get_config("NOTIFICATION_MESSAGE_FINANCE_EMAIL")
MESSAGE_FINANCE_PHONE = get_config("NOTIFICATION_MESSAGE_FINANCE_PHONE")

FORMAT_DATE = "%B %d, %Y"
FORMAT_TIME = "%I:%M%p"
FORMAT_DATETIME = "%B %d, %Y %I:%M%p"
