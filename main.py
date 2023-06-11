from textToSpeech.textToSpeech import Audio, AudioRequest, File

url = "https://text-to-speech27.p.rapidapi.com/speech"

my_file = File('sample.pdf', working_dir='speeches')

text = my_file.read_file()["txt"]

querystring = {"text":text,"lang":"en-us"}

headers = {
	"X-RapidAPI-Key": "3a6096f673msh8d7876992e9f3bep1dd92fjsn60cddb7ef707",
	"X-RapidAPI-Host": "text-to-speech27.p.rapidapi.com"
}

audio_request = AudioRequest(url=url, querystring=querystring, headers=headers)
response = audio_request.request_audio_data()

audio = Audio(audio_filename="resumerrr.wav", output_directory="speeches")

result = audio.save_audio_file(response)

print(result["message"])