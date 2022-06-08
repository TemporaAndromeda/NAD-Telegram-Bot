from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5187467076:AAFxOUJliE8G6UtcCEZLwogfahxFwfjR9HA", use_context=True)


def start(update: Update, x):
    update.message.reply_text(f"Hello!, Good day and Welcome to the Non-Academic Doubt Bot. Please click /help to see "
                              "the commands available.")


def Help(update: Update, x):
    update.message.reply_text("""Available Commands :-
    /links- For Telegram Batch Links & Youtube Channel Links.
    /In_Class - Tech Issues, Public Chat, Q/A Panel, Language.
    /Post_Class - Assignments, Replay, Notes, Tatva & Tests.
    /Courses - Enrollment into Micro Courses & Batch Change.
    /Teacher_Connect - Ask & Connect to your teacher.
    /Feedback - Post your Feedback.""")


def links(update: Update, x):
    update.message.reply_text("""Available Commands :-
        /Youtube- Youtube Channel Links.
        /Telegram - Batch Level Telegram Channel Links.""")


def telegram_grade(update: Update, x):
    update.message.reply_text("""Please select your Grade :-
    /Sankalp_12 - Telegram Batch links for Class 12.
    /Dhristi_11 - Telegram Batch links for Class 11.
    /Aakar_9_10 - Telegram Batch links for Class 9-10.
    /NEEV_6_8 - Telegram Batch links for Class 6-8.
    /Foundation_8_10 - Telegram Batch links for Foundation 8-10.
    """)


def telegram_course_12(update: Update, x):
    update.message.reply_text("""Please select your Grade :-
    /Sankalp_12_Live- Telegram Batch links for Class 12.
    /Sankalp_12_AI_Live- Telegram Batch links for Class 12 AI_Live.
    """)


def sankalp12_L(update: Update, x):
    update.message.reply_text("""Please select your level :-
    /JEE_t_12_L- Telegram Batch links for Class 12 JEE Live.
    /NEET_t_12_L - Telegram Batch links for Class 12 NEET Live.
    /CBSE_t_12_L - Telegram Batch links for Class 12 CBSE Live.
    /Commerce_t_12_L - Telegram Batch links for Class 12 Commerce Live.""")


def sankalp12_batch_name_jee(update: Update, x):
    update.message.reply_text("""Please select your batch :-
    /Sankalp_JEE_English_A -  English A Batch
    /Sankalp_JEE_Hinglish_A -  Hinglish A Batch
    /Sankalp_JEE_English_B -  English B Batch
    /Sankalp_JEE_Hinglish_B -  Hinglish B Batch
    /Sankalp_JEE_English_C -  English C Batch
    /Sankalp_JEE_English_D -  English D Batch
    /Sankalp_JEE_English_E -  English E Batch
    /Sankalp_JEE_Hinglish_I -  Hinglish I Batch
    /Sankalp_JEE_English_G -  English G Batch
       """)


def Sankalp_JEE_English_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+7YJLO9iQP2c0MzQ1 for Mobile & https://telegram.me/+7YJLO9iQP2c0MzQ1 for PC""")


def Sankalp_JEE_English_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+v459OgHMPrI1MzBl for Mobile &	https://telegram.me/+v459OgHMPrI1MzBl for PC""")


def Sankalp_JEE_Hinglish_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+WVov6bk0fKIxYTE1 for Mobile &	https://telegram.me/+WVov6bk0fKIxYTE1 for PC""")


def Sankalp_JEE_Hinglish_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+t5yjmCyKGMwwYTll for Mobile &	https://telegram.me/+t5yjmCyKGMwwYTll for PC""")


