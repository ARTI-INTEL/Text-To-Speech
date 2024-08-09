from text_to_speech import save

text = str(input("Enter the text you want to conver to Speech: "))
language = str(input("Enter IETF Tag(https://en.wikipedia.org/wiki/IETF_language_tag#List_of_common_primary_language_subtags) of the lanuguage you want it in. en for English: "))
output_file = str(input("Enter the what you want you file name to be. DO NOT INCLUDE FILE TYPE: "))
inpslow = str(input("Do you want it to be said slowly? Y/N: "))

if inpslow == "N" or inpslow == "n":
    slow : bool = False

else:
    slow : bool = True

save(text, language, file=f"{output_file}.mp3")