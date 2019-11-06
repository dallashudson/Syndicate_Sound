class User:
    def __init__(self, screen_name, username, email, password, **kwargs):
        #Required
        self.screen_name = screen_name
        self.username = username
        self.email = email
        self.password = password
        #Optional Using kwargs
        self.country = kwargs.get('country', None)
        self.state = kwargs.get('state', None)
        self.city = kwargs.get('city', None)
        #Default Init Stuff
        self.subscription = "Basic"
        self.songs = {}

        #calling convention user(screen_name, username... city='Austin'...)

    def upload_song(self, file_name, song_title, file_location, tags)
        self.songs[song_title] = file_location