def Sankalp_JEE_English_C(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+gEUkYce8rZhjMjNl for Mobile & https://telegram.me/+gEUkYce8rZhjMjNl for PC""")


def Sankalp_JEE_English_D(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+tXl1eAntolMxZjA1 for Mobile &	https://telegram.me/+tXl1eAntolMxZjA1 for PC""")


def Sankalp_JEE_Hinglish_I(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+W9x4MZq-lsNlNTg1 for Mobile &	https://telegram.me/+W9x4MZq-lsNlNTg1 for PC""")


def Sankalp_JEE_English_E(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+8U3hszGY9OliOWU1 for Mobile &	https://telegram.me/+8U3hszGY9OliOWU1 for PC""")


def Sankalp_JEE_English_G(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+XXe3PvVZ0CE0ZDdl for Mobile &	https://telegram.me/+XXe3PvVZ0CE0ZDdl for PC""")


def sankalp12_batch_name_neet(update: Update, x):
    update.message.reply_text("""Please select your batch :-
    /Sankalp_NEET_English_A -  English A Batch
    /Sankalp_NEET_Hinglish_A -  Hinglish A Batch
    /Sankalp_NEET_English_B -  English B Batch
    /Sankalp_NEET_Hinglish_I -  Hinglish I Batch
       """)


def Sankalp_NEET_English_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+FsEkQXzWMqAyNGFl for Mobile &	https://telegram.me/+FsEkQXzWMqAyNGFl for PC""")


def Sankalp_NEET_English_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+-Q-ny3IidPhhZjU1 for Mobile &	https://telegram.me/+-Q-ny3IidPhhZjU1 for PC""")


def Sankalp_NEET_English_C(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+99iTlbE_ttU0NDQ1 for Mobile &	https://telegram.me/+99iTlbE_ttU0NDQ1 for PC""")


def Sankalp_NEET_English_D(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+Q9Oniw_-D-81MTQ1 for Mobile &	https://telegram.me/+Q9Oniw_-D-81MTQ1 for PC""")


def Sankalp_NEET_Hinglish_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+eiZgZDem2gZmYmFl for Mobile &	https://telegram.me/+eiZgZDem2gZmYmFl for PC""")


def Sankalp_NEET_Hinglish_I(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+pWB06_7Uh1ZmNjhl for Mobile &	https://telegram.me/+pWB06_7Uh1ZmNjhl for PC""")


def sankalp12_batch_name_cbse(update: Update, x):
    update.message.reply_text("""Please select your batch :-
    /Sankalp_CBSE_English_A -  English A Batch
    /Sankalp_CBSE_Hinglish_A -  Hinglish A Batch
    /Sankalp_CBSE_English_B -  English B Batch
    /Sankalp_CBSE_English_C -  English C Batch
       """)


def Sankalp_CBSE_English_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+57EgY0_Y3ThiZTFl for Mobile &	https://telegram.me/+57EgY0_Y3ThiZTFl for PC""")


def Sankalp_CBSE_English_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+4gZWSAlOBJVlYWVl for Mobile &	https://telegram.me/+4gZWSAlOBJVlYWVl for PC""")


def Sankalp_CBSE_Hinglish_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+q0OPkevUh0llZTBl for Mobile &	https://telegram.me/+q0OPkevUh0llZTBl for PC""")


def Sankalp_CBSE_English_C(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+4gZWSAlOBJVlYWVl for Mobile &	https://telegram.me/4gZWSAlOBJVlYWVl for PC""")


def sankalp12_batch_name_com(update: Update, x):
    update.message.reply_text("""Please select your batch :-
    /Sankalp_Com_Hinglish_A -  Hinglish A Batch
    /Sankalp_Com_Hinglish_B -  Hinglish B Batch
       """)


def Sankalp_Com_English_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+7WkNU6a45Yc0OWU1 for PC &	https://telegram.me/+7WkNU6a45Yc0OWU1 for Mobile""")


def Sankalp_Com_English_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: Batch not started""")


def Sankalp_Com_Hinglish_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: Batch not started""")


def Sankalp_Com_Hinglish_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: Batch not started""")


#######################################################################################################################


def sankalp12_AI_L(update: Update, x):
    update.message.reply_text("""Please select your level :-
    /JEE_t_12_AI_L- Telegram Batch links for Class 12 JEE AI Live.
    /NEET_t_12_AI_L - Telegram Batch links for Class 12 NEET AI Live.
    /CBSE_t_12_AI_L - Telegram Batch links for Class 12 CBSE AI Live.
    /Commerce_t_12_AI_L - Telegram Batch links for Class 12 Commerce AI Live.""")


def sankalp12_batch_name_jee_AI(update: Update, x):
    update.message.reply_text("""Please select your batch :-
    /Sankalp_JEE_English_AI_A -  English A Batch
    /Sankalp_JEE_Hinglish_AI_A -  Hinglish A Batch
    /Sankalp_JEE_English_AI_B -  English B Batch
    /Sankalp_JEE_Hinglish_AI_B -  Hinglish B Batch
    /Sankalp_JEE_English_AI_C -  English C Batch
    /Sankalp_JEE_Hinglish_AI_C -  Hinglish C Batch
    /Sankalp_JEE_English_AI_D -  English D Batch
    /Sankalp_JEE_Hinglish_AI_D -  Hinglish D Batch
    /Sankalp_JEE_English_AI_E -  English E Batch
       """)


def Sankalp_JEE_English_AI_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+T3LV796bgik2ZTI1 for Mobile &	https://telegram.me/+T3LV796bgik2ZTI1 for PC""")


def Sankalp_JEE_English_AI_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+CF6V71aHK_EyNWVl for Mobile &	https://telegram.me/+CF6V71aHK_EyNWVl for PC""")


def Sankalp_JEE_Hinglish_AI_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+8ngwGCmpLq8xNTVl for Mobile &	https://telegram.me/+8ngwGCmpLq8xNTVl for PC""")


def Sankalp_JEE_Hinglish_AI_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+URSVYzO9CpkyMmI1 for Mobile &	https://telegram.me/+URSVYzO9CpkyMmI1 for PC""")


def Sankalp_JEE_English_AI_C(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+l39q7Mkwn6ExYjll for Mobile &	https://telegram.me/+l39q7Mkwn6ExYjll for PC""")


def Sankalp_JEE_English_AI_D(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+68e6T98Lxf1mYWM1 for Mobile &	https://telegram.me/+68e6T98Lxf1mYWM1 for PC""")


def Sankalp_JEE_Hinglish_AI_C(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+HlD5ZOKeaHUxODNl for Mobile &	https://telegram.me/+HlD5ZOKeaHUxODNl for PC""")


def Sankalp_JEE_Hinglish_AI_D(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+T-WQcaT_23c0YWM1 for Mobile &	https://telegram.me/+T-WQcaT_23c0YWM1 for PC""")


def Sankalp_JEE_English_AI_E(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+bdzx0eNyMHhlNjA1 for Mobile &	https://telegram.me/+bdzx0eNyMHhlNjA1 for PC""")


def sankalp12_batch_name_neet_AI(update: Update, x):
    update.message.reply_text("""Please select your batch :-
    /Sankalp_NEET_English_AI_A -  English A Batch
    /Sankalp_NEET_Hinglish_AI_A -  Hinglish A Batch
    /Sankalp_NEET_English_AI_B -  English B Batch
    /Sankalp_NEET_Hinglish_AI_B -  Hinglish B Batch
       """)


def Sankalp_NEET_English_AI_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+HUJKSZRbdOo1MzE1 for Mobile &	https://telegram.me/+HUJKSZRbdOo1MzE1 for PC""")


def Sankalp_NEET_English_AI_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+NSoJf6BoyM85OGJl for Mobile &	https://telegram.me/+NSoJf6BoyM85OGJl for PC""")


def Sankalp_NEET_Hinglish_AI_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+_gGk48XoImBlYjA1 for Mobile &	https://telegram.me/+_gGk48XoImBlYjA1 for PC""")


def Sankalp_NEET_Hinglish_AI_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+VbIPwvFD7opiNGE1 for Mobile &	https://telegram.me/+VbIPwvFD7opiNGE1 for PC""")


def Sankalp_NEET_English_AI_C(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+5vCi8l5VhFJmZjFl for Mobile &	https://telegram.me/+5vCi8l5VhFJmZjFl  for PC""")


def Sankalp_NEET_English_AI_D(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+BROQqywllmc2M2U1 for Mobile &	https://telegram.me/+BROQqywllmc2M2U1 for PC""")


def Sankalp_NEET_Hinglish_AI_C(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+ZWmdOG1S0l8xOWNl for Mobile &	https://telegram.me/+ZWmdOG1S0l8xOWNl for PC""")


def Sankalp_NEET_Hinglish_AI_D(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+ZWmdOG1S0l8xOWNl for Mobile &	https://telegram.me/+ZWmdOG1S0l8xOWNl for PC""")


def sankalp12_batch_name_cbse_AI(update: Update, x):
    update.message.reply_text("""Please select your batch :-
    /Sankalp_CBSE_English_AI_A -  English A Batch
    /Sankalp_CBSE_Hinglish_AI_A -  Hinglish A Batch
    /Sankalp_CBSE_English_AI_B -  English B Batch
    /Sankalp_CBSE_Hinglish_AI_B -  Hinglish B Batch
       """)


def Sankalp_CBSE_English_AI_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+V0TLGiGbVGM0OTU9 for PC &	https://telegram.me/+V0TLGiGbVGM0OTU9 for Mobile""")


def Sankalp_CBSE_English_AI_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: Batch not started""")


def Sankalp_CBSE_Hinglish_AI_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+EtC4jl4rJ6NmNzNl for PC &	https://telegram.me/+EtC4jl4rJ6NmNzNl for Mobile""")


def Sankalp_CBSE_Hinglish_AI_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+TTZ4RFEr6-Y1OWZl for PC &	https://telegram.me/+TTZ4RFEr6-Y1OWZl for Mobile""")


def sankalp12_batch_name_com_AI(update: Update, x):
    update.message.reply_text("""Please select your batch :-
    /Sankalp_Com-Hinglish_AI_A -  Hinglish A Batch
    /Sankalp_Com-Hinglish_AI_B -  Hinglish B Batch
       """)


def Sankalp_Com_English_AI_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+V0TLGiGbVGM0OTU9 for PC &	https://telegram.me/+V0TLGiGbVGM0OTU9 for Mobile""")


def Sankalp_Com_English_AI_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: Batch not started""")


def Sankalp_Com_Hinglish_AI_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+uTCNSrEN8-1mZDA1 for PC &	https://telegram.me/+uTCNSrEN8-1mZDA1 for Mobile""")


def Sankalp_Com_Hinglish_AI_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+AutF1v773O01MWU1 for PC &	https://telegram.me/+AutF1v773O01MWU1 for Mobile""")


########################################################################################################################

def telegram_course_foun(update: Update, x):
    update.message.reply_text("""Please select your Grade :-
    /Foundation_Live- Telegram Batch links for Foundation Live.
    /Foundation_AI_Live- Telegram Batch links for Foundation AI_Live.
    """)


def foundation_L(update: Update, x):
    update.message.reply_text("""Please select your level :-
    /Foundation_8_L- Telegram Batch links for Grade 8 Foundation.
    /Foundation_9_L - Telegram Batch links for Grade 9 Foundation.
    /Foundation_10_L - Telegram Batch links for Grade 10 Foundation.""")


def Aakar_batch_name_foun_8(update: Update, x):
    update.message.reply_text("""Please select your batch :-
    /AakarFoundation_Eng_8_A -  English A Batch
    /AakarFoundation_Eng_8_B -  English B Batch
    /AakarFoundation_Eng_8_C -  English C Batch""")


def AakarFoundation_Eng_8_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+5d_Z-8rjVyhiMWY1 for Mobile & https://telegram.me/+5d_Z-8rjVyhiMWY1 for PC""")


def AakarFoundation_Eng_8_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+JmpRDZvZL-IxYjZl for Mobile &	https://telegram.me/+JmpRDZvZL-IxYjZl for PC""")


def AakarFoundation_Eng_8_C(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+4Z7I8a4wlNpiOWFl for Mobile &	https://telegram.me/+4Z7I8a4wlNpiOWFl for PC""")


def Aakar_batch_name_foun_9(update: Update, x):
    update.message.reply_text("""Please select your batch :-
    /AakarFoundation_Eng_9_A -  English A Batch
    /AakarFoundation_Eng_9_B -  English B Batch
    /AakarFoundation_Eng_9_C -  English C Batch
    /AakarFoundation_Eng_9_D -  English D Batch
    /AakarFoundation_Eng_9_E -  English E Batch """)


def AakarFoundation_Eng_9_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+J9qJu_h6Zlo2NTRl for Mobile &	https://telegram.me/+J9qJu_h6Zlo2NTRl for PC""")


def AakarFoundation_Eng_9_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+4qShitv5L8NhMDll for Mobile &	https://telegram.me/+4qShitv5L8NhMDll for PC""")


def AakarFoundation_Eng_9_C(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+JPs8jFRr77RjMGJl for Mobile &	https://telegram.me/+JPs8jFRr77RjMGJl for PC""")


def AakarFoundation_Eng_9_D(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+jiLkQ_JffbQzYTM1 for Mobile &	https://telegram.me/+jiLkQ_JffbQzYTM1 for PC""")


def AakarFoundation_Eng_9_E(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: Batch Not Started Yet""")


def Aakar_batch_name_foun_10(update: Update, x):
    update.message.reply_text("""Please select your batch :-
    /AakarFoundation_Eng_10_A -  English A Batch
    /AakarFoundation_Eng_10_B -  English B Batch
    /AakarFoundation_Eng_10_C -  English C Batch
    /AakarFoundation_Eng_10_D -  English D Batch
    /AakarFoundation_Eng_10_E -  English E Batch """)


def AakarFoundation_Eng_10_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+nRGQE2hJbPlhMGU1 for Mobile &	https://telegram.me/+nRGQE2hJbPlhMGU1 for PC""")


def AakarFoundation_Eng_10_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+6wQMwuT_fIAwZTJl for Mobile &	https://telegram.me/+6wQMwuT_fIAwZTJl for PC""")


def AakarFoundation_Eng_10_C(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+XEAliX12-C0wMjU1 for Mobile &	https://telegram.me/+XEAliX12-C0wMjU1 for PC""")


def AakarFoundation_Eng_10_D(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+U08k3fSIpIMzODdl for Mobile &	https://telegram.me/+U08k3fSIpIMzODdl for PC""")


def AakarFoundation_Eng_10_E(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: Batch Not Started Yet""")
#######################################################################################################################

def foundation_AI_L(update: Update, x):
    update.message.reply_text("""Please select your level :-
    /Foundation_8_AI_L- Telegram Batch links for Grade 8 AI Live Foundation.
    /Foundation_9_AI_L - Telegram Batch links for Grade 9 AI Live Foundation.
    /Foundation_10_AI_L - Telegram Batch links for Grade 10 AI Live Foundation.""")


def Aakar_batch_name_foun_8_AI(update: Update, x):
    update.message.reply_text("""Please select your batch :-
    /AakarFoundation_Eng_8_AI_A -  English A Batch
    /AakarFoundation_Eng_8_AI_B -  English B Batch
    /AakarFoundation_Eng_8_AI_C -  English C Batch""")


def AakarFoundation_Eng_8_AI_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+5nkgiyqImdM0YWZl for Mobile & https://telegram.me/+5nkgiyqImdM0YWZl for PC""")


def AakarFoundation_Eng_8_AI_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+A4SEu4Z-8aowZjFl for Mobile &	https://telegram.me/+A4SEu4Z-8aowZjFl for PC""")

def AakarFoundation_Eng_8_AI_C(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: Batch not started""")

def Aakar_batch_name_foun_9_AI(update: Update, x):
    update.message.reply_text("""Please select your batch :-
    /AakarFoundation_Eng_9_AI_A -  English A Batch
    /AakarFoundation_Eng_9_AI_B -  English B Batch
    /AakarFoundation_Eng_9_AI_C -  English C Batch
    /AakarFoundation_Eng_9_AI_D -  English D Batch
    /AakarFoundation_Eng_9_AI_E -  English E Batch """)


def AakarFoundation_Eng_9_AI_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+E6ffzd5eadU4MjNl for Mobile &	https://telegram.me/+E6ffzd5eadU4MjNl for PC""")


def AakarFoundation_Eng_9_AI_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+-YBSV-GeLcIwMWJl for Mobile &	https://telegram.me/+-YBSV-GeLcIwMWJl for PC""")


def AakarFoundation_Eng_9_AI_C(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: Batch Not Started""")


def AakarFoundation_Eng_9_AI_D(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: Batch Not Started""")


def AakarFoundation_Eng_9_AI_E(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: Batch Not Started""")


def Aakar_batch_name_foun_10_AI(update: Update, x):
    update.message.reply_text("""Please select your batch :-
    /AakarFoundation_Eng_10_AI_A -  English A Batch
    /AakarFoundation_Eng_10_AI_B -  English B Batch
    /AakarFoundation_Eng_10_AI_C -  English C Batch
    /AakarFoundation_Eng_10_AI_D -  English D Batch
    /AakarFoundation_Eng_10_AI_E -  English E Batch """)


def AakarFoundation_Eng_10_AI_A(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+5s1qEiKiJ8s2ZDQ1 for Mobile &	https://telegram.me/+5s1qEiKiJ8s2ZDQ1 for PC""")


def AakarFoundation_Eng_10_AI_B(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: https://t.me/+G82QJ58cLN4xOGY1 for Mobile &	https://telegram.me/+G82QJ58cLN4xOGY1 for PC""")


def AakarFoundation_Eng_10_AI_C(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: Batch Not Started""")


def AakarFoundation_Eng_10_AI_D(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: Batch Not Started""")


def AakarFoundation_Eng_10_AI_E(update: Update, x):
    update.message.reply_text("""The Telegram Link to the Batch 
    is: Batch Not Started""")

def gmail_url(update: Update, x):
    update.message.reply_text("Requesting you to mail vcare@vedantu.com or contact or "
                              "toll-free number: 1800-120-456-456 / +91 988-660-2456")


def youtube_sections(update: Update, x):
    update.message.reply_text("""Available Commands :-
    /JEE_y- To get the youtube Channel links for all JEE Related Content.
    /NEET_y - FTo get the youtube Channel links for all NEET Related Content.
    /10_y - To get the youtube Channel links for all Grade 10 Related Content.
    /9_y - To get the youtube Channel links for all Grade 9 Related Content
    /Foun_y - To get the youtube Channel links for all Foundation Related Content
    /V_help - To get the youtube Channel links for Vedantu-Help""")


def youtube_neet(update: Update, x):
    update.message.reply_text(
        "Here is your NEET Channel Link, https://www.youtube.com/channel/UCqaq3Cwa7m_EsqlvfZh6uyw Happy Doctoring!")


def youtube_jee(update: Update, x):
    update.message.reply_text("Here is your JEE Channel Link, "
                              "https://www.youtube.com/channel/UClaQJq84XMtMkL44zDmL-Tg Happy Engineering!")


def youtube_10(update: Update, x):
    update.message.reply_text("Here is your Grade 10 Channel Link, "
                              "https://www.youtube.com/channel/UCMY7ZvLB6-DnuSis_2s37_A Happy hunting!")


def youtube_9(update: Update, x):
    update.message.reply_text("Here is your Grade 9 Channel Link, "
                              "https://www.youtube.com/channel/UCMY7ZvLB6-DnuSis_2s37_A Happy hunting!")


def youtube_foun(update: Update, x):
    update.message.reply_text("Here is your Foundation Channel Link,"
                              " https://www.youtube.com/channel/UCMY7ZvLB6-DnuSis_2s37_A Happy hunting!")


def youtube_vhelp(update: Update, x):
    update.message.reply_text("Here is your V-Help Channel Link, "
                              "https://www.youtube.com/channel/UCnwgEnww4iOwiR_p2EaX7cg Happy hunting!")


def youtube_url(update: Update, x):
    update.message.reply_text("Youtube Link for V-Help Channel "
                              "=> \https://www.youtube.com/channel/UCnwgEnww4iOwiR_p2EaX7cg")


def notes_link(update: Update, x):
    update.message.reply_text("Dear Student, The notes are available on your dashboard under "
                              "Content-- Content Library. The notes will be available 1 hour after the session."
                              " You can refer this V Help video - https://youtu.be/f-PSaj-4Khk. "
                              "Please subscribe this youtube channel for more Help video about the Vedantu website.")


def unknown(update: Update, x):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, x):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(CommandHandler('help', Help))
updater.dispatcher.add_handler(CommandHandler('links', links))

updater.dispatcher.add_handler(CommandHandler('Telegram', telegram_grade))
updater.dispatcher.add_handler(CommandHandler('Sankalp_12', telegram_course_12))
updater.dispatcher.add_handler(CommandHandler('Foundation_8_10', telegram_course_foun))




updater.dispatcher.add_handler(CommandHandler('Sankalp_12_Live', sankalp12_L))

updater.dispatcher.add_handler(CommandHandler('JEE_t_12_L', sankalp12_batch_name_jee))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_English_A', Sankalp_JEE_English_A))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_English_B', Sankalp_JEE_English_B))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_Hinglish_A', Sankalp_JEE_Hinglish_A))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_Hinglish_B', Sankalp_JEE_Hinglish_B))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_English_C', Sankalp_JEE_English_C))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_English_D', Sankalp_JEE_English_D))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_English_E', Sankalp_JEE_English_E))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_Hinglish_I', Sankalp_JEE_Hinglish_I))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_English_G', Sankalp_JEE_English_G))

updater.dispatcher.add_handler(CommandHandler('NEET_t_12_L', sankalp12_batch_name_neet))
updater.dispatcher.add_handler(CommandHandler('Sankalp_NEET_English_A', Sankalp_NEET_English_A))
updater.dispatcher.add_handler(CommandHandler('Sankalp_NEET_English_B', Sankalp_NEET_English_B))
updater.dispatcher.add_handler(CommandHandler('Sankalp_NEET_English_C', Sankalp_NEET_English_C))
updater.dispatcher.add_handler(CommandHandler('Sankalp_NEET_English_D', Sankalp_NEET_English_D))
updater.dispatcher.add_handler(CommandHandler('Sankalp_NEET_Hinglish_A', Sankalp_NEET_Hinglish_A))
updater.dispatcher.add_handler(CommandHandler('Sankalp_NEET_Hinglish_I', Sankalp_NEET_Hinglish_I))

updater.dispatcher.add_handler(CommandHandler('CBSE_t_12_L', sankalp12_batch_name_neet))
updater.dispatcher.add_handler(CommandHandler('Sankalp_CBSE_English_A', Sankalp_CBSE_English_A))
updater.dispatcher.add_handler(CommandHandler('Sankalp_CBSE_English_B', Sankalp_CBSE_English_B))
updater.dispatcher.add_handler(CommandHandler('Sankalp_CBSE_Hinglish_A', Sankalp_CBSE_Hinglish_A))
updater.dispatcher.add_handler(CommandHandler('Sankalp_CBSE_English_C', Sankalp_CBSE_English_C))

updater.dispatcher.add_handler(CommandHandler('Commerce_t_12_L', sankalp12_batch_name_com))
updater.dispatcher.add_handler(CommandHandler('Sankalp_Com_Hinglish_A', Sankalp_Com_Hinglish_A))

updater.dispatcher.add_handler(CommandHandler('Sankalp_12_AI_Live', sankalp12_AI_L))

updater.dispatcher.add_handler(CommandHandler('JEE_t_12_AI_L', sankalp12_batch_name_jee_AI))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_English_AI_A', Sankalp_JEE_English_AI_A))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_English_AI_B', Sankalp_JEE_English_AI_B))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_Hinglish_AI_A', Sankalp_JEE_Hinglish_AI_A))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_Hinglish_AI_B', Sankalp_JEE_Hinglish_AI_B))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_English_AI_C', Sankalp_JEE_English_AI_C))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_English_AI_D', Sankalp_JEE_English_AI_D))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_Hinglish_AI_C', Sankalp_JEE_Hinglish_AI_C))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_Hinglish_AI_D', Sankalp_JEE_Hinglish_AI_D))
updater.dispatcher.add_handler(CommandHandler('Sankalp_JEE_English_AI_E', Sankalp_JEE_English_AI_E))

updater.dispatcher.add_handler(CommandHandler('NEET_t_12_AI_L', sankalp12_batch_name_neet))
updater.dispatcher.add_handler(CommandHandler('Sankalp_NEET_English_AI_A', Sankalp_NEET_English_AI_A))
updater.dispatcher.add_handler(CommandHandler('Sankalp_NEET_English_AI_B', Sankalp_NEET_English_AI_B))
updater.dispatcher.add_handler(CommandHandler('Sankalp_NEET_Hinglish_AI_A', Sankalp_NEET_Hinglish_AI_A))
updater.dispatcher.add_handler(CommandHandler('Sankalp_NEET_Hinglish_AI_B', Sankalp_NEET_Hinglish_AI_B))
updater.dispatcher.add_handler(CommandHandler('Sankalp_NEET_English_AI_C', Sankalp_NEET_English_AI_C))
updater.dispatcher.add_handler(CommandHandler('Sankalp_NEET_English_AI_D', Sankalp_NEET_English_AI_D))
updater.dispatcher.add_handler(CommandHandler('Sankalp_NEET_Hinglish_AI_C', Sankalp_NEET_Hinglish_AI_C))
updater.dispatcher.add_handler(CommandHandler('Sankalp_NEET_Hinglish_AI_D', Sankalp_NEET_Hinglish_AI_D))

updater.dispatcher.add_handler(CommandHandler('CBSE_t_12_AI_L', sankalp12_batch_name_neet))
updater.dispatcher.add_handler(CommandHandler('Sankalp_CBSE_English_AI_A', Sankalp_CBSE_English_AI_A))
updater.dispatcher.add_handler(CommandHandler('Sankalp_CBSE_English_AI_B', Sankalp_CBSE_English_AI_B))
updater.dispatcher.add_handler(CommandHandler('Sankalp_CBSE_Hinglish_AI_A', Sankalp_CBSE_Hinglish_AI_A))
updater.dispatcher.add_handler(CommandHandler('Sankalp_CBSE_Hinglish_AI_B', Sankalp_CBSE_Hinglish_AI_B))

updater.dispatcher.add_handler(CommandHandler('Commerce_t_12_AI_L', sankalp12_batch_name_com))
updater.dispatcher.add_handler(CommandHandler('Sankalp_Com_Hinglish_AI_A', Sankalp_Com_Hinglish_AI_A))
updater.dispatcher.add_handler(CommandHandler('Sankalp_Com_Hinglish_AI_B', Sankalp_Com_Hinglish_AI_B))


updater.dispatcher.add_handler(CommandHandler('Foundation_Live', foundation_L))

updater.dispatcher.add_handler(CommandHandler('Foundation_8_L', Aakar_batch_name_foun_8))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_8_A', AakarFoundation_Eng_8_A))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_8_B', AakarFoundation_Eng_8_B))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_8_C', AakarFoundation_Eng_8_C))

updater.dispatcher.add_handler(CommandHandler('Foundation_9_L', Aakar_batch_name_foun_9))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_9_A', AakarFoundation_Eng_9_A))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_9_B', AakarFoundation_Eng_9_B))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_9_C', AakarFoundation_Eng_9_C))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_9_D', AakarFoundation_Eng_9_D))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_9_E', AakarFoundation_Eng_9_E))

