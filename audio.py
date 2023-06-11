import os


class Audio:

    def __init__(self, audio_filename, output_directory=""):
        self.audio_filename = audio_filename
        self.output_directory = output_directory

    def save_audio_file(self, audio_content):
        try:
            if not os.path.exists(self.output_directory) and self.output_directory != "":
                os.makedirs(self.output_directory)

            audio_path = os.path.join(self.output_directory, self.audio_filename)

            with open(audio_path, 'wb') as audio_file:
                audio_file.write(audio_content)

            return {"success" : True, "message" : "File saved successfully"}
        except Exception as err:
            return {"success": False, "message": err}




