REV_TOKEN =  "YmQyODZlZTgtMTExOS00MzJhLWIzZDItOTQzMzQyZjMzYmIzOnBsbElZWFkwVi1ETURKTndQN0ZOdjZvQVdxZndiTEZqNVEtV1BCeERUNlk="  #COOKIES (Token)
DEVICE_ID = "46887399-2d3f-431d-a6ec-557352cefe13" #x-device-id, all requests
GEN_NUMBER = 3 #HOW MANY CARDS TO GEN
EMPLOYEE_EMAIL = "xmaxlars@gmail.com" #WHICH TEAM MEMBER TO USE
CARD_PREFIX = "CARD_" #USED TO LABEL GENERATED CARDS
START_WITH_INDEX = 0 #INDEX WITH YOU WANT TO START CREATING YOUR CARD EX. (44) {CARD_PREFIX}_44, {CARD_PREFIX}_45...
SMS_VERIFICATION = True #USE True if you want to confirm sms code and store card information in "cards.csv"



##########################


BASE_URL = "https://business.revolut.com/api/"
CURRENT_USER = BASE_URL + "user/current"