updater.dispatcher.add_handler(CommandHandler('Foundation_10_L', Aakar_batch_name_foun_10))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_10_A', AakarFoundation_Eng_10_A))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_10_B', AakarFoundation_Eng_10_B))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_10_C', AakarFoundation_Eng_10_C))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_10_D', AakarFoundation_Eng_10_D))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_10_E', AakarFoundation_Eng_10_E))



updater.dispatcher.add_handler(CommandHandler('Foundation_AI_Live', foundation_AI_L))

updater.dispatcher.add_handler(CommandHandler('Foundation_8_AI_L', Aakar_batch_name_foun_8_AI))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_8_AI_A', AakarFoundation_Eng_8_AI_A))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_8_AI_B', AakarFoundation_Eng_8_AI_B))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_8_AI_C', AakarFoundation_Eng_8_AI_C))

updater.dispatcher.add_handler(CommandHandler('Foundation_9_AI_L', Aakar_batch_name_foun_9_AI))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_9_AI_A', AakarFoundation_Eng_9_AI_A))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_9_AI_B', AakarFoundation_Eng_9_AI_B))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_9_AI_C', AakarFoundation_Eng_9_AI_C))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_9_AI_D', AakarFoundation_Eng_9_AI_D))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_9_AI_E', AakarFoundation_Eng_9_AI_E))

updater.dispatcher.add_handler(CommandHandler('Foundation_10_AI_L', Aakar_batch_name_foun_10_AI))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_10_AI_A', AakarFoundation_Eng_10_AI_A))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_10_AI_B', AakarFoundation_Eng_10_AI_B))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_10_AI_C', AakarFoundation_Eng_10_AI_C))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_10_AI_D', AakarFoundation_Eng_10_AI_D))
updater.dispatcher.add_handler(CommandHandler('AakarFoundation_Eng_10_AI_E', AakarFoundation_Eng_10_AI_E))

updater.dispatcher.add_handler(CommandHandler('Youtube', youtube_sections))
updater.dispatcher.add_handler(CommandHandler('JEE_y', youtube_jee))
updater.dispatcher.add_handler(CommandHandler('NEET_y', youtube_neet))
updater.dispatcher.add_handler(CommandHandler('10_y', youtube_10))
updater.dispatcher.add_handler(CommandHandler('9_y', youtube_9))
updater.dispatcher.add_handler(CommandHandler('Foun_y', youtube_foun))
updater.dispatcher.add_handler(CommandHandler('V_help', youtube_vhelp))

updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('notes', notes_link))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
