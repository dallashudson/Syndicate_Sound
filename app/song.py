from datetime import datetime

class Song:
    def __init__(self, name, file_name, tags):
        today = date.today()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # upload date... obv

        self.name = name
        self.file_name = file_name
        self.upload_date = dt_string
        self.tags = tags.split(',') # tags will be entered like
                                    # (trap, bass, chicago)... this will
                                    # turn them into an array automatically
                                    # of tags

        #**NEED CLARIFICATION***
